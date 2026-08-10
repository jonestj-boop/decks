"""
Query-level AVERAGE POSITION movement for lendforall.ca: June 2026 vs last 30 days.
Lower position = better. Positive movement = moved UP the rankings.
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
JUN_S, JUN_E = "2026-06-01", "2026-06-30"
REC_E = (TODAY - timedelta(days=2)).isoformat()
REC_S = (TODAY - timedelta(days=30)).isoformat()

def q(start, end):
    body = {"startDate": start, "endDate": end, "dimensions": ["query"], "rowLimit": 5000}
    rows = service.searchanalytics().query(siteUrl=site, body=body).execute().get("rows", [])
    return {r["keys"][0]: r for r in rows}

jun = q(JUN_S, JUN_E)
rec = q(REC_S, REC_E)

rows = []
for kw in set(jun) & set(rec):
    j, r = jun[kw], rec[kw]
    # require some visibility in both periods so the average position is meaningful
    if j["impressions"] < 20 or r["impressions"] < 20:
        continue
    jp, rp = j["position"], r["position"]
    rows.append({
        "query": kw,
        "jun_pos": round(jp, 1), "now_pos": round(rp, 1),
        "move": round(jp - rp, 1),          # positive = moved up
        "jun_clicks": j["clicks"], "now_clicks": r["clicks"],
        "now_impr": r["impressions"],
    })

# Biggest upward movers among terms with real search volume
movers_up = sorted([x for x in rows if x["move"] > 0], key=lambda x: x["move"], reverse=True)
movers_dn = sorted([x for x in rows if x["move"] < 0], key=lambda x: x["move"])

# Core money terms to always show
CORE = ["loans for bad credit", "bad credit loans", "loans for bad credit canada",
        "personal loans canada", "payday loans alberta", "instant loans canada 24/7",
        "bad credit loans canada", "loans for bad credit instant", "no credit check loans canada"]
by_q = {x["query"]: x for x in rows}
core = [by_q[c] for c in CORE if c in by_q]

out = {"jun": [JUN_S, JUN_E], "recent": [REC_S, REC_E],
       "core": core, "movers_up": movers_up[:15], "movers_down": movers_dn[:8],
       "total_tracked": len(rows)}
with open(r"C:\Users\jones\Claude\lendforall-positions.json", "w") as f:
    json.dump(out, f, indent=2)

def show(title, arr):
    print(f"\n{title}")
    for x in arr:
        arrow = "UP  " if x["move"] > 0 else "DOWN"
        print(f"  {arrow} {x['jun_pos']:>5} -> {x['now_pos']:>5}  ({x['move']:+.1f})  imp {x['now_impr']:>5}  {x['query']}")

print(f"tracked queries (>=20 impr both periods): {len(rows)}")
show("CORE MONEY TERMS", core)
show("TOP UPWARD MOVERS", movers_up[:15])
show("SLIPPED", movers_dn[:8])
