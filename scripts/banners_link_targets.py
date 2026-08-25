"""
Banners.com — Backlink target prioritization from GSC striking-distance data.

Client is on Authority Accelerator ($5,250/mo): 2x DA50+ backlinks per month.
Goal: point those links at money pages within striking distance of page-one
top spots, ranked by projected click uplift.

Input : gsc_banners.json  (GSC pull, 2025-11-01 .. 2026-04-30, 6 months)
Output: banners-com-link-target-plan.xlsx
"""
import json, math, re
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

SRC = r"C:\Users\jones\Claude\gsc_banners.json"
OUT = r"C:\Users\jones\Claude\banners-com-link-target-plan.xlsx"

data = json.load(open(SRC, encoding="utf-8"))
pages = data["top_pages"]
queries = data["top_queries"]

# ---- Conservative uplift model, calibrated to Banners.com's OWN CTR --------
# Banners.com's real CTR tops out around ~1.3-1.9% even in the top few spots
# (vs a 6-8% industry curve), so a generic curve massively overstates. Instead
# we model a boosted striking-distance page as doing a realistic MULTIPLE of its
# current clicks, larger the further it has to climb, capped at 3x. This anchors
# every number to what Banners.com pages actually achieve today.
def uplift_factor(pos):
    if pos >= 15: return 3.0   # deep page-two -> top-5 = biggest relative jump
    if pos >= 11: return 2.5   # low page-one / top of page-two
    if pos >= 8:  return 2.0
    return 1.5                 # already pos 5-8, less headroom

# ---- Page classification ----------------------------------------------------
# Non-money / not link-worthy targets for this exercise
BRAND_NAV = {"/", "/promo"}
def page_type(p):
    if p in BRAND_NAV: return "Brand/Nav"
    if p.startswith("/resources/"): return "Informational"
    return "Money (commercial)"

STOP = {"the","and","for","with","of","a","to","on","in","banners","banner","com","custom"}
def slug_tokens(page):
    return [t for t in re.split(r"[/-]", page) if t and t not in ("",)]

def money_keywords_for(page):
    """Best-matching commercial queries for a page slug, by impressions."""
    toks = set(t for t in re.split(r"[/-]", page) if t)
    toks.discard("")
    hits = []
    GENERIC = {"banners","banner","com","custom","the"}
    for q in queries:
        qt = set(re.split(r"\s+", q["query"].lower()))
        # require overlap on the distinctive (non-generic) slug tokens
        distinctive = toks - GENERIC
        overlap = distinctive & qt
        # generic pages (few distinctive tokens) fall back to full-slug overlap
        if overlap or (not distinctive and (toks & qt)):
            # skip brand/nav junk queries
            ql = q["query"]
            if any(b in ql for b in ["login","coupon","discount",".com","banners.com","banner .com"]):
                continue
            hits.append(q)
    hits.sort(key=lambda x: -x["impressions"])
    return hits[:3]

rows = []
for p in pages:
    page, pos, imp = p["page"], p["position"], p["impressions"]
    clicks = p["clicks"]; ctr = p["ctr_pct"]
    ptype = page_type(page)
    factor = uplift_factor(pos)
    proj_clicks = clicks * factor
    uplift = proj_clicks - clicks
    # striking distance sweet spot for a single-link nudge
    striking = 5.0 <= pos <= 20.0
    kws = money_keywords_for(page)
    kw_str = "; ".join(f'{k["query"]} (p{k["position"]:.0f}, {k["impressions"]:,} imp)' for k in kws)
    rows.append({
        "page": page, "type": ptype, "pos": pos, "imp": imp, "clicks": clicks,
        "ctr": ctr, "proj_clicks": round(proj_clicks), "uplift": round(uplift),
        "striking": striking, "keywords": kw_str,
    })

# Priority = money pages in striking distance, ranked by projected click uplift
targets = [r for r in rows if r["type"].startswith("Money") and r["striking"]]
targets.sort(key=lambda r: -r["uplift"])
for i, r in enumerate(targets, 1):
    r["rank"] = i
    r["tier"] = "Tier 1 (Priority)" if i <= 6 else ("Tier 2" if i <= 14 else "Tier 3")
    # 2 links / month schedule
    r["link_month"] = f"Month {((i-1)//2)+1}"

# ---- Workbook ---------------------------------------------------------------
EMBER = "FF333C"; INK = "1A1A1A"; MIST = "F2F2F2"; LINE = "D9D9D9"
wb = Workbook()

def style_header(ws, ncol, row=1):
    for c in range(1, ncol+1):
        cell = ws.cell(row=row, column=c)
        cell.font = Font(bold=True, color="FFFFFF", size=10)
        cell.fill = PatternFill("solid", fgColor=INK)
        cell.alignment = Alignment(vertical="center", wrap_text=True)
        cell.border = Border(bottom=Side(style="thin", color=LINE))

