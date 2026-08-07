"""
Comprehensive GSC pull for lendforall.ca:
 1. Recovery breakdown  (query + page level, trough vs recovery)
 2. Blog-article impact  (per-article clicks/impressions/keyword count, ranking buckets)
Outputs a single JSON consumed by the HTML builders.
"""
import json
from datetime import date, timedelta
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

TODAY = date.today()

def q(start, end, dims, row_limit=25000, filters=None):
    body = {"startDate": start, "endDate": end, "dimensions": dims, "rowLimit": row_limit}
    if filters:
        body["dimensionFilterGroups"] = filters
    return service.searchanalytics().query(siteUrl=site, body=body).execute().get("rows", [])

# ---- Blog article slugs (published May-June 2026) ----
recent = json.load(open(r"C:\Users\jones\Claude\gsc-lendforall-recent.json"))
blog = {}
for p in recent["new_pages"]:
    slug = p["page"]
    if slug.rstrip("/").endswith("/blog/9") or slug.rstrip("/") == "/blog/9":
        continue
    blog[slug] = {"first_seen": p["first_seen"]}
blog_slugs = set(blog.keys())

# ---- Per-page performance since publishing window (May 1 -> today) ----
PUB_START = "2026-05-01"
END = TODAY.isoformat()
page_rows = q(PUB_START, END, ["page"], row_limit=5000)
for r in page_rows:
    url = r["keys"][0]
    path = "/" + url.split("lendforall.ca", 1)[-1].lstrip("/") if "lendforall.ca" in url else url
    # normalize to path
    from urllib.parse import urlparse
    path = urlparse(url).path
    if path in blog:
        blog[path]["clicks"] = r["clicks"]
        blog[path]["impressions"] = r["impressions"]
        blog[path]["position"] = round(r["position"], 1)

# ---- Per page+query: keyword counts and ranking buckets for blog pages ----
pq = q(PUB_START, END, ["page", "query"], row_limit=25000)
buckets = {"p1": 0, "p2": 0, "p3_5": 0, "p6plus": 0}
for r in pq:
    from urllib.parse import urlparse
    path = urlparse(r["keys"][0]).path
    if path in blog:
        b = blog[path]
        b["kw"] = b.get("kw", 0) + 1
        pos = r["position"]
        if pos <= 10: buckets["p1"] += 1
        elif pos <= 20: buckets["p2"] += 1
        elif pos <= 50: buckets["p3_5"] += 1
        else: buckets["p6plus"] += 1

blog_total_kw = sum(v.get("kw", 0) for v in blog.values())
blog_total_clicks = sum(v.get("clicks", 0) for v in blog.values())
blog_total_impr = sum(v.get("impressions", 0) for v in blog.values())

# ---- Recovery: query-level, trough (June) vs recovery (last 28d) ----
def month_range(y, m):
    start = date(y, m, 1)
    end = (date(y, m + 1, 1) - timedelta(days=1)) if m < 12 else date(y, 12, 31)
    return start.isoformat(), end.isoformat()

jun_s, jun_e = month_range(2026, 6)
rec_e = (TODAY - timedelta(days=2)).isoformat()
rec_s = (TODAY - timedelta(days=30)).isoformat()

def keyed(rows):
    return {r["keys"][0]: r for r in rows}

q_jun = keyed(q(jun_s, jun_e, ["query"], row_limit=5000))
q_rec = keyed(q(rec_s, rec_e, ["query"], row_limit=5000))
p_jun = keyed(q(jun_s, jun_e, ["page"], row_limit=5000))
p_rec = keyed(q(rec_s, rec_e, ["page"], row_limit=5000))

def deltas(jun, rec, topn=15):
    out = []
    for k in set(jun) | set(rec):
        jc = jun.get(k, {}).get("clicks", 0)
        rc = rec.get(k, {}).get("clicks", 0)
        out.append({"key": k, "jun_clicks": jc, "rec_clicks": rc, "delta": rc - jc,
                    "rec_impr": rec.get(k, {}).get("impressions", 0)})
    return sorted(out, key=lambda x: x["delta"], reverse=True)[:topn]

out = {
    "property": site,
    "generated": END,
    "recovery": {
        "trough_month": {"range": [jun_s, jun_e]},
        "recovery_window": {"range": [rec_s, rec_e]},
        "top_query_gainers": deltas(q_jun, q_rec),
        "top_page_gainers": deltas(p_jun, p_rec),
    },
    "blog": {
        "publish_window": [PUB_START, END],
        "article_count": len(blog),
        "total_clicks": blog_total_clicks,
        "total_impressions": blog_total_impr,
        "total_keywords": blog_total_kw,
        "ranking_buckets": buckets,
        "articles": sorted(
            [{"path": k, **v} for k, v in blog.items()],
            key=lambda x: x.get("impressions", 0), reverse=True),
    },
}
with open(r"C:\Users\jones\Claude\lendforall-impact-data.json", "w") as f:
    json.dump(out, f, indent=2)
print("articles:", len(blog), "blog clicks:", blog_total_clicks,
      "blog impr:", blog_total_impr, "blog kw:", blog_total_kw)
print("buckets:", buckets)
print("top query gainers:")
for g in out["recovery"]["top_query_gainers"][:8]:
    print(f"   +{g['delta']:>4}  jun {g['jun_clicks']:>3} -> rec {g['rec_clicks']:>3}  {g['key']}")
