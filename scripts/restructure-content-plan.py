#!/usr/bin/env python3
"""
Two changes to the deck:
1. Remove Competitor Analysis / Backlink Gap two-col boxes from Month 1 slide
   (those are now their own sections)
2. Move Month-by-Month Content Plan slide (Content Engine) from after Backlink Gap
   to right after the Month 1 slide, within the Content Strategy section
"""

DECK = "/Users/deannaspallone/Documents/Claude Projects/embertribe-decks/decks/ceu-matrix-seo-foundation.html"

with open(DECK, "r", encoding="utf-8") as f:
    html = f.read()

# ─────────────────────────────────────────────────────────────────────────────
# 1. Remove the two-col Competitor/Backlink boxes from Month 1 slide
# ─────────────────────────────────────────────────────────────────────────────
OLD_TWO_COL = """  <div class="two-col" style="margin-bottom:16px;">
    <div style="background:#FFF8E1;border-left:3px solid var(--ember-red);border-radius:0 8px 8px 0;padding:14px 16px;">
      <div class="bold" style="font-size:13px;color:var(--ceu-navy);margin-bottom:4px;">Competitor Analysis Report</div>
      <div style="font-size:12px;color:var(--text-light);line-height:1.6;">Keyword gap, backlink gap, and content gap vs. CASR + 4 other competitors. Identifies every search term CASR ranks for where CEU Matrix does not, every domain linking to CASR but not CEU Matrix, and content types CEU Matrix is missing entirely. Basis for all outreach and content prioritization in M2+.</div>
    </div>
    <div style="background:#FFF8E1;border-left:3px solid var(--ember-red);border-radius:0 8px 8px 0;padding:14px 16px;">
      <div class="bold" style="font-size:13px;color:var(--ceu-navy);margin-bottom:4px;">Backlink Gap Report</div>
      <div style="font-size:12px;color:var(--text-light);line-height:1.6;">Full list of every domain linking to CASR, CE4Less, or Sober College that does not link to CEU Matrix. Each domain annotated with DA, relevance, and outreach pathway (state board directory, NAADAC affiliate, CJ org, etc.). This is the outreach hit list that drives the 6 links/month acquisition in M2–M4.</div>
    </div>
  </div>

  <table>"""

NEW_TWO_COL = """  <table>"""

if OLD_TWO_COL in html:
    html = html.replace(OLD_TWO_COL, NEW_TWO_COL, 1)
    print("✓ Two-col Competitor/Backlink boxes removed from Month 1 slide")
else:
    print("✗ Two-col block not found — check whitespace")

# ─────────────────────────────────────────────────────────────────────────────
# 2. Cut the Content Engine slide from its current position (after Backlink Gap)
#    and paste it right after the Month 1 slide
# ─────────────────────────────────────────────────────────────────────────────

CONTENT_ENGINE_BLOCK = """<!-- 14: Content Engine by Month (tabbed) -->
<div class="slide">
  <div class="slide-label">Content Engine</div>
  <h2>Month-by-Month Content Plan</h2>"""

# The block to remove from its current location (after Backlink Gap content):
# It currently sits between the Backlink Gap closing </div> and the Authority & AI divider
OLD_LOCATION_ANCHOR = """\n\n<!-- 14: Content Engine by Month (tabbed) -->"""
NEW_LOCATION_ANCHOR = ""  # just remove it from the old spot

# First verify the Content Engine block exists in html
if CONTENT_ENGINE_BLOCK not in html:
    print("✗ Content Engine block not found at original location")
else:
    # Extract the entire Content Engine slide block
    # Find start marker
    start_marker = "\n\n<!-- 14: Content Engine by Month (tabbed) -->\n"
    end_marker = "\n\n<!-- 14: Section divider: Authority & AI -->"

    start_idx = html.find(start_marker)
    end_idx   = html.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        print(f"✗ Could not find boundaries: start={start_idx}, end={end_idx}")
    else:
        content_engine_block = html[start_idx:end_idx]  # includes the leading \n\n
        print(f"  Content Engine block extracted ({len(content_engine_block)} chars)")

        # Remove from current location
        html = html[:start_idx] + html[end_idx:]
        print("  ✓ Removed from after Backlink Gap")

        # Insert right after Month 1 slide (before Competitor Analysis section divider)
        insert_marker = "\n\n<!-- Competitor Analysis — Section Divider -->"
        insert_idx = html.find(insert_marker)

        if insert_idx == -1:
            print("✗ Insert marker (Competitor Analysis divider) not found")
        else:
            html = html[:insert_idx] + content_engine_block + html[insert_idx:]
            print("  ✓ Inserted after Month 1 slide, before Competitor Analysis section")

with open(DECK, "w", encoding="utf-8") as f:
    f.write(html)
print("\nDone — deck saved.")
