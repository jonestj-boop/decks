"""
CEU Matrix — GSC + GA4 Data Pull
Pulls CDCA query performance, page-level data, and organic landing page sessions
for the Ohio CDCA drop analysis.
"""

import json
import os
from datetime import date, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange, Dimension, Metric, RunReportRequest, FilterExpression,
    Filter
)

# ── Config ────────────────────────────────────────────────────────────────────
KEY_FILE    = "/Users/melissacedeno/Desktop/Claude/embertribe-decks/embertribe-content-tools-e6776250739e.json"
GSC_SITE    = "sc-domain:ceumatrix.com"   # try domain property first
GA4_PROP    = None                         # will try to discover below

SCOPES_GSC  = ["https://www.googleapis.com/auth/webmasters.readonly"]
SCOPES_GA4  = ["https://www.googleapis.com/auth/analytics.readonly"]

# Date windows
TODAY        = date.today()                          # 2026-04-22
LAST7_END    = str(TODAY - timedelta(days=1))        # 2026-04-21
LAST7_START  = str(TODAY - timedelta(days=7))        # 2026-04-15
PREV28_END   = str(TODAY - timedelta(days=8))        # 2026-04-14
PREV28_START = str(TODAY - timedelta(days=35))       # 2026-03-18
MARCH_START  = "2026-03-01"
MARCH_END    = "2026-03-31"

output = {}

# ── GSC ──────────────────────────────────────────────────────────────────────
print("=== GOOGLE SEARCH CONSOLE ===\n")

try:
    gsc_creds = service_account.Credentials.from_service_account_file(
        KEY_FILE, scopes=SCOPES_GSC
    )
    gsc = build("searchconsole", "v1", credentials=gsc_creds)

    # --- 0. List available sites ---
    print("0. Available GSC sites for this service account...")
    sites_resp = gsc.sites().list().execute()
    output["gsc_sites"] = sites_resp
    for s in sites_resp.get("siteEntry", []):
        print(f"   {s['siteUrl']}  permission:{s['permissionLevel']}")

    # Try URL-prefix property if domain property fails
    if not sites_resp.get("siteEntry"):
        print("   (no sites found — service account may need to be added to the GSC property)")

    # --- 1. CDCA queries — last 7 days ---
    print("1. CDCA queries (last 7 days)...")
    r = gsc.searchanalytics().query(
        siteUrl=GSC_SITE,
        body={
            "startDate": LAST7_START,
            "endDate":   LAST7_END,
            "dimensions": ["query"],
            "dimensionFilterGroups": [{
                "filters": [{
                    "dimension": "query",
                    "operator":  "contains",
                    "expression": "cdca"
                }]
            }],
            "rowLimit": 50
        }
    ).execute()

    cdca_last7 = r.get("rows", [])
    output["cdca_queries_last7"] = cdca_last7
    print(f"   Found {len(cdca_last7)} rows")
    for row in cdca_last7[:10]:
        print(f"   {row['keys'][0]:<45} clicks:{row['clicks']:>4}  impr:{row['impressions']:>6}  pos:{row['position']:.1f}")

    # --- 2. CDCA queries — March baseline ---
    print("\n2. CDCA queries (March 2026 baseline)...")
    r2 = gsc.searchanalytics().query(
        siteUrl=GSC_SITE,
        body={
            "startDate": MARCH_START,
            "endDate":   MARCH_END,
            "dimensions": ["query"],
            "dimensionFilterGroups": [{
                "filters": [{
                    "dimension": "query",
                    "operator":  "contains",
                    "expression": "cdca"
                }]
            }],
            "rowLimit": 50
        }
    ).execute()

    cdca_march = r2.get("rows", [])
    output["cdca_queries_march"] = cdca_march
    print(f"   Found {len(cdca_march)} rows")
    for row in cdca_march[:10]:
        print(f"   {row['keys'][0]:<45} clicks:{row['clicks']:>4}  impr:{row['impressions']:>6}  pos:{row['position']:.1f}")

    # --- 3. Ohio CDCA pages — last 7 days ---
    print("\n3. Ohio CDCA pages — last 7 days (by URL)...")
    r3 = gsc.searchanalytics().query(
        siteUrl=GSC_SITE,
        body={
            "startDate": LAST7_START,
            "endDate":   LAST7_END,
            "dimensions": ["page"],
            "dimensionFilterGroups": [{
                "filters": [{
                    "dimension": "page",
                    "operator":  "contains",
                    "expression": "cdca"
                }]
            }],
            "rowLimit": 25
        }
    ).execute()

    cdca_pages_last7 = r3.get("rows", [])
    output["cdca_pages_last7"] = cdca_pages_last7
    print(f"   Found {len(cdca_pages_last7)} rows")
    for row in cdca_pages_last7:
        print(f"   {row['keys'][0]:<65} clicks:{row['clicks']:>4}  impr:{row['impressions']:>6}  pos:{row['position']:.1f}")

    # --- 4. Ohio CDCA pages — March baseline ---
    print("\n4. Ohio CDCA pages — March 2026 baseline...")
    r4 = gsc.searchanalytics().query(
        siteUrl=GSC_SITE,
        body={
            "startDate": MARCH_START,
            "endDate":   MARCH_END,
            "dimensions": ["page"],
            "dimensionFilterGroups": [{
                "filters": [{
                    "dimension": "page",
                    "operator":  "contains",
                    "expression": "cdca"
                }]
            }],
            "rowLimit": 25
        }
    ).execute()

    cdca_pages_march = r4.get("rows", [])
    output["cdca_pages_march"] = cdca_pages_march
    print(f"   Found {len(cdca_pages_march)} rows")
    for row in cdca_pages_march:
        print(f"   {row['keys'][0]:<65} clicks:{row['clicks']:>4}  impr:{row['impressions']:>6}  pos:{row['position']:.1f}")

    # --- 5. All Ohio pages — last 7 days ---
    print("\n5. All Ohio pages — last 7 days...")
    r5 = gsc.searchanalytics().query(
        siteUrl=GSC_SITE,
        body={
            "startDate": LAST7_START,
            "endDate":   LAST7_END,
            "dimensions": ["page"],
            "dimensionFilterGroups": [{
                "filters": [{
                    "dimension": "page",
                    "operator":  "contains",
                    "expression": "ohio"
                }]
            }],
            "rowLimit": 25
        }
    ).execute()

    ohio_pages_last7 = r5.get("rows", [])
    output["ohio_pages_last7"] = ohio_pages_last7
    print(f"   Found {len(ohio_pages_last7)} rows")
    for row in ohio_pages_last7:
        print(f"   {row['keys'][0]:<65} clicks:{row['clicks']:>4}  impr:{row['impressions']:>6}  pos:{row['position']:.1f}")

    # --- 6. Top overall queries — last 7 days ---
    print("\n6. Top 20 queries overall (last 7 days)...")
    r6 = gsc.searchanalytics().query(
        siteUrl=GSC_SITE,
        body={
            "startDate": LAST7_START,
            "endDate":   LAST7_END,
            "dimensions": ["query"],
            "rowLimit": 20
        }
    ).execute()

    top_queries = r6.get("rows", [])
    output["top_queries_last7"] = top_queries
    for row in top_queries:
        print(f"   {row['keys'][0]:<45} clicks:{row['clicks']:>4}  impr:{row['impressions']:>6}  pos:{row['position']:.1f}")

    # --- 7. List all available GSC properties ---
    print("\n7. Available GSC properties for this service account...")
    sites = gsc.sites().list().execute()
    output["gsc_sites"] = sites
    for s in sites.get("siteEntry", []):
        print(f"   {s['siteUrl']}  permissionLevel:{s['permissionLevel']}")

    print("\n✓ GSC pull complete")

