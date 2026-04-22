"""
CEU Matrix — GSC Data Pull
Tries multiple property formats and pulls CDCA query performance data
"""

import json, os
from datetime import date, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY_FILE = "/Users/melissacedeno/Desktop/Claude/embertribe-decks/embertribe-content-tools-e6776250739e.json"
SCOPES   = ["https://www.googleapis.com/auth/webmasters.readonly"]

TODAY        = date.today()
LAST7_END    = str(TODAY - timedelta(days=1))
LAST7_START  = str(TODAY - timedelta(days=7))
MARCH_START  = "2026-03-01"
MARCH_END    = "2026-03-31"

creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
gsc   = build("searchconsole", "v1", credentials=creds)

output = {}

# ── 1. List all available GSC sites ──────────────────────────────────────────
print("=== 1. All GSC sites accessible to this service account ===")
try:
    resp = gsc.sites().list().execute()
    sites = resp.get("siteEntry", [])
    output["available_sites"] = sites
    if sites:
        for s in sites:
            print(f"  {s['siteUrl']}  permission:{s['permissionLevel']}")
    else:
        print("  No sites found — service account not added to any GSC property yet.")
        print(f"\n  To grant access, go to:")
        print(f"  GSC → Settings → Users & permissions → Add user")
        print(f"  Email: embertribe-content-tools@embertribe-content-tools.iam.gserviceaccount.com")
        print(f"  Permission: Full (to enable data pulls)")
except Exception as e:
    print(f"  Error listing sites: {e}")

# ── 2. Try multiple property formats ─────────────────────────────────────────
print("\n=== 2. Trying property URL formats ===")
candidates = [
    "sc-domain:ceumatrix.com",
    "https://ceumatrix.com/",
    "http://ceumatrix.com/",
    "https://www.ceumatrix.com/",
]

working_site = None
for url in candidates:
    try:
        test = gsc.searchanalytics().query(
            siteUrl=url,
            body={"startDate": LAST7_START, "endDate": LAST7_END,
                  "dimensions": ["query"], "rowLimit": 1}
        ).execute()
        print(f"  ✓ WORKS: {url}")
        working_site = url
    except Exception as e:
        err = str(e)[:80]
        print(f"  ✗ {url}: {err}")

