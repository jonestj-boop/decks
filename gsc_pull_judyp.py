"""
Pull GSC data for judypapparel.com using service account credentials.
Outputs structured JSON for use in the JudyP Apparel growth roadmap deck.
"""
import json
from datetime import date, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY_FILE = r"C:\Users\jones\Downloads\embertribe-content-tools-e6776250739e (1).json"
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]

credentials = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
service = build("searchconsole", "v1", credentials=credentials)

SITE_URL = "sc-domain:judypapparel.com"
START_DATE = "2025-11-01"
END_DATE   = "2026-05-21"

def query_gsc(dimensions, row_limit=1000, filters=None, start=START_DATE, end=END_DATE):
    body = {
        "startDate": start,
        "endDate": end,
        "dimensions": dimensions,
        "rowLimit": row_limit,
    }
    if filters:
        body["dimensionFilterGroups"] = filters
    return service.searchanalytics().query(siteUrl=SITE_URL, body=body).execute()

print(f"Pulling GSC data for {SITE_URL}...")
print(f"Date range: {START_DATE} to {END_DATE}\n")

# 1. Overall totals by date
overall = query_gsc(["date"], row_limit=250)
rows = overall.get("rows", [])
total_clicks = sum(r["clicks"] for r in rows)
total_imps   = sum(r["impressions"] for r in rows)
days = len(rows)
avg_ctr = round(total_clicks / total_imps * 100, 2) if total_imps else 0

# Avg position (weighted)
total_pos_weight = sum(r["impressions"] * r["position"] for r in rows)
avg_position = round(total_pos_weight / total_imps, 1) if total_imps else 0

print(f"=== OVERALL TOTALS ===")
print(f"  Date rows:          {days}")
print(f"  Total clicks:       {total_clicks:,}")
print(f"  Total impressions:  {total_imps:,}")
print(f"  Overall CTR:        {avg_ctr}%")
print(f"  Avg position:       {avg_position}")

# 2. By month
by_month_clicks = {}
by_month_imps = {}
for row in rows:
    month = row["keys"][0][:7]
    by_month_clicks[month] = by_month_clicks.get(month, 0) + row["clicks"]
    by_month_imps[month] = by_month_imps.get(month, 0) + row["impressions"]

print("\n=== CLICKS BY MONTH ===")
for m in sorted(by_month_clicks):
    print(f"  {m}: {by_month_clicks[m]:,} clicks  |  {by_month_imps[m]:,} imps")

# 3. Top queries (by clicks)
top_queries = query_gsc(["query"], row_limit=500)
qrows = sorted(top_queries.get("rows", []), key=lambda x: x["clicks"], reverse=True)

print("\n=== TOP 30 QUERIES (by clicks) ===")
for r in qrows[:30]:
    print(f"  {r['clicks']:>6,} clicks | {r['impressions']:>8,} imps | pos {r['position']:.1f} | {r['keys'][0]}")

# 4. Striking-distance queries (pos 11-30, sorted by impressions)
striking = [r for r in top_queries.get("rows", []) if 11 <= r["position"] <= 30]
striking.sort(key=lambda x: x["impressions"], reverse=True)
print(f"\n=== STRIKING DISTANCE (pos 11-30): {len(striking)} keywords ===")
for r in striking[:20]:
    print(f"  pos {r['position']:.0f} | {r['clicks']:>5,} clicks | {r['impressions']:>8,} imps | {r['keys'][0]}")

# 5. Top pages (by clicks)
top_pages = query_gsc(["page"], row_limit=100)
prows = sorted(top_pages.get("rows", []), key=lambda x: x["clicks"], reverse=True)

print("\n=== TOP 20 PAGES (by clicks) ===")
for r in prows[:20]:
    page = r["keys"][0].replace("https://judypapparel.com", "").replace("http://judypapparel.com", "")
    if not page:
        page = "/"
    print(f"  {r['clicks']:>6,} clicks | {r['impressions']:>8,} imps | pos {r['position']:.1f} | {page}")