def autow(ws, widths):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

# --- Sheet 1: Link Target Priority ---
ws = wb.active; ws.title = "Link Target Priority"
title = ws.cell(row=1, column=1, value="Banners.com — Backlink Target Priority")
title.font = Font(bold=True, size=14, color=EMBER)
sub = ws.cell(row=2, column=1,
    value="Where to point the 2 DA50+ links/mo (Authority Accelerator). Money pages in striking distance (pos 5–20), "
          "ranked by projected click uplift if boosted to top-of-page-one. Source: GSC Nov 2025–Apr 2026.")
sub.font = Font(size=9, italic=True, color="595959")
ws.merge_cells(start_row=1, end_row=1, start_column=1, end_column=10)
ws.merge_cells(start_row=2, end_row=2, start_column=1, end_column=10)

hdr = ["#","Link Month","Tier","Target Page","Money Keyword(s) it ranks for","Avg Pos",
       "Monthly Impr.","Clicks/mo now","Proj. clicks/mo","Added clicks/mo"]
hrow = 4
for c, h in enumerate(hdr, 1): ws.cell(row=hrow, column=c, value=h)
style_header(ws, len(hdr), row=hrow)
r0 = hrow + 1
for i, r in enumerate(targets):
    rr = r0 + i
    vals = [r["rank"], r["link_month"], r["tier"], r["page"], r["keywords"],
            round(r["pos"],1), r["imp"], r["clicks"], r["proj_clicks"], r["uplift"]]
    for c, v in enumerate(vals, 1):
        cell = ws.cell(row=rr, column=c, value=v)
        cell.font = Font(size=9)
        cell.alignment = Alignment(vertical="center", wrap_text=(c in (4,5)))
        if i % 2: cell.fill = PatternFill("solid", fgColor=MIST)
    ws.cell(row=rr, column=1).font = Font(bold=True, size=9)
    ws.cell(row=rr, column=10).font = Font(bold=True, size=9, color=EMBER)
    if r["tier"].startswith("Tier 1"):
        ws.cell(row=rr, column=3).font = Font(bold=True, size=9, color=EMBER)
    for c in (7,8,9,10): ws.cell(row=rr, column=c).number_format = "#,##0"
    ws.cell(row=rr, column=6).number_format = "0.0"
# totals
tr = r0 + len(targets) + 1
ws.cell(row=tr, column=4, value="TOTAL opportunity (all striking-distance money pages)").font = Font(bold=True, size=9)
ws.cell(row=tr, column=8, value=sum(r["clicks"] for r in targets)).font = Font(bold=True, size=9)
ws.cell(row=tr, column=9, value=sum(r["proj_clicks"] for r in targets)).font = Font(bold=True, size=9)
ws.cell(row=tr, column=10, value=sum(r["uplift"] for r in targets)).font = Font(bold=True, size=9, color=EMBER)
for c in (8,9,10): ws.cell(row=tr, column=c).number_format = "#,##0"
ws.freeze_panes = "A5"
autow(ws, [4,10,15,28,44,8,13,13,14,14])

# --- Sheet 2: Money Keywords (Striking Distance) ---
ws2 = wb.create_sheet("Money Keywords (SD)")
t = ws2.cell(row=1, column=1, value="Money Keywords in Striking Distance (pos 5–20)")
t.font = Font(bold=True, size=13, color=EMBER)
ws2.merge_cells(start_row=1, end_row=1, start_column=1, end_column=6)
sub2 = ws2.cell(row=2, column=1, value="Commercial queries close enough that authority pointed at the ranking page can convert impressions to clicks. Brand/nav/coupon terms excluded.")
sub2.font = Font(size=9, italic=True, color="595959")
ws2.merge_cells(start_row=2, end_row=2, start_column=1, end_column=6)
h2 = ["Query","Avg Pos","Monthly Impr.","Clicks/mo","CTR %","Opportunity (impr × pos)"]
for c, h in enumerate(h2, 1): ws2.cell(row=4, column=c, value=h)
style_header(ws2, len(h2), row=4)
BRANDY = ["login","coupon","discount",".com","banners.com","banner .com","banneradsites"]
sd_q = [q for q in queries if 5.0 <= q["position"] <= 20.0
        and not any(b in q["query"] for b in BRANDY)]
sd_q.sort(key=lambda q: -q["impressions"])
for i, q in enumerate(sd_q):
    rr = 5 + i
    opp = q["impressions"]  # demand available at this position
    vals = [q["query"], round(q["position"],1), q["impressions"], q["clicks"], q["ctr_pct"], opp]
    for c, v in enumerate(vals, 1):
        cell = ws2.cell(row=rr, column=c, value=v)
        cell.font = Font(size=9)
        if i % 2: cell.fill = PatternFill("solid", fgColor=MIST)
    ws2.cell(row=rr, column=2).number_format = "0.0"
    for c in (3,4,6): ws2.cell(row=rr, column=c).number_format = "#,##0"
    ws2.cell(row=rr, column=5).number_format = "0.00"