if working_site:
    print(f"\n✓ Using: {working_site}")

    # ── 3. CDCA queries last 7 days ───────────────────────────────────────────
    print("\n=== 3. CDCA queries — last 7 days ===")
    r = gsc.searchanalytics().query(
        siteUrl=working_site,
        body={
            "startDate": LAST7_START, "endDate": LAST7_END,
            "dimensions": ["query"],
            "dimensionFilterGroups": [{"filters": [
                {"dimension": "query", "operator": "contains", "expression": "cdca"}
            ]}],
            "rowLimit": 50
        }
    ).execute()
    rows = r.get("rows", [])
    output["cdca_queries_last7"] = rows
    print(f"  {'Query':<50} {'Clicks':>7} {'Impr':>7} {'CTR':>6} {'Pos':>6}")
    print("  " + "-"*80)
    for row in rows:
        print(f"  {row['keys'][0]:<50} {row['clicks']:>7.0f} {row['impressions']:>7.0f} "
              f"{row['ctr']*100:>5.1f}% {row['position']:>6.1f}")

    # ── 4. CDCA queries March baseline ───────────────────────────────────────
    print("\n=== 4. CDCA queries — March 2026 baseline ===")
    r2 = gsc.searchanalytics().query(
        siteUrl=working_site,
        body={
            "startDate": MARCH_START, "endDate": MARCH_END,
            "dimensions": ["query"],
            "dimensionFilterGroups": [{"filters": [
                {"dimension": "query", "operator": "contains", "expression": "cdca"}
            ]}],
            "rowLimit": 50
        }
    ).execute()
    rows2 = r2.get("rows", [])
    output["cdca_queries_march"] = rows2
    print(f"  {'Query':<50} {'Clicks':>7} {'Impr':>7} {'CTR':>6} {'Pos':>6}")
    print("  " + "-"*80)
    for row in rows2:
        print(f"  {row['keys'][0]:<50} {row['clicks']:>7.0f} {row['impressions']:>7.0f} "
              f"{row['ctr']*100:>5.1f}% {row['position']:>6.1f}")

    # ── 5. Ohio pages last 7d ─────────────────────────────────────────────────
    print("\n=== 5. Ohio pages — last 7 days (by page) ===")
    r3 = gsc.searchanalytics().query(
        siteUrl=working_site,
        body={
            "startDate": LAST7_START, "endDate": LAST7_END,
            "dimensions": ["page"],
            "dimensionFilterGroups": [{"filters": [
                {"dimension": "page", "operator": "contains", "expression": "ohio"}
            ]}],
            "rowLimit": 25
        }
    ).execute()
    rows3 = r3.get("rows", [])
    output["ohio_pages_last7"] = rows3
    for row in rows3:
        print(f"  {row['keys'][0]:<70} pos:{row['position']:>6.1f}  clicks:{row['clicks']:>4.0f}")

    # ── 6. /course/ vs /product/ CDCA — position comparison ──────────────────
    print("\n=== 6. /course/ vs /product/ CDCA pages — position + clicks ===")
    r4 = gsc.searchanalytics().query(
        siteUrl=working_site,
        body={
            "startDate": LAST7_START, "endDate": LAST7_END,
            "dimensions": ["page"],
            "dimensionFilterGroups": [{"filters": [
                {"dimension": "page", "operator": "contains", "expression": "cdca"}
            ]}],
            "rowLimit": 25
        }
    ).execute()
    rows4 = r4.get("rows", [])
    output["cdca_pages_gsc_last7"] = rows4
    print(f"  {'Page':<65} {'Clicks':>7} {'Impr':>7} {'Pos':>6}")
    print("  " + "-"*90)
    for row in rows4:
        print(f"  {row['keys'][0]:<65} {row['clicks']:>7.0f} {row['impressions']:>7.0f} {row['position']:>6.1f}")

    # ── 7. Same pages in March for comparison ────────────────────────────────
    print("\n=== 7. /course/ vs /product/ CDCA pages — March baseline positions ===")
    r5 = gsc.searchanalytics().query(
        siteUrl=working_site,
        body={
            "startDate": MARCH_START, "endDate": MARCH_END,
            "dimensions": ["page"],
            "dimensionFilterGroups": [{"filters": [
                {"dimension": "page", "operator": "contains", "expression": "cdca"}
            ]}],
            "rowLimit": 25
        }
    ).execute()
    rows5 = r5.get("rows", [])
    output["cdca_pages_gsc_march"] = rows5
    for row in rows5:
        print(f"  {row['keys'][0]:<65} {row['clicks']:>7.0f} {row['impressions']:>7.0f} {row['position']:>6.1f}")

    # ── 8. Top queries + average position, last 7d ───────────────────────────
    print("\n=== 8. Top queries — last 7 days (all) ===")
    r6 = gsc.searchanalytics().query(
        siteUrl=working_site,
        body={
            "startDate": LAST7_START, "endDate": LAST7_END,
            "dimensions": ["query"],
            "rowLimit": 25
        }
    ).execute()
    rows6 = r6.get("rows", [])
    output["top_queries_last7"] = rows6
    for row in rows6:
        print(f"  {row['keys'][0]:<50} clicks:{row['clicks']:>4.0f}  pos:{row['position']:>6.1f}")

else:
    print("\n✗ No working GSC property found for this service account.")
    print("  Next step: Add embertribe-content-tools@embertribe-content-tools.iam.gserviceaccount.com")
    print("  to the ceumatrix.com GSC property with Full access.")

# ── Save ──────────────────────────────────────────────────────────────────────
out_path = "/Users/melissacedeno/Desktop/Claude/embertribe-decks/reference files/ceu-matrix/gsc-cdca-pull.json"
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"\n✓ Output saved to: {out_path}")