except Exception as e:
    print(f"✗ GSC error: {e}")
    output["gsc_error"] = str(e)

# ── GA4 ──────────────────────────────────────────────────────────────────────
print("\n=== GOOGLE ANALYTICS 4 ===\n")

try:
    ga4_creds = service_account.Credentials.from_service_account_file(
        KEY_FILE, scopes=SCOPES_GA4
    )

    # Try to discover the GA4 property ID via Admin API
    admin = build("analyticsadmin", "v1alpha", credentials=ga4_creds)
    accts = admin.accountSummaries().list().execute()
    output["ga4_accounts"] = accts

    for acct in accts.get("accountSummaries", []):
        print(f"Account: {acct['displayName']} ({acct['account']})")
        for prop in acct.get("propertySummaries", []):
            print(f"  Property: {prop['displayName']} — {prop['property']}")
            if "ceu" in prop["displayName"].lower() or "ceumatrix" in prop["displayName"].lower():
                GA4_PROP = prop["property"].replace("properties/", "")
                print(f"  *** Found CEU Matrix GA4 property: {GA4_PROP} ***")

    if GA4_PROP:
        client = BetaAnalyticsDataClient(credentials=ga4_creds)

        # Organic landing pages — Ohio CDCA — last 7 days
        print(f"\nPulling GA4 organic landing pages for /ohio-cdca* (last 7 days)...")
        req = RunReportRequest(
            property=f"properties/{GA4_PROP}",
            date_ranges=[DateRange(start_date=LAST7_START, end_date=LAST7_END)],
            dimensions=[Dimension(name="landingPage"), Dimension(name="sessionDefaultChannelGroup")],
            metrics=[Metric(name="sessions"), Metric(name="bounceRate")],
            dimension_filter=FilterExpression(
                filter=Filter(
                    field_name="landingPage",
                    string_filter=Filter.StringFilter(
                        match_type=Filter.StringFilter.MatchType.CONTAINS,
                        value="cdca"
                    )
                )
            )
        )
        resp = client.run_report(req)
        ga4_cdca = []
        for row in resp.rows:
            ga4_cdca.append({
                "page":    row.dimension_values[0].value,
                "channel": row.dimension_values[1].value,
                "sessions": row.metric_values[0].value,
                "bounce":   row.metric_values[1].value,
            })
        output["ga4_cdca_last7"] = ga4_cdca
        print(f"   Found {len(ga4_cdca)} rows")
        for r in ga4_cdca:
            print(f"   {r['page']:<60} channel:{r['channel']:<20} sessions:{r['sessions']}")

    print("\n✓ GA4 pull complete")

except Exception as e:
    print(f"✗ GA4 error: {e}")
    output["ga4_error"] = str(e)

# ── Save output ───────────────────────────────────────────────────────────────
out_path = "/Users/melissacedeno/Desktop/Claude/embertribe-decks/reference files/ceu-matrix/gsc-ga4-cdca-pull.json"
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"\n✓ Full output saved to: {out_path}")
