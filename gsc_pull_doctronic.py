"""
Pull GSC data for doctronic.ai — penalty investigation.
Date range covers 16 months to capture pre/post penalty trend.
"""
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY_FILE = r"C:\Users\jones\Claude\embertribe-content-tools-e6776250739e.json"
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
SITE_URL = "sc-domain:doctronic.ai"

START_DATE = "2025-02-01"
END_DATE   = "2026-05-31"

credentials = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
service = build("searchconsole", "v1", credentials=credentials)

def query(dimensions, row_limit=1000, filters=None):
    body = {
        "startDate": START_DATE,
        "endDate": END_DATE,
        "dimensions": dimensions,
        "rowLimit": row_limit,
    }
    if filters:
        body["dimensionFilterGroups"] = filters
    return service.searchanalytics().query(siteUrl=SITE_URL, body=body).execute()

# 1. By date (daily clicks/impressions for trend)
print("Pulling daily data...")
daily = query(["date"], row_limit=500)

# 2. By month summary
by_month = {}
by_month_imps = {}
for row in daily.get("rows", []):
    m = row["keys"][0][:7]
    by_month[m] = by_month.get(m, 0) + row["clicks"]
    by_month_imps[m] = by_month_imps.get(m, 0) + row["impressions"]

print("\n=== CLICKS & IMPRESSIONS BY MONTH ===")
for m in sorted(by_month):
    print(f"  {m}: {by_month[m]:>8,} clicks | {by_month_imps[m]:>10,} imps")

# 3. Top queries
print("\nPulling top queries...")
top_queries = query(["query"], row_limit=50)
print("\n=== TOP 50 QUERIES (by clicks) ===")
for r in top_queries.get("rows", []):
    print(f"  {r['clicks']:>6,} clicks | {r['impressions']:>8,} imps | pos {r['position']:.1f} | {r['keys'][0]}")

# 4. Top pages
print("\nPulling top pages...")
top_pages = query(["page"], row_limit=50)
print("\n=== TOP 50 PAGES (by clicks) ===")
for r in top_pages.get("rows", []):
    page = r["keys"][0].replace("https://doctronic.ai", "").replace("https://www.doctronic.ai", "")
    print(f"  {r['clicks']:>6,} clicks | {r['impressions']:>8,} imps | pos {r['position']:.1f} | {page}")

# 5. Country breakdown
print("\nPulling country data...")
countries = query(["country"], row_limit=20)
print("\n=== TOP COUNTRIES ===")
for r in countries.get("rows", []):
    print(f"  {r['clicks']:>6,} clicks | {r['impressions']:>8,} imps | {r['keys'][0]}")

# 6. Device breakdown
devices = query(["device"], row_limit=10)
print("\n=== DEVICE BREAKDOWN ===")
for r in devices.get("rows", []):
    print(f"  {r['clicks']:>6,} clicks | {r['keys'][0]}")

# 7. Save JSON
total_clicks = sum(r["clicks"] for r in daily.get("rows", []))
total_imps   = sum(r["impressions"] for r in daily.get("rows", []))

output = {
    "property": SITE_URL,
    "start_date": START_DATE,
    "end_date": END_DATE,
    "totals": {
        "total_clicks": total_clicks,
        "total_impressions": total_imps,
    },
    "by_month": by_month,
    "by_month_impressions": by_month_imps,
    "top_queries": [
        {
            "query": r["keys"][0],
            "clicks": r["clicks"],
            "impressions": r["impressions"],
            "ctr_pct": round(r["ctr"] * 100, 2),
            "position": round(r["position"], 1),
        }
        for r in top_queries.get("rows", [])
    ],
    "top_pages": [
        {
            "page": r["keys"][0].replace("https://doctronic.ai", "").replace("https://www.doctronic.ai", ""),
            "clicks": r["clicks"],
            "impressions": r["impressions"],
            "ctr_pct": round(r["ctr"] * 100, 2),
            "position": round(r["position"], 1),
        }
        for r in top_pages.get("rows", [])
    ],
    "countries": [
        {"country": r["keys"][0], "clicks": r["clicks"], "impressions": r["impressions"]}
        for r in countries.get("rows", [])
    ],
    "devices": [
        {"device": r["keys"][0], "clicks": r["clicks"]}
        for r in devices.get("rows", [])
    ],
}

with open(r"C:\Users\jones\Claude\gsc-doctronic.json", "w") as f:
    json.dump(output, f, indent=2)
print("\nSaved to gsc-doctronic.json")
