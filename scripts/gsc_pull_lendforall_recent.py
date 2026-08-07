"""
Pull recent daily GSC data for lendforall.ca to check whether traffic recovered.
"""
import json
from datetime import date, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY_FILE = r"C:\Users\jones\Downloads\embertribe-content-tools-e6776250739e (1).json"
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]

credentials = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
service = build("searchconsole", "v1", credentials=credentials)

site_url = "sc-domain:lendforall.ca"
try:
    service.sites().get(siteUrl=site_url).execute()
except Exception:
    site_url = "https://lendforall.ca/"

END_DATE = date.today().isoformat()
START_DATE = (date.today() - timedelta(days=120)).isoformat()

def q(dimensions, row_limit=1000):
    body = {"startDate": START_DATE, "endDate": END_DATE,
            "dimensions": dimensions, "rowLimit": row_limit}
    return service.searchanalytics().query(siteUrl=site_url, body=body).execute()

daily = q(["date"], row_limit=200)
rows = daily.get("rows", [])

monthly = {}
for r in rows:
    d = r["keys"][0]
    m = d[:7]
    monthly.setdefault(m, {"clicks": 0, "impressions": 0, "days": 0})
    monthly[m]["clicks"] += r["clicks"]
    monthly[m]["impressions"] += r["impressions"]
    monthly[m]["days"] += 1

out = {
    "property": site_url,
    "range": [START_DATE, END_DATE],
    "monthly": monthly,
    "last_14_days": [
        {"date": r["keys"][0], "clicks": r["clicks"], "impressions": r["impressions"]}
        for r in rows[-14:]
    ],
}
print(json.dumps(out, indent=2))
with open(r"C:\Users\jones\Claude\gsc-lendforall-fresh.json", "w") as f:
    json.dump(out, f, indent=2)
