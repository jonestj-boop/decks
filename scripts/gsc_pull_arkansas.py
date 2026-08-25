"""
Pull GSC data for arkansaspropertybuyers.com.
Focus: how published articles/blog content have ranked since publishing (Oct 2025+).
"""
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY_FILE = r"C:\Users\jones\Downloads\embertribe-content-tools-e6776250739e (1).json"
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]

credentials = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
service = build("searchconsole", "v1", credentials=credentials)

# --- List all properties + find arkansas ---
print("=== AVAILABLE PROPERTIES ===")
sites = service.sites().list().execute()
for s in sites.get("siteEntry", []):
    print(f"  {s['permissionLevel']:<20} {s['siteUrl']}")

site_url = None
for s in sites.get("siteEntry", []):
    if "arkansaspropertybuyers" in s["siteUrl"].lower():
        site_url = s["siteUrl"]
        break

if not site_url:
    for candidate in ["https://www.arkansaspropertybuyers.com/",
                      "https://arkansaspropertybuyers.com/",
                      "sc-domain:arkansaspropertybuyers.com"]:
        try:
            service.sites().get(siteUrl=candidate).execute()
            site_url = candidate
            break
        except Exception as e:
            print(f"  {candidate}: {e}")

if not site_url:
    print("Could not find arkansaspropertybuyers property.")
    raise SystemExit(1)

print(f"\nUsing property: {site_url}")

START_DATE = "2025-10-01"
END_DATE   = "2026-06-23"

def query_gsc(dimensions, row_limit=1000, start_row=0, filters=None):
    body = {
        "startDate": START_DATE,
        "endDate": END_DATE,
        "dimensions": dimensions,
        "rowLimit": row_limit,
        "startRow": start_row,
    }
    if filters:
        body["dimensionFilterGroups"] = filters
    return service.searchanalytics().query(siteUrl=site_url, body=body).execute()

# -- Totals + monthly --
overall = query_gsc(["date"], row_limit=400)
rows = overall.get("rows", [])
total_clicks = sum(r["clicks"] for r in rows)
total_imps   = sum(r["impressions"] for r in rows)
by_month_clicks, by_month_imps = {}, {}
for r in rows:
    m = r["keys"][0][:7]
    by_month_clicks[m] = by_month_clicks.get(m, 0) + r["clicks"]
    by_month_imps[m]   = by_month_imps.get(m, 0) + r["impressions"]

print("\n=== TOTALS (%s to %s) ===" % (START_DATE, END_DATE))
print("  clicks: %s | impressions: %s | CTR %.2f%%" % (
    f"{total_clicks:,}", f"{total_imps:,}",
    (total_clicks/total_imps*100 if total_imps else 0)))
print("\n=== BY MONTH ===")
for m in sorted(by_month_clicks):
    print("  %s: %6s clicks | %8s imps" % (m, f"{by_month_clicks[m]:,}", f"{by_month_imps[m]:,}"))

# -- All pages (paged) --
all_pages = []
start = 0
while True:
    resp = query_gsc(["page"], row_limit=5000, start_row=start)
    batch = resp.get("rows", [])
    all_pages.extend(batch)
    if len(batch) < 5000:
        break
    start += 5000

all_pages.sort(key=lambda r: r["clicks"], reverse=True)
print("\n=== ALL PAGES (%d) ===" % len(all_pages))
for r in all_pages:
    page = r["keys"][0]
    print("  %5s clicks | %7s imps | pos %5.1f | ctr %4.1f%% | %s" % (
        f"{r['clicks']:,}", f"{r['impressions']:,}", r["position"], r["ctr"]*100, page))

# -- All queries (paged) --
all_q = []
start = 0
while True:
    resp = query_gsc(["query"], row_limit=5000, start_row=start)
    batch = resp.get("rows", [])
    all_q.extend(batch)
    if len(batch) < 5000:
        break
    start += 5000
all_q.sort(key=lambda r: r["clicks"], reverse=True)
print("\n=== TOP 40 QUERIES (%d total) ===" % len(all_q))
for r in all_q[:40]:
    print("  %5s clicks | %7s imps | pos %5.1f | %s" % (
        f"{r['clicks']:,}", f"{r['impressions']:,}", r["position"], r["keys"][0]))

# -- Save raw --
def slim_p(r):
    return {"page": r["keys"][0], "clicks": r["clicks"], "impressions": r["impressions"],
            "ctr_pct": round(r["ctr"]*100, 2), "position": round(r["position"], 1)}
def slim_q(r):
    return {"query": r["keys"][0], "clicks": r["clicks"], "impressions": r["impressions"],
            "ctr_pct": round(r["ctr"]*100, 2), "position": round(r["position"], 1)}

output = {
    "property": site_url,
    "start_date": START_DATE,
    "end_date": END_DATE,
    "totals": {
        "total_clicks": total_clicks,
        "total_impressions": total_imps,
        "overall_ctr_pct": round(total_clicks/total_imps*100, 2) if total_imps else 0,
    },
    "by_month_clicks": by_month_clicks,
    "by_month_impressions": by_month_imps,
    "all_pages": [slim_p(r) for r in all_pages],
    "all_queries": [slim_q(r) for r in all_q],
}
with open(r"C:\Users\jones\Claude\gsc-arkansas.json", "w") as f:
    json.dump(output, f, indent=2)
print("\nSaved to gsc-arkansas.json")
