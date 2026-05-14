"""
CEU Matrix — Extended GA4 Pull
Comparison: last 7 days vs. prior 28 days for Ohio CDCA pages
Also pulls site-wide organic context and /course/ vs /product/ split
"""

import json, os
from datetime import date, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange, Dimension, Metric, RunReportRequest,
    FilterExpression, Filter, OrderBy
)

KEY_FILE  = "/Users/melissacedeno/Desktop/Claude/embertribe-decks/embertribe-content-tools-e6776250739e.json"
GA4_PROP  = "276964576"
SCOPES    = ["https://www.googleapis.com/auth/analytics.readonly"]

TODAY        = date.today()
LAST7_END    = str(TODAY - timedelta(days=1))
LAST7_START  = str(TODAY - timedelta(days=7))
PREV28_END   = str(TODAY - timedelta(days=8))
PREV28_START = str(TODAY - timedelta(days=35))
MARCH_START  = "2026-03-01"
MARCH_END    = "2026-03-31"

creds  = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
client = BetaAnalyticsDataClient(credentials=creds)
output = {}

def run(label, req):
    print(f"\n── {label}")
    resp = client.run_report(req)
    rows = []
    for row in resp.rows:
        d = [v.value for v in row.dimension_values]
        m = [v.value for v in row.metric_values]
        rows.append({"dims": d, "metrics": m})
    return rows


# ── 1. CDCA organic sessions: last 7 days vs prev 28 days (side-by-side) ─────
from google.analytics.data_v1beta.types import FilterExpressionList
print("=== 1. CDCA pages — Last 7d vs Prev 28d (organic) ===")
req1 = RunReportRequest(
    property=f"properties/{GA4_PROP}",
    date_ranges=[
        DateRange(start_date=LAST7_START,  end_date=LAST7_END,   name="last_7d"),
        DateRange(start_date=PREV28_START, end_date=PREV28_END,  name="prev_28d"),
    ],
    dimensions=[Dimension(name="landingPage")],
    metrics=[Metric(name="sessions"), Metric(name="engagementRate")],
    dimension_filter=FilterExpression(
        and_group=FilterExpressionList(expressions=[
            FilterExpression(filter=Filter(
                field_name="landingPage",
                string_filter=Filter.StringFilter(
                    match_type=Filter.StringFilter.MatchType.CONTAINS,
                    value="cdca"
                )
            )),
            FilterExpression(filter=Filter(
                field_name="sessionDefaultChannelGroup",
                string_filter=Filter.StringFilter(
                    match_type=Filter.StringFilter.MatchType.EXACT,
                    value="Organic Search"
                )
            ))
        ])
    ),
    order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)]
)
resp1 = client.run_report(req1)

cdca_comparison = {}
for row in resp1.rows:
    page      = row.dimension_values[0].value
    dr        = row.dimension_values[1].value
    sessions  = int(row.metric_values[0].value)
    engage    = float(row.metric_values[1].value)
    if page not in cdca_comparison:
        cdca_comparison[page] = {}
    cdca_comparison[page][dr] = {"sessions": sessions, "engage": round(engage*100,1)}

output["cdca_organic_comparison"] = cdca_comparison
print(f"{'Page':<65} {'Last 7d':>8} {'Prev 28d':>9} {'Change':>8}")
print("-" * 95)
for page, data in sorted(cdca_comparison.items(), key=lambda x: x[1].get("last_7d",{}).get("sessions",0), reverse=True):
    l7  = data.get("last_7d",  {}).get("sessions", 0)
    p28 = data.get("prev_28d", {}).get("sessions", 0)
    # normalize prev_28d to a 7-day equivalent for fair comparison
    p28_norm = round(p28 * 7/28, 1)
    chg = f"{((l7 - p28_norm) / p28_norm * 100):+.0f}%" if p28_norm else "new"
    print(f"{page:<65} {l7:>8} {p28:>9} ({chg} vs daily avg)")


