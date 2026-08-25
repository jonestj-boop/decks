"""
Same Day Diplomas — GSC re-pull for check-in call.
Baseline in the deck was 90 days Feb-Apr 2026: 10,280 non-branded clicks (93.3%),
739 branded clicks (6.7%). Pull current 90-day window and compare.
"""
import json
from datetime import date, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY_FILE = r"C:\Users\jones\Downloads\embertribe-content-tools-e6776250739e (1).json"
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]

credentials = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
service = build("searchconsole", "v1", credentials=credentials)

print("=== AVAILABLE PROPERTIES ===")
sites = service.sites().list().execute()
site_entries = sites.get("siteEntry", [])
for s in site_entries:
    print(f"  {s['siteUrl']}  ({s['permissionLevel']})")

target_url = None
for s in site_entries:
    if "samedaydiplomas" in s["siteUrl"].lower():
        target_url = s["siteUrl"]
        break

if not target_url:
    print("\nNo samedaydiplomas property found. Trying common formats...")
    for candidate in ["https://samedaydiplomas.com/", "sc-domain:samedaydiplomas.com"]:
        try:
            service.sites().get(siteUrl=candidate).execute()
            target_url = candidate
            print(f"Found: {candidate}")
            break
        except Exception as e:
            print(f"  {candidate}: {e}")

if not target_url:
    print("Could not find samedaydiplomas.com property. Stopping.")
    exit(1)

print(f"\nUsing property: {target_url}")

TODAY = date.today()
END_DATE = str(TODAY - timedelta(days=2))  # GSC data lags ~2 days
START_DATE = str(TODAY - timedelta(days=91))

def query_gsc(dimensions, row_limit=1000, filters=None):
    body = {
        "startDate": START_DATE,
        "endDate": END_DATE,
        "dimensions": dimensions,
        "rowLimit": row_limit,
    }
    if filters:
        body["dimensionFilterGroups"] = filters
    return service.searchanalytics().query(siteUrl=target_url, body=body).execute()

print(f"\n=== OVERALL TOTALS ({START_DATE} to {END_DATE}) ===")
overall = query_gsc(["date"], row_limit=200)
total_clicks = sum(r["clicks"] for r in overall.get("rows", []))
total_imps = sum(r["impressions"] for r in overall.get("rows", []))
avg_ctr = round(total_clicks / total_imps * 100, 2) if total_imps else 0
print(f"  Total clicks:       {total_clicks:,.0f}")
print(f"  Total impressions:  {total_imps:,.0f}")
print(f"  Overall CTR:        {avg_ctr}%")

print("\n=== BRANDED VS NON-BRANDED ===")
all_queries = query_gsc(["query"], row_limit=1000)
rows = all_queries.get("rows", [])
branded_terms = ["same day diploma", "samedaydiplomas", "same day diplomas"]
branded_clicks = sum(r["clicks"] for r in rows if any(t in r["keys"][0].lower() for t in branded_terms))
nonbranded_clicks = total_clicks - branded_clicks
branded_pct = round(branded_clicks / total_clicks * 100, 1) if total_clicks else 0
nonbranded_pct = round(100 - branded_pct, 1)
print(f"  Non-branded: {nonbranded_clicks:,.0f} clicks ({nonbranded_pct}%)")
print(f"  Branded:     {branded_clicks:,.0f} clicks ({branded_pct}%)")

print("\n=== TOP 30 QUERIES (by clicks) ===")
top_queries = query_gsc(["query"], row_limit=30)
for r in top_queries.get("rows", []):
    print(f"  {r['clicks']:>6,.0f} clicks | {r['impressions']:>8,.0f} imps | pos {r['position']:.1f} | {r['keys'][0]}")

print("\n=== TOP 30 PAGES (by clicks) ===")
top_pages = query_gsc(["page"], row_limit=30)
for r in top_pages.get("rows", []):
    page = r["keys"][0].replace(target_url.rstrip("/"), "").replace("https://samedaydiplomas.com", "")
    print(f"  {r['clicks']:>6,.0f} clicks | {r['impressions']:>8,.0f} imps | pos {r['position']:.1f} | {page}")

output = {
    "property": target_url,
    "start_date": START_DATE,
    "end_date": END_DATE,
    "totals": {
        "total_clicks": total_clicks,
        "total_impressions": total_imps,
        "overall_ctr_pct": avg_ctr,
    },
    "branded_vs_nonbranded": {
        "branded_clicks": branded_clicks,
        "branded_pct": branded_pct,
        "nonbranded_clicks": nonbranded_clicks,
        "nonbranded_pct": nonbranded_pct,
    },
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
            "page": r["keys"][0].replace("https://samedaydiplomas.com", ""),
            "clicks": r["clicks"],
            "impressions": r["impressions"],
            "ctr_pct": round(r["ctr"] * 100, 2),
            "position": round(r["position"], 1),
        }
        for r in top_pages.get("rows", [])
    ],
}

with open(r"C:\Users\jones\Claude\gsc-same-day-diplomas.json", "w") as f:
    json.dump(output, f, indent=2)
print("\n✓ Saved to gsc-same-day-diplomas.json")
