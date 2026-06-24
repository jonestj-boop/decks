"""
Pull GSC data for fleetsnap.ai — /guides keyword-intent analysis.
Last 90 days, per-guide top queries + site-wide pages/queries.
"""
import json, datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY_FILE = "/Users/melissacedeno/Desktop/Claude/embertribe-decks/embertribe-content-tools-e6776250739e.json"
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
SITE_URL = "sc-domain:fleetsnap.ai"

END = datetime.date(2026, 6, 24)
START = END - datetime.timedelta(days=90)
START_DATE = START.isoformat()
END_DATE = END.isoformat()

creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
service = build("searchconsole", "v1", credentials=creds)

def query(dimensions, row_limit=1000, filters=None):
    body = {"startDate": START_DATE, "endDate": END_DATE,
            "dimensions": dimensions, "rowLimit": row_limit}
    if filters:
        body["dimensionFilterGroups"] = filters
    return service.searchanalytics().query(siteUrl=SITE_URL, body=body).execute()

GUIDES = [
    "/guides",
    "/guides/turo-guest-messaging-data",
    "/guides/turo-monthly-rentals",
    "/guides/ai-for-turo",
    "/guides/turo-co-host-split",
    "/guides/turo-partner-statement",
    "/guides/turo-virtual-assistant-guide",
    "/guides/turo-cohosting-guide",
    "/guides/turo-damage-claim",
]
BASE = "https://fleetsnap.ai"

def row(r):
    return {"key": r["keys"][0], "clicks": r["clicks"], "impressions": r["impressions"],
            "ctr_pct": round(r["ctr"]*100, 2), "position": round(r["position"], 1)}

out = {"property": SITE_URL, "start_date": START_DATE, "end_date": END_DATE}

# Site-wide top pages
print("Site-wide top pages...")
pages = query(["page"], row_limit=100)
out["top_pages"] = [dict(row(r), page=r["keys"][0].replace(BASE, "")) for r in pages.get("rows", [])]
for p in out["top_pages"][:25]:
    print(f"  {p['clicks']:>5} clk {p['impressions']:>7} imp pos{p['position']:>5} {p['page']}")

# Site-wide top queries
print("\nSite-wide top queries...")
sq = query(["query"], row_limit=100)
out["top_queries_sitewide"] = [row(r) for r in sq.get("rows", [])]

# Per-guide queries
out["per_guide"] = {}
for g in GUIDES:
    url = BASE + g
    flt = [{"filters": [{"dimension": "page", "operator": "equals", "expression": url}]}]
    # totals for the page
    pr = query(["page"], filters=flt)
    totals = pr.get("rows", [])
    tot = row(totals[0]) if totals else {"clicks":0,"impressions":0,"ctr_pct":0,"position":0}
    qr = query(["query"], row_limit=30, filters=flt)
    queries = [row(r) for r in qr.get("rows", [])]
    out["per_guide"][g] = {"totals": {k:tot[k] for k in ("clicks","impressions","ctr_pct","position")},
                            "queries": queries}
    print(f"\n=== {g} === clicks={tot['clicks']} imp={tot['impressions']} ctr={tot['ctr_pct']}% pos={tot['position']}")
    for q in queries[:12]:
        print(f"   {q['clicks']:>4} clk {q['impressions']:>6} imp ctr{q['ctr_pct']:>5} pos{q['position']:>5} | {q['key']}")

with open("/Users/melissacedeno/Desktop/Claude/embertribe-decks/gsc-fleetsnap.json", "w") as f:
    json.dump(out, f, indent=2)
print("\nSaved gsc-fleetsnap.json")
