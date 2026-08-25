"""
Pull GSC data for mastermatchmakers.com using service account credentials.
Outputs structured JSON for the Master Matchmakers SEO growth roadmap deck.
"""
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY_FILE = r"C:\Users\jones\Downloads\embertribe-content-tools-e6776250739e (1).json"
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
SITE = "https://www.mastermatchmakers.com/"

START_DATE = "2025-12-01"
END_DATE   = "2026-05-31"

credentials = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
service = build("searchconsole", "v1", credentials=credentials)

def query_gsc(dimensions, row_limit=1000, start_row=0):
    body = {
        "startDate": START_DATE,
        "endDate": END_DATE,
        "dimensions": dimensions,
        "rowLimit": row_limit,
        "startRow": start_row,
    }
    return service.searchanalytics().query(siteUrl=SITE, body=body).execute()

# -- 1. Daily -> monthly + totals ---------------------------------------------
overall = query_gsc(["date"], row_limit=250)
rows = overall.get("rows", [])
total_clicks = sum(r["clicks"] for r in rows)
total_imps   = sum(r["impressions"] for r in rows)
days = len(rows)
by_month_clicks, by_month_imps = {}, {}
for r in rows:
    m = r["keys"][0][:7]
    by_month_clicks[m] = by_month_clicks.get(m, 0) + r["clicks"]
    by_month_imps[m]   = by_month_imps.get(m, 0) + r["impressions"]

print("=== TOTALS (%s to %s, %d days) ===" % (START_DATE, END_DATE, days))
print("  clicks: %s | impressions: %s | CTR %.2f%%" % (
    f"{total_clicks:,}", f"{total_imps:,}",
    (total_clicks/total_imps*100 if total_imps else 0)))
print("\n=== BY MONTH ===")
for m in sorted(by_month_clicks):
    print("  %s: %s clicks | %s imps" % (m, f"{by_month_clicks[m]:,}", f"{by_month_imps[m]:,}"))

# -- 2. All queries (paged) ----------------------------------------------------
all_q = []
start = 0
while True:
    resp = query_gsc(["query"], row_limit=5000, start_row=start)
    batch = resp.get("rows", [])
    all_q.extend(batch)
    if len(batch) < 5000:
        break
    start += 5000
print("\nTotal queries returned: %d" % len(all_q))

BRAND_TOKENS = ["master match", "mastermatch", "master-match"]
def is_branded(q):
    ql = q.lower()
    return any(t in ql for t in BRAND_TOKENS)

branded   = [r for r in all_q if is_branded(r["keys"][0])]
unbranded = [r for r in all_q if not is_branded(r["keys"][0])]
b_clicks = sum(r["clicks"] for r in branded)
u_clicks = sum(r["clicks"] for r in unbranded)
print("Branded clicks: %s | Non-branded clicks: %s" % (f"{b_clicks:,}", f"{u_clicks:,}"))

# -- 3. Top non-branded queries ------------------------------------------------
top_unbranded = sorted(unbranded, key=lambda r: r["clicks"], reverse=True)[:40]
print("\n=== TOP 40 NON-BRANDED QUERIES (by clicks) ===")
for r in top_unbranded:
    print("  %6s clicks | %8s imps | pos %5.1f | %s" % (
        f"{r['clicks']:,}", f"{r['impressions']:,}", r["position"], r["keys"][0]))

# -- 4. Striking distance: non-branded, position 11-30, by impressions ---------
sd = [r for r in unbranded if 11 <= r["position"] <= 30]
sd.sort(key=lambda r: r["impressions"], reverse=True)
print("\n=== STRIKING DISTANCE (non-branded, pos 11-30) ===")
print("Count: %d | total impressions: %s" % (len(sd), f"{sum(r['impressions'] for r in sd):,}"))
for r in sd[:30]:
    print("  pos %5.1f | %8s imps | %5s clicks | %s" % (
        r["position"], f"{r['impressions']:,}", f"{r['clicks']:,}", r["keys"][0]))

# Page-2+ demand: impressions where you rank but rarely get clicked
page2plus = [r for r in unbranded if r["position"] > 10]
p2_imps = sum(r["impressions"] for r in page2plus)
p2_clicks = sum(r["clicks"] for r in page2plus)
print("\nNon-branded queries beyond page 1: %d | imps %s | clicks %s" % (
    len(page2plus), f"{p2_imps:,}", f"{p2_clicks:,}"))