# 6. Branded vs non-branded
branded_terms = ["judy", "judyp", "judy p"]
branded_clicks = sum(r["clicks"] for r in qrows if any(b in r["keys"][0].lower() for b in branded_terms))
nonbrand_clicks = total_clicks - branded_clicks
print(f"\n=== BRANDED vs NON-BRANDED ===")
print(f"  Branded:     {branded_clicks:,} clicks")
print(f"  Non-branded: {nonbrand_clicks:,} clicks")

# 7. Smart casual cluster
smart_casual = [r for r in qrows if "smart casual" in r["keys"][0].lower()]
smart_casual.sort(key=lambda x: x["clicks"], reverse=True)
sc_clicks = sum(r["clicks"] for r in smart_casual)
print(f"\n=== SMART CASUAL CLUSTER ===")
print(f"  Total: {sc_clicks:,} clicks across {len(smart_casual)} queries")
for r in smart_casual[:10]:
    print(f"  {r['clicks']:>5,} clicks | pos {r['position']:.1f} | {r['keys'][0]}")

# 8. Travel cluster
travel = [r for r in qrows if any(t in r["keys"][0].lower() for t in ["travel", "wrinkle", "pack", "cruise"])]
travel.sort(key=lambda x: x["clicks"], reverse=True)
travel_clicks = sum(r["clicks"] for r in travel)
print(f"\n=== TRAVEL / WRINKLE CLUSTER ===")
print(f"  Total: {travel_clicks:,} clicks across {len(travel)} queries")
for r in travel[:10]:
    print(f"  {r['clicks']:>5,} clicks | pos {r['position']:.1f} | {r['keys'][0]}")

# Save structured output
output = {
    "property": SITE_URL,
    "start_date": START_DATE,
    "end_date": END_DATE,
    "totals": {
        "total_clicks": total_clicks,
        "total_impressions": total_imps,
        "avg_ctr_pct": avg_ctr,
        "avg_position": avg_position,
        "days_of_data": days,
    },
    "by_month": {
        m: {"clicks": by_month_clicks[m], "impressions": by_month_imps[m]}
        for m in sorted(by_month_clicks)
    },
    "top_queries": [
        {
            "query": r["keys"][0],
            "clicks": r["clicks"],
            "impressions": r["impressions"],
            "ctr_pct": round(r["ctr"] * 100, 2),
            "position": round(r["position"], 1),
        }
        for r in qrows[:100]
    ],
    "striking_distance": [
        {
            "query": r["keys"][0],
            "clicks": r["clicks"],
            "impressions": r["impressions"],
            "ctr_pct": round(r["ctr"] * 100, 2),
            "position": round(r["position"], 1),
        }
        for r in striking[:50]
    ],
    "top_pages": [
        {
            "page": r["keys"][0].replace("https://judypapparel.com", "").replace("http://judypapparel.com", "") or "/",
            "clicks": r["clicks"],
            "impressions": r["impressions"],
            "ctr_pct": round(r["ctr"] * 100, 2),
            "position": round(r["position"], 1),
        }
        for r in prows[:30]
    ],
    "clusters": {
        "smart_casual": {
            "total_clicks": sc_clicks,
            "keyword_count": len(smart_casual),
            "queries": [
                {"query": r["keys"][0], "clicks": r["clicks"], "impressions": r["impressions"], "position": round(r["position"], 1)}
                for r in smart_casual
            ],
        },
        "travel_wrinkle": {
            "total_clicks": travel_clicks,
            "keyword_count": len(travel),
        },
    },
    "branded_clicks": branded_clicks,
    "nonbranded_clicks": nonbrand_clicks,
    "striking_distance_count": len(striking),
}

out_path = r"C:\Users\jones\Claude\gsc-judyp-apparel.json"
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to gsc-judyp-apparel.json")
