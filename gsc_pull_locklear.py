"""
Pull GSC data for Locklear Dentistry.
Traffic + visibility report: April–August, MoM and YoY.
Outputs structured JSON.
"""
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY_FILE = r"C:\Users\jones\Downloads\embertribe-content-tools-e6776250739e (1).json"
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
SITE = "https://www.lockleardentistry.com/"

credentials = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
service = build("searchconsole", "v1", credentials=credentials)

# Month windows: April 1 – August 31, for 2025 and 2026
MONTHS = {
    "2025-04": ("2025-04-01", "2025-04-30"),
    "2025-05": ("2025-05-01", "2025-05-31"),
    "2025-06": ("2025-06-01", "2025-06-30"),
    "2025-07": ("2025-07-01", "2025-07-31"),
    "2025-08": ("2025-08-01", "2025-08-31"),
    "2026-04": ("2026-04-01", "2026-04-30"),
    "2026-05": ("2026-05-01", "2026-05-31"),
    "2026-06": ("2026-06-01", "2026-06-30"),
    "2026-07": ("2026-07-01", "2026-07-31"),
    "2026-08": ("2026-08-01", "2026-08-31"),
}

def query(start, end, dimensions=None, row_limit=25000, filters=None):
    body = {"startDate": start, "endDate": end, "rowLimit": row_limit}
    if dimensions:
        body["dimensions"] = dimensions
    if filters:
        body["dimensionFilterGroups"] = filters
    return service.searchanalytics().query(siteUrl=SITE, body=body).execute()

def totals(start, end):
    """Aggregate totals for a window (no dimension => single summary row)."""
    res = query(start, end, dimensions=None)
    rows = res.get("rows", [])
    if not rows:
        return {"clicks": 0, "impressions": 0, "ctr": 0.0, "position": 0.0}
    r = rows[0]
    return {
        "clicks": r.get("clicks", 0),
        "impressions": r.get("impressions", 0),
        "ctr": round(r.get("ctr", 0) * 100, 2),
        "position": round(r.get("position", 0), 1),
    }

# ── 1. Monthly totals ──────────────────────────────────────────────
print("=== MONTHLY TOTALS ===")
monthly = {}
for label, (start, end) in MONTHS.items():
    t = totals(start, end)
    monthly[label] = t
    print(f"  {label}: {t['clicks']:>5,} clicks | {t['impressions']:>8,} imps | CTR {t['ctr']:>5}% | pos {t['position']}")

# ── 2. Top queries per period (Apr–Aug each year) ──────────────────
def top_dim(start, end, dim, limit=100):
    res = query(start, end, dimensions=[dim], row_limit=limit)
    return [
        {
            "key": r["keys"][0],
            "clicks": r["clicks"],
            "impressions": r["impressions"],
            "ctr": round(r["ctr"] * 100, 2),
            "position": round(r["position"], 1),
        }
        for r in res.get("rows", [])
    ]

print("\n=== PULLING TOP QUERIES / PAGES (Apr 1 – Aug 31, each year) ===")
periods = {
    "2025": ("2025-04-01", "2025-08-31"),
    "2026": ("2026-04-01", "2026-08-31"),
}

top_queries = {}
top_pages = {}
device_split = {}
country_split = {}
period_totals = {}
for yr, (start, end) in periods.items():
    period_totals[yr] = totals(start, end)
    top_queries[yr] = top_dim(start, end, "query", 200)
    top_pages[yr] = top_dim(start, end, "page", 200)
    device_split[yr] = top_dim(start, end, "device", 10)
    country_split[yr] = top_dim(start, end, "country", 20)
    print(f"  {yr}: {len(top_queries[yr])} queries, {len(top_pages[yr])} pages pulled")

output = {
    "property": SITE,
    "report": "Locklear Dentistry — Traffic & Visibility, April–August",
    "monthly_totals": monthly,
    "period_totals": period_totals,
    "top_queries": top_queries,
    "top_pages": top_pages,
    "device_split": device_split,
    "country_split": country_split,
}

with open(r"C:\Users\jones\Claude\gsc_locklear.json", "w") as f:
    json.dump(output, f, indent=2)
print("\n✓ Saved to gsc_locklear.json")
