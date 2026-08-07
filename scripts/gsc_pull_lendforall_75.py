"""
Re-measure the 75-article 'recent batch' (sitemap post-sitemap, lastmod >= 2026-07-14).
Pull GSC clicks/impressions/keyword-count/position per article + aggregate + ranking buckets.
"""
import json
from datetime import date, timedelta
from urllib.parse import urlparse
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY_FILE = r"C:\Users\jones\Downloads\embertribe-content-tools-e6776250739e (1).json"
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
service = build("searchconsole", "v1", credentials=creds)
site = "sc-domain:lendforall.ca"
try:
    service.sites().get(siteUrl=site).execute()
except Exception:
    site = "https://lendforall.ca/"

# The 75 recent-batch article slugs (sitemap posts 49-123, lastmod >= 2026-07-14)
SLUGS = """
how-to-spot-a-legitimate-online-bad-credit-lender-in-canada
cpp-disability-benefits-eligibility-and-application
gis-guaranteed-income-supplement-who-qualifies
canada-child-benefit-ccb-payment-dates-and-amounts
canada-workers-benefit-acwb-what-you-get
disability-tax-credit-in-canada-who-qualifies
pc-financial-mastercard-review-good-for-bad-credit
capital-one-guaranteed-approval-credit-cards-the-reality
consumer-proposal-timeline-what-5-years-actually-looks-like
credit-counselling-services-in-canada-free-help
how-to-dispute-a-credit-report-error-in-canada
7-strategies-for-paying-off-your-loan-faster
gross-vs-net-income
refinancing-car-loans-for-beginners
everything-you-need-to-know-about-bad-credit
what-is-the-minimum-credit-score-for-a-mortgage-in-canada
how-to-get-a-fast-cash-loan-in-canada
how-to-rent-to-own-in-ontario
get-the-best-rate-for-a-line-of-credit-in-canada
how-consumer-credit-counselling-services-actually-work
questions-about-debt-consolidation
what-is-debt-forgiveness-in-canada
best-buy-financing
how-to-qualify-for-a-1000-loan-in-canada
about-car-title-loans
guide-to-building-your-emergency-fund
understanding-car-loans
leasing-vs-financing-how-to-get-your-hands-on-a-vehicle
7-smart-ways-to-repair-your-bad-credit
how-to-get-an-unsecured-personal-loan-with-a-bad-credit
credit-repair-companies-explained
direct-lenders-vs-loan-matching-platforms-bad-credit
ontario-payday-loan-laws
bc-payday-loan-rules
toronto-payday-loan-alternatives
calgary-borrowing-energy-sector
ottawa-government-employee-borrower-tips
quebec-payday-loan-caps-montreal
brampton-newcomer-borrower-guide
saskatoon-borrower-resources
toronto-average-credit-score
calgary-credit-building-tips
winnipeg-family-credit-recovery
edmonton-borrowing-after-job-loss
bad-credit-loans-vancouver
canada-retirement-age-changes
gst-hst-payment-dates-canada
compound-interest-explained-canada
tfsa-vs-rrsp
understanding-canadian-interest-rates
vancouver-payday-loan-regulations-explained
what-counts-as-bad-credit-in-british-columbia
hamilton-family-finance-guide-when-short-term-borrowing-hurts
alberta-payday-loan-rates-reforms
what-counts-as-bad-credit-in-ontario
how-bad-credit-loans-work-in-canada
how-payday-loans-work-in-canada
edmonton-payday-loan-costs-what-300-really-costs-you
5-free-financial-resources-for-winnipeg-borrowers
a-guide-to-cpp-payment-dates-for-the-canada-pension-plan
canadian-government-benefits-and-financial-assistance-programs
financial-literacy-for-canadians-the-basics
how-to-build-an-emergency-fund-in-canada
how-to-reduce-and-manage-debt-in-canada
ei-benefits-in-canada-how-many-weeks-you-get
what-affects-credit-score-in-canada-five-factors
6-payday-loan-myths
what-is-the-prime-rate
ottawa-rebuild-credit-guide
applying-for-payday-loans-for-the-first-time
the-right-choice-installment-vs-payday-loans
what-is-debt-consolidation
personal-loans-vs-lines-of-credit-for-bad-credit-borrowers
quebec-borrower-protections
credit-cards-580-649-credit-score-canada
""".split()

paths = {f"/{s}/": s for s in SLUGS}
assert len(paths) == 75, f"expected 75 got {len(paths)}"

END = date.today().isoformat()
START = "2026-05-01"

def q(dims, row_limit=25000):
    body = {"startDate": START, "endDate": END, "dimensions": dims, "rowLimit": row_limit}
    return service.searchanalytics().query(siteUrl=site, body=body).execute().get("rows", [])

art = {p: {"slug": paths[p], "clicks": 0, "impressions": 0, "kw": 0, "position": None} for p in paths}

for r in q(["page"], row_limit=5000):
    path = urlparse(r["keys"][0]).path
    if path in art:
        art[path]["clicks"] = r["clicks"]
        art[path]["impressions"] = r["impressions"]
        art[path]["position"] = round(r["position"], 1)

buckets = {"p1": 0, "p2": 0, "p3_5": 0, "p6plus": 0}
for r in q(["page", "query"], row_limit=25000):
    path = urlparse(r["keys"][0]).path
    if path in art:
        art[path]["kw"] += 1
        pos = r["position"]
        if pos <= 10: buckets["p1"] += 1
        elif pos <= 20: buckets["p2"] += 1
        elif pos <= 50: buckets["p3_5"] += 1
        else: buckets["p6plus"] += 1

earning = [a for a in art.values() if a["impressions"] > 0]
total_clicks = sum(a["clicks"] for a in art.values())
total_impr = sum(a["impressions"] for a in art.values())
total_kw = sum(a["kw"] for a in art.values())
p1p2 = buckets["p1"] + buckets["p2"]

out = {
    "cohort": "sitemap recent batch (75 posts, lastmod >= 2026-07-14)",
    "window": [START, END],
    "article_count": 75,
    "earning_count": len(earning),
    "total_clicks": total_clicks,
    "total_impressions": total_impr,
    "total_keywords": total_kw,
    "page1_2_keywords": p1p2,
    "ranking_buckets": buckets,
    "articles": sorted(art.values(), key=lambda x: x["impressions"], reverse=True),
}
with open(r"C:\Users\jones\Claude\lendforall-impact-75.json", "w") as f:
    json.dump(out, f, indent=2)

print(f"75 articles | earning impressions: {len(earning)} | clicks {total_clicks} | impr {total_impr} | kw {total_kw} | pg1-2 kw {p1p2}")
print("buckets", buckets)
print("\nTop 12 by impressions:")
for a in out["articles"][:12]:
    print(f"  {a['impressions']:>5} impr | {a['clicks']:>2} clk | {a['kw']:>3} kw | pos {a['position']} | {a['slug']}")