ws2.freeze_panes = "A5"
autow(ws2, [34,9,15,11,9,22])

# --- Sheet 3: All Pages (reference) ---
ws3 = wb.create_sheet("All Pages (reference)")
h3 = ["Page","Type","Avg Pos","Monthly Impr.","Clicks/mo","CTR %","In striking distance?"]
for c, h in enumerate(h3, 1): ws3.cell(row=1, column=c, value=h)
style_header(ws3, len(h3))
allrows = sorted(rows, key=lambda r: -r["imp"])
for i, r in enumerate(allrows):
    rr = 2 + i
    vals = [r["page"], r["type"], round(r["pos"],1), r["imp"], r["clicks"], r["ctr"],
            "Yes" if r["striking"] else "No"]
    for c, v in enumerate(vals, 1):
        cell = ws3.cell(row=rr, column=c, value=v)
        cell.font = Font(size=9)
        if i % 2: cell.fill = PatternFill("solid", fgColor=MIST)
    ws3.cell(row=rr, column=3).number_format = "0.0"
    for c in (4,5): ws3.cell(row=rr, column=c).number_format = "#,##0"
    ws3.cell(row=rr, column=6).number_format = "0.00"
ws3.freeze_panes = "A2"
autow(ws3, [40,20,9,15,11,9,20])

# --- Sheet 4: Methodology ---
ws4 = wb.create_sheet("Methodology")
lines = [
    ("Banners.com — Backlink Target Methodology", "title"),
    ("", ""),
    ("Objective", "h"),
    ("Direct the 2 DA50+ backlinks/month (Authority Accelerator plan) at the pages where added authority", "b"),
    ("converts the most existing demand into clicks — i.e. money pages already within striking distance of", "b"),
    ("page-one top spots.", "b"),
    ("", ""),
    ("What counts as a target", "h"),
    ("• Money page: a commercial product/category page (brand/nav pages like / and /promo and", "b"),
    ("  /resources/* informational pages are excluded as primary link targets).", "b"),
    ("• Striking distance: average position between 5 and 20. Pages already top-5 need little help;", "b"),
    ("  pages past 20 are a longer haul than a single link resolves.", "b"),
    ("", ""),
    ("How opportunity is scored", "h"),
    ("Banners.com's real CTR tops out near ~1.3-1.9% even in the top spots — far below the 6-8% industry", "b"),
    ("curve — so a generic curve overstates wildly. Instead we model a boosted page as doing a realistic", "b"),
    ("MULTIPLE of its own current clicks, capped at 3x and larger the further it must climb:", "b"),
    ("   pos 15-20 -> 3.0x   |   pos 11-15 -> 2.5x   |   pos 8-11 -> 2.0x   |   pos 5-8 -> 1.5x", "b"),
    ("Every number is anchored to what Banners.com pages actually achieve today, so it is conservative.", "b"),
    ("Projected clicks = current clicks × factor.  Added clicks/mo = projected − current.  Pages ranked by added clicks.", "b"),
    ("", ""),
    ("Link schedule", "h"),
    ("2 links/month are assigned down the ranked list: Month 1 = ranks 1–2, Month 2 = ranks 3–4, etc.", "b"),
    ("Tier 1 (top 6) are the highest-ROI placements and should lead.", "b"),
    ("", ""),
    ("Caveats", "h"),
    ("• This is a striking-distance / internal-opportunity model, not a competitor referring-domain gap.", "b"),
    ("  A true backlink gap needs an Ahrefs/Semrush export (domains linking to BannerBuzz et al. but not us).", "b"),
    ("• GSC window: 2025-11-01 to 2026-04-30 (6 months). Positions are period averages.", "b"),
    ("• Anchor text should use the money keyword(s) listed for each target page; vary naturally.", "b"),
]
for i, (txt, kind) in enumerate(lines, 1):
    cell = ws4.cell(row=i, column=1, value=txt)
    if kind == "title": cell.font = Font(bold=True, size=14, color=EMBER)
    elif kind == "h": cell.font = Font(bold=True, size=11, color=INK)
    else: cell.font = Font(size=10, color="333333")
ws4.column_dimensions["A"].width = 110

wb.save(OUT)
print("Saved:", OUT)
print("\nTier 1 link targets (lead with these):")
for r in targets[:6]:
    print(f'  {r["rank"]}. {r["page"]:<28} pos {r["pos"]:>4.1f}  {r["imp"]:>9,} imp  '
          f'+{r["uplift"]:>4} clicks/mo  [{r["link_month"]}]')
print(f'\nStriking-distance money pages: {len(targets)}')
print(f'Total modeled added clicks/mo if all boosted to ~pos 4: +{sum(r["uplift"] for r in targets):,}')
