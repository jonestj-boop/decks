"""Pull GSC queries for the /lenders/icash/ page to source real FAQ content."""
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

END = date.today().isoformat()
START = (date.today() - timedelta(days=90)).isoformat()
body = {
    "startDate": START, "endDate": END,
    "dimensions": ["query"], "rowLimit": 100,
    "dimensionFilterGroups": [{"filters": [
        {"dimension": "page", "operator": "contains", "expression": "/lenders/icash"}
    ]}],
}
rows = service.searchanalytics().query(siteUrl=site, body=body).execute().get("rows", [])
out = [{"query": r["keys"][0], "clicks": r["clicks"], "impr": r["impressions"],
        "pos": round(r["position"], 1)} for r in rows]
out.sort(key=lambda x: x["impr"], reverse=True)
json.dump({"page": "/lenders/icash/", "window": [START, END], "queries": out},
          open(r"C:\Users\jones\Claude\icash-queries.json", "w"), indent=2)
print(f"{len(out)} queries for /lenders/icash/  ({START} to {END})")
for q in out[:30]:
    print(f"  {q['impr']:>5} impr | {q['clicks']:>2} clk | pos {q['pos']:>5} | {q['query']}")
