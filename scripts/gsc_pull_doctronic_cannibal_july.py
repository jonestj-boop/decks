"""
Doctronic.ai — GSC query x page pull to refresh the cannibalization analysis.
Window: Jun 1 - Jul 28, 2026 (a current ~2-month window, matching the original
Mar 30 - May 29 analysis span). Finds queries where 2+ /blog/ pages compete,
splitting impressions. Rebuilds the deck's `cannibal` structure.
"""
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY = r"C:\Users\jones\Claude\embertribe-content-tools-e6776250739e.json"
SITE = "sc-domain:doctronic.ai"
creds = service_account.Credentials.from_service_account_file(
    KEY, scopes=["https://www.googleapis.com/auth/webmasters.readonly"])
svc = build("searchconsole", "v1", credentials=creds)

START, END = "2026-06-01", "2026-07-28"
blog_filter = [{"filters": [{"dimension": "page", "operator": "contains", "expression": "/blog/"}]}]

rows, sr = [], 0
while True:
    body = {"startDate": START, "endDate": END, "dimensions": ["query", "page"],
            "rowLimit": 25000, "startRow": sr, "dimensionFilterGroups": blog_filter}
    batch = svc.searchanalytics().query(siteUrl=SITE, body=body).execute().get("rows", [])
    rows += batch
    if len(batch) < 25000:
        break
    sr += 25000
print(f"pulled {len(rows)} query x page rows")

# load is_et classification from the existing deck blob
with open(r"decks/doctronic/content-audit.html", encoding="utf-8") as f:
    html = f.read()
i = html.find('id="jd"'); s = html.index(">", i) + 1; e = html.index("</script>", s)
blob = json.loads(html[s:e])
is_et = {}
for lst in list(blob["rows"].values()) + [blob["declining"], blob["et_top"], blob["dt_top"]]:
    for r in lst:
        if r.get("url"):
            is_et[r["url"].rstrip("/")] = r.get("is_et")

def slug(u):
    return u.rstrip("/").split("/blog/")[-1]

# group by query
groups = {}
for r in rows:
    q, page = r["keys"]
    groups.setdefault(q, []).append({
        "url": page, "slug": slug(page),
        "clicks": round(r["clicks"]), "impr": round(r["impressions"]),
        "pos": round(r["position"], 1), "is_et": is_et.get(page.rstrip("/"))})

out_groups = []
for q, pages in groups.items():
    if len(pages) < 2:
        continue
    pages.sort(key=lambda p: -p["impr"])
    total_impr = sum(p["impr"] for p in pages)
    total_clicks = sum(p["clicks"] for p in pages)
    if total_impr < 2000:   # ignore trivial splits
        continue
    # severity by split impressions
    sev = "High" if total_impr >= 20000 else "Medium" if total_impr >= 5000 else "Low"
    # est click loss: if consolidated to best position, assume top page's CTR on all impressions
    best = pages[0]
    best_ctr = (best["clicks"] / best["impr"]) if best["impr"] else 0
    est_consolidated = best_ctr * total_impr
    click_loss = max(0, round(est_consolidated - total_clicks))
    ets = [p["is_et"] for p in pages if p["is_et"] is not None]
    if ets and all(ets):
        ct = "ET vs ET"
    elif ets and not any(ets):
        ct = "DT vs DT"
    elif True in ets and False in ets:
        ct = "ET vs DT"
    else:
        ct = "Mixed"
    out_groups.append({
        "query": q, "severity": sev, "conflict_type": ct,
        "page_count": len(pages), "total_impr": total_impr,
        "total_clicks": total_clicks, "click_loss": click_loss,
        "pages": [{"slug": p["slug"], "url": p["url"], "pos": p["pos"], "clicks": p["clicks"]}
                  for p in pages[:6]]})

out_groups.sort(key=lambda g: -g["total_impr"])
sev_counts = {s: sum(1 for g in out_groups if g["severity"] == s) for s in ["High", "Medium", "Low"]}
conflict_counts = {}
for g in out_groups:
    conflict_counts[g["conflict_type"]] = conflict_counts.get(g["conflict_type"], 0) + 1
total_loss = sum(g["click_loss"] for g in out_groups)

cannibal = {
    "range": f"{START} to {END}",
    "total_groups": len(out_groups),
    "total_click_loss": total_loss,
    "conflict_counts": conflict_counts,
    "sev_counts": sev_counts,
    "groups": out_groups[:200]}

print(f"groups (2+ pages, >=2K impr): {len(out_groups)}")
print(f"severity: {sev_counts}")
print(f"conflict types: {conflict_counts}")
print(f"est total click loss/mo (~2mo window): {total_loss:,}")
print("\ntop 8 by split impressions:")
for g in out_groups[:8]:
    print(f"  {g['total_impr']:>7,} impr | {g['page_count']}p | {g['severity']:6} | {g['conflict_type']:9} | {g['query'][:40]}")

with open(r"C:\Users\jones\Claude\gsc-doctronic-cannibal-july.json", "w") as f:
    json.dump(cannibal, f, indent=2)
print("\nSaved gsc-doctronic-cannibal-july.json")