# ── 2. /course/ vs /product/ split — CDCA — last 7d ─────────────────────────
print("\n\n=== 2. /course/ vs /product/ — CDCA — Last 7d (all channels) ===")
req2 = RunReportRequest(
    property=f"properties/{GA4_PROP}",
    date_ranges=[DateRange(start_date=LAST7_START, end_date=LAST7_END)],
    dimensions=[Dimension(name="landingPage"), Dimension(name="sessionDefaultChannelGroup")],
    metrics=[Metric(name="sessions"), Metric(name="engagementRate"), Metric(name="conversions")],
    dimension_filter=FilterExpression(filter=Filter(
        field_name="landingPage",
        string_filter=Filter.StringFilter(
            match_type=Filter.StringFilter.MatchType.CONTAINS,
            value="ohio-cdca"
        )
    )),
    order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)]
)
resp2 = client.run_report(req2)
output["course_vs_product_last7"] = []
print(f"{'URL':<60} {'Channel':<22} {'Sessions':>8} {'EngRate':>8}")
print("-" * 100)
for row in resp2.rows:
    page    = row.dimension_values[0].value
    channel = row.dimension_values[1].value
    sess    = row.metric_values[0].value
    eng     = f"{float(row.metric_values[1].value)*100:.0f}%"
    output["course_vs_product_last7"].append({"page": page, "channel": channel, "sessions": sess})
    print(f"{page:<60} {channel:<22} {sess:>8} {eng:>8}")


# ── 3. Site-wide organic sessions — two separate pulls ───────────────────────
print("\n\n=== 3. Site-wide sessions by channel ===")
output["sitewide_sessions"] = {}
for label, (s, e) in [("last_7d", (LAST7_START, LAST7_END)), ("march_baseline", (MARCH_START, MARCH_END))]:
    req3 = RunReportRequest(
        property=f"properties/{GA4_PROP}",
        date_ranges=[DateRange(start_date=s, end_date=e)],
        dimensions=[Dimension(name="sessionDefaultChannelGroup")],
        metrics=[Metric(name="sessions"), Metric(name="newUsers")],
        order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)]
    )
    resp3 = client.run_report(req3)
    output["sitewide_sessions"][label] = []
    total = 0
    print(f"\n  {label} ({s} → {e}):")
    print(f"  {'Channel':<28} {'Sessions':>10} {'New Users':>10}")
    print("  " + "-" * 50)
    for row in resp3.rows:
        ch   = row.dimension_values[0].value
        sess = int(row.metric_values[0].value)
        new  = row.metric_values[1].value
        total += sess
        output["sitewide_sessions"][label].append({"channel": ch, "sessions": sess})
        print(f"  {ch:<28} {sess:>10} {new:>10}")
    print(f"  {'TOTAL':<28} {total:>10}")


# ── 4. Top organic landing pages last 7d ─────────────────────────────────────
print("\n\n=== 4. Top 25 organic landing pages — last 7d ===")
req4 = RunReportRequest(
    property=f"properties/{GA4_PROP}",
    date_ranges=[DateRange(start_date=LAST7_START, end_date=LAST7_END)],
    dimensions=[Dimension(name="landingPage")],
    metrics=[Metric(name="sessions")],
    dimension_filter=FilterExpression(filter=Filter(
        field_name="sessionDefaultChannelGroup",
        string_filter=Filter.StringFilter(
            match_type=Filter.StringFilter.MatchType.EXACT,
            value="Organic Search"
        )
    )),
    order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)],
    limit=25
)
resp4 = client.run_report(req4)
output["top_organic_pages_last7"] = []
print(f"{'Landing Page':<65} {'Organic Sessions':>16}")
print("-" * 83)
for i, row in enumerate(resp4.rows, 1):
    page = row.dimension_values[0].value
    sess = row.metric_values[0].value
    output["top_organic_pages_last7"].append({"page": page, "sessions": int(sess)})
    print(f"{i:>2}. {page:<62} {sess:>16}")


# ── Save ──────────────────────────────────────────────────────────────────────
out_path = "/Users/melissacedeno/Desktop/Claude/embertribe-decks/reference files/ceu-matrix/ga4-extended-pull.json"
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"\n✓ Saved to: {out_path}")
