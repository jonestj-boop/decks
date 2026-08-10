"""
Doctronic.ai — GA4 July refresh for the content-audit update.
Pulls monthly Organic Search sessions site-wide and blog-only (landingPage
contains /blog/), Dec 2025 -> Jul 2026, to complete slide 2's trend through July.
Also pulls blog engagement rate + avg engagement time by month for context.
GA4 property 373721890. Window ends Jul 28 to match the GSC pull.
"""
import json
from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange, Dimension, Metric, RunReportRequest,
    FilterExpression, Filter, FilterExpressionList, OrderBy
)

KEY = r"C:\Users\jones\Claude\embertribe-content-tools-e6776250739e.json"
PROP = "properties/373721890"
creds = service_account.Credentials.from_service_account_file(
    KEY, scopes=["https://www.googleapis.com/auth/analytics.readonly"])
client = BetaAnalyticsDataClient(credentials=creds)

RANGE = ("2025-12-01", "2026-07-28")
organic = FilterExpression(filter=Filter(
    field_name="sessionDefaultChannelGroup",
    string_filter=Filter.StringFilter(
        match_type=Filter.StringFilter.MatchType.EXACT, value="Organic Search")))
blog = FilterExpression(filter=Filter(
    field_name="landingPage",
    string_filter=Filter.StringFilter(
        match_type=Filter.StringFilter.MatchType.CONTAINS, value="/blog/")))

def monthly(dim_filter, metrics):
    req = RunReportRequest(
        property=PROP,
        date_ranges=[DateRange(start_date=RANGE[0], end_date=RANGE[1])],
        dimensions=[Dimension(name="yearMonth")],
        metrics=[Metric(name=m) for m in metrics],
        dimension_filter=dim_filter,
        order_bys=[OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name="yearMonth"))])
    resp = client.run_report(req)
    out = {}
    for row in resp.rows:
        ym = row.dimension_values[0].value  # YYYYMM
        out[ym] = {m: row.metric_values[i].value for i, m in enumerate(metrics)}
    return out

site = monthly(organic, ["sessions"])
blog_m = monthly(
    FilterExpression(and_group=FilterExpressionList(expressions=[organic, blog])),
    ["sessions", "engagementRate", "averageSessionDuration"])

print("=== SITE-WIDE ORGANIC SESSIONS BY MONTH ===")
for ym in sorted(site):
    print(f"  {ym}: {int(float(site[ym]['sessions'])):>10,}")
print("\n=== BLOG-ONLY ORGANIC SESSIONS BY MONTH ===")
for ym in sorted(blog_m):
    s = int(float(blog_m[ym]['sessions']))
    er = float(blog_m[ym]['engagementRate']) * 100
    dur = float(blog_m[ym]['averageSessionDuration'])
    print(f"  {ym}: {s:>9,} | engage {er:4.1f}% | avg {dur:5.1f}s")

out = {"range": RANGE, "site_monthly": site, "blog_monthly": blog_m}
with open(r"C:\Users\jones\Claude\gsc-doctronic-ga4-july.json", "w") as f:
    json.dump(out, f, indent=2)
print("\nSaved gsc-doctronic-ga4-july.json")
