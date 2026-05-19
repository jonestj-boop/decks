"""
Retreat (joinretreat.app) — QC Data Pull
Cross-references claims in the growth-roadmap deck against live GSC + GA4 data.
"""

import json, os
from datetime import date, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY_FILE = "/Users/melissacedeno/Desktop/Claude/embertribe-decks/embertribe-content-tools-e6776250739e.json"
GSC_SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
GA4_SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]

TODAY      = date.today()
END_DATE   = str(TODAY - timedelta(days=1))
START_DATE = str(TODAY - timedelta(days=28))  # last 28 days for stable averages

output = {}

# ── GSC Setup ─────────────────────────────────────────────────────────────────
gsc_creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=GSC_SCOPES)
gsc = build("searchconsole", "v1", credentials=gsc_creds)

# ── 1. List all accessible GSC sites ─────────────────────────────────────────
print("=== 1. All GSC sites accessible to service account ===")
try:
    resp = gsc.sites().list().execute()
    sites = resp.get("siteEntry", [])
    output["available_gsc_sites"] = sites
    for s in sites:
        print(f"  {s['siteUrl']}  ({s['permissionLevel']})")
    if not sites:
        print("  No sites found.")
except Exception as e:
    print(f"  Error: {e}")

# ── 2. Try Retreat property formats ───────────────────────────────────────────
print("\n=== 2. Probing joinretreat.app property formats ===")
candidates = [
    "sc-domain:joinretreat.app",
    "https://joinretreat.app/",
    "http://joinretreat.app/",
    "https://www.joinretreat.app/",
]
working_site = None
for url in candidates:
    try:
        gsc.searchanalytics().query(
            siteUrl=url,
            body={"startDate": END_DATE, "endDate": END_DATE,
                  "dimensions": ["query"], "rowLimit": 1}
        ).execute()
        print(f"  WORKS: {url}")
        working_site = url
        break
    except Exception as e:
        print(f"  FAIL  {url}: {str(e)[:80]}")

if working_site:
    # ── 3. Total clicks + impressions last 28 days ────────────────────────────
    print(f"\n=== 3. Site-wide totals — last 28 days ({START_DATE} to {END_DATE}) ===")
    r = gsc.searchanalytics().query(
        siteUrl=working_site,
        body={"startDate": START_DATE, "endDate": END_DATE,
              "dimensions": ["date"], "rowLimit": 90}
    ).execute()
    rows = r.get("rows", [])
    total_clicks = sum(row["clicks"] for row in rows)
    total_impr   = sum(row["impressions"] for row in rows)
    monthly_est  = round(total_clicks * 30 / 28)
    output["sitewide_28d"] = {"clicks": total_clicks, "impressions": total_impr,
                               "monthly_est": monthly_est, "days": len(rows)}
    print(f"  Total clicks (28d): {total_clicks}")
    print(f"  Total impressions (28d): {total_impr}")
    print(f"  Estimated monthly organic traffic: ~{monthly_est}")
    print(f"  Report claims: 9 monthly visits")

    # ── 4. Ranking keywords (queries with >=1 click) ──────────────────────────
    print(f"\n=== 4. Queries with clicks — last 28 days ===")
    r2 = gsc.searchanalytics().query(
        siteUrl=working_site,
        body={"startDate": START_DATE, "endDate": END_DATE,
              "dimensions": ["query"], "rowLimit": 100}
    ).execute()
    rows2 = r2.get("rows", [])
    queries_with_clicks = [row for row in rows2 if row["clicks"] > 0]
    queries_with_impr   = [row for row in rows2 if row["impressions"] > 0]
    output["queries"] = rows2
    print(f"  Queries with >=1 click: {len(queries_with_clicks)}")
    print(f"  Queries with impressions: {len(queries_with_impr)}")
    print(f"  Report claims: 2 ranking keywords")
    print(f"\n  Top 20 queries by clicks:")
    print(f"  {'Query':<45} {'Clicks':>7} {'Impr':>7} {'CTR':>6} {'Pos':>6}")
    print("  " + "-"*75)
    for row in sorted(rows2, key=lambda x: x["clicks"], reverse=True)[:20]:
        print(f"  {row['keys'][0]:<45} {row['clicks']:>7.0f} {row['impressions']:>7.0f} "
              f"{row['ctr']*100:>5.1f}% {row['position']:>6.1f}")

    # ── 5. Pages with traffic ─────────────────────────────────────────────────
    print(f"\n=== 5. Pages with clicks — last 28 days ===")
    r3 = gsc.searchanalytics().query(
        siteUrl=working_site,
        body={"startDate": START_DATE, "endDate": END_DATE,
              "dimensions": ["page"], "rowLimit": 100}
    ).execute()
    rows3 = r3.get("rows", [])
    pages_with_clicks = [row for row in rows3 if row["clicks"] > 0]
    output["pages"] = rows3
    print(f"  Pages with >=1 click: {len(pages_with_clicks)}")
    print(f"  Report claims: 1 page (homepage only)")
    for row in sorted(rows3, key=lambda x: x["clicks"], reverse=True)[:15]:
        print(f"  {row['keys'][0]:<70} clicks:{row['clicks']:>4.0f}  pos:{row['position']:>6.1f}")

    # ── 6. Specific keyword checks ────────────────────────────────────────────
    print(f"\n=== 6. Specific keyword verification ===")
    for kw in ["retreat app", "retreat software"]:
        match = next((r for r in rows2 if r["keys"][0] == kw), None)
        if match:
            print(f"  '{kw}': pos {match['position']:.1f}, clicks {match['clicks']}, impr {match['impressions']}")
        else:
            found = [r for r in rows2 if kw in r["keys"][0]]
            if found:
                print(f"  '{kw}': not exact match, closest: {found[0]['keys'][0]} pos {found[0]['position']:.1f}")
            else:
                print(f"  '{kw}': not found in GSC data (no impressions in last 28 days)")
    print(f"  Report claims: 'retreat app' at pos #2, 'retreat software' at pos #66")

else:
    print("\n  joinretreat.app not found in this service account's GSC access.")
    print("  Cannot verify traffic claims from GSC.")

# ── 7. GA4 — list accessible properties ──────────────────────────────────────
print("\n=== 7. GA4 — checking accessible properties ===")
try:
    from google.analytics.admin_v1alpha import AnalyticsAdminServiceClient
    from google.oauth2 import service_account as sa

    ga_creds = sa.Credentials.from_service_account_file(KEY_FILE, scopes=GA4_SCOPES)
    admin_client = AnalyticsAdminServiceClient(credentials=ga_creds)
    accounts = list(admin_client.list_account_summaries())
    output["ga4_accounts"] = []
    for acct in accounts:
        print(f"  Account: {acct.display_name}")
        for prop in acct.property_summaries:
            print(f"    Property: {prop.display_name} — {prop.property}")
            output["ga4_accounts"].append({"account": acct.display_name,
                                            "property": prop.display_name,
                                            "id": prop.property})
except ImportError:
    print("  google-analytics-admin not installed — skipping property listing")
    print("  (pip install google-analytics-admin to enable)")
except Exception as e:
    print(f"  Error: {e}")

# ── Save ──────────────────────────────────────────────────────────────────────
out_path = "/Users/melissacedeno/Desktop/Claude/embertribe-decks/reference files/join-retreat/qc-data-pull.json"
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w") as f:
    json.dump(output, f, indent=2, default=str)
print(f"\n✓ Saved to: {out_path}")
