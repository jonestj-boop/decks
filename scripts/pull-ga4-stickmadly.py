"""
Pull the GA4 reports needed for the Stickmadly omnichannel deck.

Usage:
    python3 scripts/pull-ga4-stickmadly.py --property-id 123456789 [--days 90] [--output ga4-stickmadly.json]

Requires:
    embertribe-content-tools-e6776250739e.json to have Viewer access on the
    GA4 property (Admin > Property Access Management > add
    embertribe-content-tools@embertribe-content-tools.iam.gserviceaccount.com).
    Run scripts/check-ga4-access.py (or the admin API scan) first to confirm
    access and get the numeric property ID if you don't have it yet.

Library: google-analytics-data (BetaAnalyticsDataClient), scope analytics.readonly.
"""

import argparse
import json
import sys

from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest,
    DateRange,
    Dimension,
    Metric,
)

KEY_FILE = "embertribe-content-tools-e6776250739e.json"
SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]


def get_client():
    creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
    return BetaAnalyticsDataClient(credentials=creds)


def run(client, property_id, dimensions, metrics, days, order_bys=None, limit=50):
    request = RunReportRequest(
        property=f"properties/{property_id}",
        date_ranges=[DateRange(start_date=f"{days}daysAgo", end_date="today")],
        dimensions=[Dimension(name=d) for d in dimensions],
        metrics=[Metric(name=m) for m in metrics],
        order_bys=order_bys or [],
        limit=limit,
    )
    response = client.run_report(request)
    rows = []
    for row in response.rows:
        rows.append(
            {
                **{dimensions[i]: dv.value for i, dv in enumerate(row.dimension_values)},
                **{metrics[i]: mv.value for i, mv in enumerate(row.metric_values)},
            }
        )
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--property-id", required=True, help="Numeric GA4 property ID, e.g. 123456789 (not the 'properties/' prefix)")
    parser.add_argument("--days", type=int, default=90)
    parser.add_argument("--output", default="ga4-stickmadly.json")
    args = parser.parse_args()

    client = get_client()
    results = {}

    print(f"Pulling last {args.days} days for properties/{args.property_id}...\n")

    # 1. Site-wide AOV, revenue, transactions
    print("1/6  Site-wide e-commerce summary...")
    results["ecommerce_summary"] = run(
        client, args.property_id,
        dimensions=[],
        metrics=["transactions", "purchaseRevenue", "averagePurchaseRevenue", "sessions", "totalUsers"],
        days=args.days,
    )

    # 2. Traffic by channel, monthly trend
    print("2/6  Traffic by channel, monthly...")
    results["channel_trend"] = run(
        client, args.property_id,
        dimensions=["yearMonth", "sessionDefaultChannelGroup"],
        metrics=["sessions", "totalUsers", "transactions", "purchaseRevenue"],
        days=args.days,
        order_bys=[{"dimension": {"dimension_name": "yearMonth"}}],
    )

    # 3. New vs. returning purchasers (closest API proxy for repeat-purchase rate)
    print("3/6  New vs. returning, transactions and revenue...")
    results["new_vs_returning"] = run(
        client, args.property_id,
        dimensions=["newVsReturning"],
        metrics=["totalUsers", "transactions", "purchaseRevenue", "averagePurchaseRevenue"],
        days=args.days,
    )

    # 4. Landing page performance
    print("4/6  Landing page performance...")
    results["landing_pages"] = run(
        client, args.property_id,
        dimensions=["landingPagePlusQueryString"],
        metrics=["sessions", "engagementRate", "transactions", "purchaseRevenue"],
        days=args.days,
        order_bys=[{"metric": {"metric_name": "sessions"}, "desc": True}],
        limit=30,
    )

    # 5. On-site funnel, site-wide (cross-check against Meta's own funnel)
    print("5/6  Site-wide funnel (sessions to purchase)...")
    results["funnel"] = run(
        client, args.property_id,
        dimensions=[],
        metrics=["sessions", "addToCarts", "checkouts", "ecommercePurchases", "cartToViewRate", "purchaseToViewRate"],
        days=args.days,
    )

    # 6. Device breakdown on checkout
    print("6/6  Funnel by device...")
    results["funnel_by_device"] = run(
        client, args.property_id,
        dimensions=["deviceCategory"],
        metrics=["sessions", "addToCarts", "checkouts", "ecommercePurchases"],
        days=args.days,
    )

    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nSaved to {args.output}\n")
    print("=" * 60)
    for key, rows in results.items():
        print(f"\n{key}:")
        for row in rows:
            print(" ", row)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nERROR: {e}", file=sys.stderr)
        print(
            "\nIf this is a permission error, confirm the service account "
            "has Viewer access on this exact property in GA4 Admin > "
            "Property Access Management, and that --property-id is the "
            "numeric ID (not the 'G-XXXX' measurement ID or the account ID).",
            file=sys.stderr,
        )
        sys.exit(1)
