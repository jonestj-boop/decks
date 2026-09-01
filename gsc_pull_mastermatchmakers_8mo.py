"""
Pull 8 months of GSC data for mastermatchmakers.com and build a
month-over-month traffic comparison. Outputs gsc-master-matchmakers-8mo.json.
"""
import json, calendar
from datetime import date
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY_FILE = r"C:\Users\jones\Downloads\embertribe-content-tools-e6776250739e (1).json"
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
START_DATE = "2026-01-01"
END_DATE   = "2026-08-31"

credentials = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
service = build("searchconsole", "v1", credentials=credentials)

# --- Find the property ---
sites = service.sites().list().execute()
prop = None
for s in sites.get("siteEntry", []):
    if "mastermatchmakers" in s["siteUrl"].lower():
        prop = s["siteUrl"]
        break
if not prop:
    print("Available:", [s["siteUrl"] for s in sites.get("siteEntry", [])])
    raise SystemExit("mastermatchmakers property not found")
print(f"Using property: {prop}")


def q(dimensions, row_limit=1000, start=START_DATE, end=END_DATE, filters=None):
    body = {"startDate": start, "endDate": end, "dimensions": dimensions, "rowLimit": row_limit}
    if filters:
        body["dimensionFilterGroups"] = filters
    return service.searchanalytics().query(siteUrl=prop, body=body).execute()


# --- Daily rows -> monthly rollup ---
daily = q(["date"], row_limit=500)
months = {}
for r in daily.get("rows", []):
    m = r["keys"][0][:7]
    d = months.setdefault(m, {"clicks": 0, "impressions": 0, "pos_sum": 0.0, "days": 0})
    d["clicks"] += r["clicks"]
    d["impressions"] += r["impressions"]
    d["pos_sum"] += r["position"]
    d["days"] += 1

by_month = {}
for m in sorted(months):
    d = months[m]
    ctr = round(d["clicks"] / d["impressions"] * 100, 2) if d["impressions"] else 0
    avg_pos = round(d["pos_sum"] / d["days"], 1) if d["days"] else 0
    by_month[m] = {
        "clicks": d["clicks"],
        "impressions": d["impressions"],
        "ctr_pct": ctr,
        "avg_position": avg_pos,
        "days": d["days"],
    }

total_clicks = sum(months[m]["clicks"] for m in months)
total_imps = sum(months[m]["impressions"] for m in months)
overall_ctr = round(total_clicks / total_imps * 100, 2) if total_imps else 0

# --- Branded vs non-branded (last full 8 months) ---
allq = q(["query"], row_limit=25000)
brand_terms = ["master matchmaker", "mastermatchmaker", "joann ward", "joann",
               "steven ward", "steven b ward", "steve ward", "stevenbward"]
branded = sum(r["clicks"] for r in allq.get("rows", [])
              if any(b in r["keys"][0].lower() for b in brand_terms))
nonbranded = total_clicks - branded

# --- Top queries / pages over the window ---
top_queries = [
    {"query": r["keys"][0], "clicks": r["clicks"], "impressions": r["impressions"],
     "ctr_pct": round(r["ctr"] * 100, 2), "position": round(r["position"], 1)}
    for r in q(["query"], row_limit=30).get("rows", [])
]
top_pages = [
    {"page": r["keys"][0].replace(prop.rstrip("/"), ""), "clicks": r["clicks"],
     "impressions": r["impressions"], "ctr_pct": round(r["ctr"] * 100, 2),
     "position": round(r["position"], 1)}
    for r in q(["page"], row_limit=30).get("rows", [])
]

# --- First month vs last month deltas ---
mkeys = sorted(by_month)
first_m, last_m = mkeys[0], mkeys[-1]


def pct(a, b):
    return round((b - a) / a * 100, 1) if a else None


comparison = {
    "first_month": first_m,
    "last_month": last_m,
    "clicks": {"start": by_month[first_m]["clicks"], "end": by_month[last_m]["clicks"],
               "change_pct": pct(by_month[first_m]["clicks"], by_month[last_m]["clicks"])},
    "impressions": {"start": by_month[first_m]["impressions"], "end": by_month[last_m]["impressions"],
                    "change_pct": pct(by_month[first_m]["impressions"], by_month[last_m]["impressions"])},
    "avg_position": {"start": by_month[first_m]["avg_position"], "end": by_month[last_m]["avg_position"]},
}

output = {
    "property": prop,
    "start_date": START_DATE,
    "end_date": END_DATE,
    "totals": {
        "total_clicks": total_clicks,
        "total_impressions": total_imps,
        "overall_ctr_pct": overall_ctr,
        "branded_clicks": branded,
        "nonbranded_clicks": nonbranded,
        "months_covered": len(mkeys),
    },
    "by_month": by_month,
    "month_over_month_comparison": comparison,
    "top_queries": top_queries,
    "top_pages": top_pages,
}

with open(r"C:\Users\jones\Claude\gsc-master-matchmakers-8mo.json", "w") as f:
    json.dump(output, f, indent=2)

# --- Console summary ---
print(f"\n=== MASTER MATCHMAKERS — 8-MONTH TRAFFIC ({START_DATE} to {END_DATE}) ===")
print(f"Total clicks: {total_clicks:,} | Total impressions: {total_imps:,} | CTR: {overall_ctr}%")
print(f"Branded: {branded:,} | Non-branded: {nonbranded:,}\n")
print(f"{'Month':<9}{'Clicks':>9}{'Impr':>11}{'CTR%':>8}{'AvgPos':>9}")
for m in mkeys:
    b = by_month[m]
    print(f"{m:<9}{b['clicks']:>9,}{b['impressions']:>11,}{b['ctr_pct']:>8}{b['avg_position']:>9}")
print(f"\nMoM ({first_m} -> {last_m}): clicks {comparison['clicks']['change_pct']}%, "
      f"impressions {comparison['impressions']['change_pct']}%, "
      f"position {comparison['avg_position']['start']} -> {comparison['avg_position']['end']}")
print("\nSaved gsc-master-matchmakers-8mo.json")