# -- 5. Local intent: "[city] matchmaker" style queries -------------------------
local_terms = ["near me", "matchmaker in", "matchmakers in"]
CITIES = ["new york","nyc","los angeles","chicago","houston","philadelphia","phoenix",
          "san diego","dallas","austin","san francisco","seattle","denver","boston",
          "atlanta","miami","tampa","orlando","charlotte","pittsburgh","cleveland",
          "columbus","detroit","baltimore","raleigh","cincinnati","milwaukee",
          "louisville","buffalo","hartford","birmingham","knoxville","boise",
          "des moines","naples","spokane","albuquerque","tucson","memphis","reno",
          "tulsa","omaha","sacramento","new jersey","las vegas","fort worth",
          "portland","nashville","st louis","colorado springs","jacksonville",
          "minneapolis","san antonio","washington","scottsdale"]
def is_local(q):
    ql = q.lower()
    return any(t in ql for t in local_terms) or any(c in ql for c in CITIES)
local_q = [r for r in unbranded if is_local(r["keys"][0])]
local_q.sort(key=lambda r: r["impressions"], reverse=True)
print("\n=== LOCAL-INTENT NON-BRANDED QUERIES ===")
print("Count: %d | imps %s | clicks %s" % (
    len(local_q), f"{sum(r['impressions'] for r in local_q):,}",
    f"{sum(r['clicks'] for r in local_q):,}"))
for r in local_q[:25]:
    print("  pos %5.1f | %8s imps | %5s clicks | %s" % (
        r["position"], f"{r['impressions']:,}", f"{r['clicks']:,}", r["keys"][0]))

# -- 6. Top pages ----------------------------------------------------------------
top_pages = query_gsc(["page"], row_limit=50)
print("\n=== TOP 25 PAGES ===")
for r in top_pages.get("rows", [])[:25]:
    page = r["keys"][0].replace("https://www.mastermatchmakers.com", "")
    print("  %6s clicks | %8s imps | pos %5.1f | %s" % (
        f"{r['clicks']:,}", f"{r['impressions']:,}", r["position"], page))

# -- 7. Save ----------------------------------------------------------------------
def slim(r):
    return {"query": r["keys"][0], "clicks": r["clicks"], "impressions": r["impressions"],
            "ctr_pct": round(r["ctr"]*100, 2), "position": round(r["position"], 1)}

output = {
    "property": SITE,
    "start_date": START_DATE,
    "end_date": END_DATE,
    "totals": {
        "total_clicks": total_clicks,
        "total_impressions": total_imps,
        "days": days,
        "overall_ctr_pct": round(total_clicks/total_imps*100, 2) if total_imps else 0,
        "branded_clicks": b_clicks,
        "nonbranded_clicks": u_clicks,
        "total_queries": len(all_q),
        "nonbranded_queries": len(unbranded),
    },
    "by_month_clicks": by_month_clicks,
    "by_month_impressions": by_month_imps,
    "top_nonbranded_queries": [slim(r) for r in top_unbranded],
    "striking_distance": {
        "count": len(sd),
        "total_impressions": sum(r["impressions"] for r in sd),
        "top": [slim(r) for r in sd[:50]],
    },
    "page2_plus": {"count": len(page2plus), "impressions": p2_imps, "clicks": p2_clicks},
    "local_intent": {
        "count": len(local_q),
        "impressions": sum(r["impressions"] for r in local_q),
        "clicks": sum(r["clicks"] for r in local_q),
        "top": [slim(r) for r in local_q[:50]],
    },
    "top_pages": [
        {"page": r["keys"][0].replace("https://www.mastermatchmakers.com", ""),
         "clicks": r["clicks"], "impressions": r["impressions"],
         "ctr_pct": round(r["ctr"]*100, 2), "position": round(r["position"], 1)}
        for r in top_pages.get("rows", [])[:50]
    ],
}
with open(r"C:\Users\jones\Claude\gsc-master-matchmakers.json", "w") as f:
    json.dump(output, f, indent=2)
print("\nSaved to gsc-master-matchmakers.json")
