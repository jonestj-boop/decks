"""
Doctronic.ai — July 2026 refresh pull for the churned-client urgency update.
Extends the daily trend past June 30, pulls July page-level data for ET/DT
re-classification, and monthly blog-vs-sitewide clicks.
"""
import json, datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY_FILE = r"C:\Users\jones\Claude\embertribe-content-tools-e6776250739e.json"
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
SITE_URL = "sc-domain:doctronic.ai"

creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
svc = build("searchconsole", "v1", credentials=creds)

def q(start, end, dimensions, row_limit=25000, filters=None, start_row=0):
    body = {"startDate": start, "endDate": end, "dimensions": dimensions,
            "rowLimit": row_limit, "startRow": start_row}
    if filters:
        body["dimensionFilterGroups"] = filters
    return svc.searchanalytics().query(siteUrl=SITE_URL, body=body).execute()

blog_filter = [{"filters":[{"dimension":"page","operator":"contains","expression":"/blog/"}]}]

# 1) Daily site-wide + daily blog, May 1 -> today (GSC lags ~2-3 days)
today = datetime.date(2026,7,30)
start = "2026-05-01"
end = today.isoformat()

daily_all  = q(start, end, ["date"], row_limit=500).get("rows", [])
daily_blog = q(start, end, ["date"], row_limit=500, filters=blog_filter).get("rows", [])

def daily_list(rows):
    return [{"date": r["keys"][0], "clicks": round(r["clicks"]),
             "impressions": round(r["impressions"]), "position": round(r["position"],1)} for r in rows]

print("=== DAILY BLOG (last available) ===")
db = daily_list(daily_blog)
for r in db[-8:]:
    print(" ", r["date"], f'{r["clicks"]:>7,} clicks | {r["impressions"]:>10,} imp | pos {r["position"]}')
print("  latest date w/ data:", db[-1]["date"] if db else "NONE")

# 2) Monthly blog clicks + sitewide clicks
def monthly(rows):
    m={}
    for r in rows:
        k=r["keys"][0][:7]; m.setdefault(k,{"clicks":0,"imp":0})
        m[k]["clicks"]+=r["clicks"]; m[k]["imp"]+=r["impressions"]
    return {k:{"clicks":round(v["clicks"]),"imp":round(v["imp"])} for k,v in sorted(m.items())}

mb = monthly(daily_blog); ma = monthly(daily_all)
print("\n=== MONTHLY BLOG CLICKS ===")
for k in mb: print(f'  {k}: blog {mb[k]["clicks"]:>8,} | sitewide {ma[k]["clicks"]:>8,}')

# 3) July page-level (blog) for ET/DT reclassification, paginated
jul_start, jul_end = "2026-07-01", "2026-07-29"
pages=[]; sr=0
while True:
    batch = q(jul_start, jul_end, ["page"], row_limit=25000, filters=blog_filter, start_row=sr).get("rows", [])
    pages += batch
    if len(batch) < 25000: break
    sr += 25000
print(f"\n=== JULY page-level blog rows: {len(pages)} ===")

# 4) June page-level (blog) too, to compute Jun->Jul declines
jun_pages=[]; sr=0
while True:
    batch = q("2026-06-01","2026-06-30", ["page"], row_limit=25000, filters=blog_filter, start_row=sr).get("rows", [])
    jun_pages += batch
    if len(batch) < 25000: break
    sr += 25000
print(f"=== JUNE page-level blog rows: {len(jun_pages)} ===")

out = {
  "pulled": today.isoformat(),
  "daily_all": daily_list(daily_all),
  "daily_blog": db,
  "monthly_blog": mb,
  "monthly_all": ma,
  "july_range": [jul_start, jul_end],
  "july_pages": [{"page":r["keys"][0],"clicks":round(r["clicks"]),"impressions":round(r["impressions"]),
                  "ctr":round(r["ctr"]*100,3),"position":round(r["position"],1)} for r in pages],
  "june_pages": [{"page":r["keys"][0],"clicks":round(r["clicks"]),"impressions":round(r["impressions"]),
                  "ctr":round(r["ctr"]*100,3),"position":round(r["position"],1)} for r in jun_pages],
}
with open(r"C:\Users\jones\Claude\gsc-doctronic-july.json","w") as f:
    json.dump(out,f,indent=2)
print("\nSaved gsc-doctronic-july.json")
