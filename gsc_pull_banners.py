"""
Pull GSC data for banners.com using service account credentials.
Outputs structured JSON for use in the pitch deck.
"""
import json
from datetime import date, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY_FILE = r"C:\Users\jones\Downloads\embertribe-content-tools-e6776250739e (1).json"
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]

credentials = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
service = build("searchconsole", "v1", credentials=credentials)

# --- List all properties the service account can access ---
print("=== AVAILABLE PROPERTIES ===")
sites = service.sites().list().execute()
for s in sites.get("siteEntry", []):
    print(f"  {s['siteUrl']}  ({s['permissionLevel']})")

# --- Find banners.com property ---
site_entries = sites.get("siteEntry", [])
banners_url = None
for s in site_entries:
    if "banners.com" in s["siteUrl"].lower():
        banners_url = s["siteUrl"]
        break

if not banners_url:
    print("\nNo banners.com property found in service account access.")
    print("Trying common formats directly...")
    for candidate in ["https://www.banners.com/", "https://banners.com/", "sc-domain:banners.com"]:
        try:
            service.sites().get(siteUrl=candidate).execute()
            banners_url = candidate
            print(f"Found: {candidate}")
            break
        except Exception as e:
            print(f"  {candidate}: {e}")

if not banners_url:
    print("\n✗ banners.com is not accessible to this service account.")
    print("  Ask the client to add embertribe-content-tools@embertribe-content-tools.iam.gserviceaccount.com")
    print("  to their GSC property as a restricted user.")
    exit(1)

print(f"\nUsing property: {banners_url}")

# Date range: last ~6 months
START_DATE = "2025-11-01"
END_DATE   = "2026-04-30"

def query_gsc(dimensions, row_limit=1000, filters=None):
    body = {
        "startDate": START_DATE,
        "endDate": END_DATE,
        "dimensions": dimensions,
        "rowLimit": row_limit,
    }
    if filters:
        body["dimensionFilterGroups"] = filters
    return service.searchanalytics().query(siteUrl=banners_url, body=body).execute()

# ── 1. Overall totals ──────────────────────────────────────────────────────────
print("\n=== OVERALL TOTALS (6-month) ===")
overall = query_gsc(["date"], row_limit=200)
rows = overall.get("rows", [])
total_clicks = sum(r["clicks"] for r in rows)
total_imps   = sum(r["impressions"] for r in rows)
days = len(rows)
avg_clicks = round(total_clicks / max(days, 1) * 30)
avg_imps   = round(total_imps   / max(days, 1) * 30)
avg_ctr    = round(total_clicks / total_imps * 100, 2) if total_imps else 0
print(f"  Total clicks:        {total_clicks:,}")
print(f"  Total impressions:   {total_imps:,}")
print(f"  Days of data:        {days}")
print(f"  Est. monthly clicks: {avg_clicks:,}")
print(f"  Est. monthly imps:   {avg_imps:,}")
print(f"  Overall CTR:         {avg_ctr}%")

# ── 2. By month ────────────────────────────────────────────────────────────────
print("\n=== CLICKS BY MONTH ===")
by_month = {}
for row in rows:
    month = row["keys"][0][:7]
    by_month[month] = by_month.get(month, 0) + row["clicks"]
for m, c in sorted(by_month.items()):
    print(f"  {m}: {c:,} clicks")

# ── 3. Top queries ─────────────────────────────────────────────────────────────
print("\n=== TOP 50 QUERIES (by clicks) ===")
top_queries = query_gsc(["query"], row_limit=50)
for r in top_queries.get("rows", []):
    print(f"  {r['clicks']:>6,} clicks | {r['impressions']:>8,} imps | pos {r['position']:.1f} | ctr {r['ctr']*100:.1f}% | {r['keys'][0]}")

# ── 4. Top pages ───────────────────────────────────────────────────────────────
print("\n=== TOP 30 PAGES (by clicks) ===")
top_pages = query_gsc(["page"], row_limit=30)
for r in top_pages.get("rows", []):
    page = r["keys"][0].replace("https://www.banners.com", "").replace("https://banners.com", "")
    print(f"  {r['clicks']:>6,} clicks | {r['impressions']:>8,} imps | pos {r['position']:.1f} | ctr {r['ctr']*100:.1f}% | {page}")

# ── 5. High-impression / low-CTR queries (quick wins) ─────────────────────────
print("\n=== QUICK WINS (high imps, low CTR, pos 4–20) ===")
all_queries_raw = query_gsc(["query"], row_limit=500)
quick_wins = [
    r for r in all_queries_raw.get("rows", [])
    if r["impressions"] >= 500 and r["ctr"] < 0.05 and 4 <= r["position"] <= 20
]
quick_wins.sort(key=lambda x: x["impressions"], reverse=True)
for r in quick_wins[:20]:
    print(f"  pos {r['position']:.1f} | {r['impressions']:>6,} imps | ctr {r['ctr']*100:.1f}% | {r['keys'][0]}")

# ── 6. Save structured output ──────────────────────────────────────────────────
output = {
    "property": banners_url,
    "start_date": START_DATE,
    "end_date": END_DATE,
    "totals": {
        "total_clicks": total_clicks,
        "total_impressions": total_imps,
        "avg_monthly_clicks": avg_clicks,
        "avg_monthly_impressions": avg_imps,
        "overall_ctr_pct": avg_ctr,
    },
    "by_month": by_month,
    "top_pages": [
        {
            "page": r["keys"][0].replace("https://www.banners.com", "").replace("https://banners.com", "") or "/",
            "clicks": r["clicks"],
            "impressions": r["impressions"],
            "ctr_pct": round(r["ctr"] * 100, 2),
            "position": round(r["position"], 1),
        }
        for r in top_pages.get("rows", [])
    ],
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
    "quick_wins": [
        {
            "query": r["keys"][0],
            "clicks": r["clicks"],
            "impressions": r["impressions"],
            "ctr_pct": round(r["ctr"] * 100, 2),
            "position": round(r["position"], 1),
        }
        for r in quick_wins[:20]
    ],
}

out_path = r"C:\Users\jones\Claude\gsc_banners.json"
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"\n✓ Saved to {out_path}")
