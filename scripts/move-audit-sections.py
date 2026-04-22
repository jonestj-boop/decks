#!/usr/bin/env python3
"""
Restructure: move Backlink Gap + Competitor Analysis to right after Technical Audit.
New order: Technical Audit → Backlink Gap → Competitor Analysis → Keyword Strategy → ...
Also: change "SEO Foundation Deliverable" → "Section" on both divider labels.
"""

DECK = "/Users/deannaspallone/Documents/Claude Projects/embertribe-decks/decks/ceu-matrix-seo-foundation.html"

with open(DECK, "r", encoding="utf-8") as f:
    html = f.read()

# ─── Markers ───────────────────────────────────────────────────────────────
COMP_START   = "\n\n<!-- Competitor Analysis — Section Divider -->"
BL_START     = "\n\n<!-- Backlink Gap — Section Divider -->"
AFTER_BL     = "\n\n<!-- 14: Section divider: Authority & AI -->"
INSERT_AFTER = "\n\n<!-- 6: Section divider: Keyword Strategy -->"

# Verify all markers exist
for name, marker in [("Comp start", COMP_START), ("BL start", BL_START),
                     ("After BL", AFTER_BL), ("Insert after", INSERT_AFTER)]:
    if marker not in html:
        print(f"✗ Marker not found: {name!r}")
        exit(1)
    else:
        print(f"  ✓ Found: {name}")

# ─── Extract Competitor Analysis block ────────────────────────────────────
comp_start_idx = html.index(COMP_START)
bl_start_idx   = html.index(BL_START)

# Competitor Analysis = from COMP_START up to (but not including) BL_START
comp_block = html[comp_start_idx : bl_start_idx]
print(f"  Extracted Competitor Analysis block ({len(comp_block)} chars)")

# ─── Extract Backlink Gap block ────────────────────────────────────────────
after_bl_idx = html.index(AFTER_BL)

# Backlink Gap = from BL_START up to (but not including) AFTER_BL
bl_block = html[bl_start_idx : after_bl_idx]
print(f"  Extracted Backlink Gap block ({len(bl_block)} chars)")

# ─── Remove both blocks from current location ─────────────────────────────
html = html[:comp_start_idx] + html[after_bl_idx:]
print("  ✓ Removed both blocks from current location (after Month-by-Month Plan)")

# ─── Insert after Issues Found, before Keyword Strategy ───────────────────
insert_idx = html.index(INSERT_AFTER)

# New order: Backlink Gap first, Competitor Analysis second
both_blocks = bl_block + comp_block
html = html[:insert_idx] + both_blocks + html[insert_idx:]
print("  ✓ Inserted: Backlink Gap → Competitor Analysis, before Keyword Strategy divider")

# ─── Change "SEO Foundation Deliverable" → "Section" on both dividers ─────
old_label = '<div class="slide-label">SEO Foundation Deliverable</div>'
new_label = '<div class="slide-label">Section</div>'

count = html.count(old_label)
html = html.replace(old_label, new_label)
print(f"  ✓ Updated {count} divider label(s): 'SEO Foundation Deliverable' → 'Section'")

with open(DECK, "w", encoding="utf-8") as f:
    f.write(html)
print("\nDone — deck saved.")
