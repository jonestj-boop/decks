"""
Full-engagement traffic analysis for lendforall.ca.
Monthly arc (16 mo), recent vs baseline queries/pages, CTR + position trend.
"""
import json
from datetime import date, timedelta
from urllib.parse import urlparse
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY_FILE = r"C:\Users\jones\Downloads\embertribe-content-tools-e6776250739e (1).json"
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
service = build("searchconsole", "v1", credentials=creds)
site = "sc-domain:lendforall.ca"
try:
    service.sites().get(siteUrl=site).execute()
except Exception:
    site = "https://lendforall.ca/"

TODAY = date.today()

def q(start, end, dims, row_limit=25000):
    body = {"startDate": start, "endDate": end, "dimensions": dims, "rowLimit": row_limit}
    return service.searchanalytics().query(siteUrl=site, body=body).execute().get("rows", [])

# ---- Monthly arc (last ~16 months) ----
start16 = (TODAY - timedelta(days=490)).isoformat()
daily = q(start16, TODAY.isoformat(), ["date"], row_limit=600)
monthly = {}
for r in daily:
    m = r["keys"][0][:7]
    e = monthly.setdefault(m, {"clicks": 0, "impressions": 0, "days": 0, "pos_wt": 0})
    e["clicks"] += r["clicks"]; e["impressions"] += r["impressions"]; e["days"] += 1
    e["pos_wt"] += r["position"] * r["impressions"]
for m, e in monthly.items():
    e["ctr"] = round(100 * e["clicks"] / e["impressions"], 2) if e["impressions"] else 0
    e["avg_pos"] = round(e["pos_wt"] / e["impressions"], 1) if e["impressions"] else 0
    del e["pos_wt"]

# ---- Recent 90d vs baseline 90d ----
rec_e = (TODAY - timedelta(days=2)).isoformat()
rec_s = (TODAY - timedelta(days=92)).isoformat()
# baseline = the 90d a year ago (pre-/early-engagement)
base_e = (TODAY - timedelta(days=367)).isoformat()
base_s = (TODAY - timedelta(days=457)).isoformat()

def totals(rows):
    c = sum(r["clicks"] for r in rows); i = sum(r["impressions"] for r in rows)
    return {"clicks": c, "impressions": i, "ctr": round(100*c/i,2) if i else 0}

rec_tot = totals(q(rec_s, rec_e, ["date"], 200))
base_tot = totals(q(base_s, base_e, ["date"], 200))

def keyed(rows):
    return {r["keys"][0]: r for r in rows}
q_rec = keyed(q(rec_s, rec_e, ["query"], 5000))
q_base = keyed(q(base_s, base_e, ["query"], 5000))
p_rec = q(rec_s, rec_e, ["page"], 5000)

MONEY = ["loans for bad credit","bad credit loans","bad credit loans canada",
         "loans for bad credit canada","personal loans canada","no credit check loans canada",
         "payday loans","installment loans canada","debt consolidation loans"]
money = []
for k in MONEY:
    r = q_rec.get(k); b = q_base.get(k)
    if r:
        money.append({"q":k,"now_pos":round(r["position"],1),"now_clicks":r["clicks"],
                      "now_impr":r["impressions"],
                      "base_pos":round(b["position"],1) if b else None,
                      "base_clicks":b["clicks"] if b else 0})

top_q = sorted(q_rec.values(), key=lambda r:r["clicks"], reverse=True)[:20]
top_p = sorted(p_rec, key=lambda r:r["clicks"], reverse=True)[:15]

out = {
  "generated": rec_e, "property": site,
  "monthly": dict(sorted(monthly.items())),
  "recent_90d": {"range":[rec_s,rec_e], **rec_tot},
  "baseline_90d": {"range":[base_s,base_e], **base_tot},
  "money_terms": money,
  "top_queries": [{"q":r["keys"][0],"clicks":r["clicks"],"impr":r["impressions"],"pos":round(r["position"],1)} for r in top_q],
  "top_pages": [{"page":urlparse(r["keys"][0]).path,"clicks":r["clicks"],"impr":r["impressions"],"pos":round(r["position"],1)} for r in top_p],
}
json.dump(out, open(r"C:\Users\jones\Claude\lendforall-engagement-traffic.json","w"), indent=2)

print("MONTHLY ARC:")
for m,e in sorted(monthly.items()):
    print(f"  {m}: {e['clicks']:>5} clk | {e['impressions']:>7} impr | CTR {e['ctr']:>4}% | pos {e['avg_pos']:>4} | {e['days']}d")
print(f"\nRECENT 90d:  {rec_tot}  ({rec_s}..{rec_e})")
print(f"BASELINE 90d:{base_tot}  ({base_s}..{base_e})")
print("\nMONEY TERMS (base_pos -> now_pos | now_clicks):")
for m in money:
    print(f"  {str(m['base_pos']):>5} -> {m['now_pos']:>5} | {m['now_clicks']:>3} clk | {m['q']}")
print("\nTOP QUERIES NOW:")
for r in out["top_queries"][:12]:
    print(f"  {r['clicks']:>4} clk | {r['impr']:>6} impr | pos {r['pos']:>4} | {r['q']}")
