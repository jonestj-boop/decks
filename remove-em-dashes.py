#!/usr/bin/env python3
"""
Remove all em dashes from visible text in the deck.
Em dashes used as null table cell values (>—<) are preserved.
Each replacement is explicit to ensure correct grammar.
"""

DECK = "/Users/deannaspallone/Documents/Claude Projects/embertribe-decks/decks/ceu-matrix-seo-foundation.html"

with open(DECK, "r", encoding="utf-8") as f:
    html = f.read()

replacements = [
    # Current state snapshot — traffic donut legend
    ("<strong>Branded</strong> — ~1,260 clicks/mo",
     "<strong>Branded</strong>: ~1,260 clicks/mo"),
    ("<strong>Non-branded</strong> — ~540 clicks/mo",
     "<strong>Non-branded</strong>: ~540 clicks/mo"),

    # Current state — insight callout
    ("The last row — 4 clicks on 1,800 impressions at position 22 — shows the non-branded opportunity hiding in page 2.",
     "The last row (4 clicks on 1,800 impressions at position 22) shows the non-branded opportunity hiding in page 2."),

    # Issues Found bar chart label
    ("HIGH — Not implemented",
     "HIGH: Not implemented"),

    # Accordion detail text
    ("59 broken links found across the site — primarily in product category navigation and WooCommerce migration artifacts",
     "59 broken links found across the site, primarily in product category navigation and WooCommerce migration artifacts"),

    ("58 pages with &lt;15% text-to-HTML ratio — primarily WooCommerce product and category pages",
     "58 pages with &lt;15% text-to-HTML ratio, primarily WooCommerce product and category pages"),

    ("30 pages — including the homepage — have no meta description.",
     "30 pages, including the homepage, have no meta description."),

    ("19 pages have more than one H1 — a common artifact of WooCommerce themes",
     "19 pages have more than one H1, a common artifact of WooCommerce themes"),

    ("Zero structured data implemented site-wide — no FAQPage",
     "Zero structured data implemented site-wide: no FAQPage"),

    # PageSpeed CWV table descriptions
    ("First Contentful Paint — first text/image visible",
     "First Contentful Paint: first text/image visible"),
    ("Largest Contentful Paint — main content loaded",
     "Largest Contentful Paint: main content loaded"),
    ("Cumulative Layout Shift — visual stability",
     "Cumulative Layout Shift: visual stability"),
    ("Total Blocking Time — main thread blocked",
     "Total Blocking Time: main thread blocked"),

    # PageSpeed Key Gap callout
    ("(needs improvement) — driven by unminified CSS/JS",
     "(needs improvement), driven by unminified CSS/JS"),

    # Backlink Gap section divider subtitle
    ("that does not link to CEU Matrix — annotated with DA, relevance, and outreach pathway.",
     "that does not link to CEU Matrix, annotated with DA, relevance, and outreach pathway."),

    # Backlink Gap slide subtitle
    ("Relevance is pre-qualified — acquisition rate 3x higher than cold prospecting.",
     "Relevance is pre-qualified; acquisition rate is 3x higher than cold prospecting."),

    # Pathway legend descriptions
    ("<span class=\"dim\"> — CEU Matrix holds a credential",
     "<span class=\"dim\">: CEU Matrix holds a credential"),
    ("<span class=\"dim\"> — state licensing board or certification org",
     "<span class=\"dim\">: state licensing board or certification org"),
    ("<span class=\"dim\"> — general resource or licensing guide site",
     "<span class=\"dim\">: general resource or licensing guide site"),
    ("<span class=\"dim\"> — editorial or content site",
     "<span class=\"dim\">: editorial or content site"),

    # Competitor analysis callout
    ("from our keyword bank — CASR dominates",
     "from our keyword bank; CASR dominates"),

    # Month-by-month plan table cells
    ("AI crawler routing — currently zero on site",
     "AI crawler routing (currently zero on site)"),
    ("Refresh title, H1, meta — currently ranks top 10",
     "Refresh title, H1, meta; currently ranks top 10"),
    ("Bidirectional — hub links down, credentials link back up",
     "Bidirectional: hub links down, credentials link back up"),
    ("Bidirectional — hub links down, credential pages link back up",
     "Bidirectional: hub links down, credential pages link back up"),
    ("Expand content depth — CSAC and LCAS",
     "Expand content depth; CSAC and LCAS"),
    ("Enforce bidirectional internal linking — hub links down, credential pages link back up",
     "Enforce bidirectional internal linking: hub links down, credential pages link back up"),
    ("OCDP Provider #50-19236 citation pass — cited prominently",
     "OCDP Provider #50-19236 citation pass, cited prominently"),
    ("NAADAC Provider #94564 citation pass — all relevant",
     "NAADAC Provider #94564 citation pass covering all relevant"),
    ("Criminal Justice hub — build topical cluster",
     "Criminal Justice hub to build topical cluster"),
    ("Cross-link pass back to Ohio hub — enforce bidirectional linking",
     "Cross-link pass back to Ohio hub, enforcing bidirectional linking"),
    ("Resolve remaining duplicate titles from audit — unique, keyword-targeted titles for each",
     "Resolve remaining duplicate titles from audit; write unique, keyword-targeted titles for each"),
    ("Preserves link equity — temporary redirects bleed authority",
     "Preserves link equity; temporary redirects bleed authority"),
    ("Content depth expansion to 4,000+ words — exam prep tips",
     "Content depth expansion to 4,000+ words: exam prep tips"),
    ("Optimize for featured snippets — direct-answer openings",
     "Optimize for featured snippets: direct-answer openings"),
    ("Enforce bidirectional linking — hub links down, credential pages link back up",
     "Enforce bidirectional linking: hub links down, credential pages link back up"),
    ("Bidirectional linking pass — enforce hub architecture consistency",
     "Bidirectional linking pass to enforce hub architecture consistency"),
    ("Content depth review vs. CASR — expand any pages",
     "Content depth review vs. CASR; expand any pages"),
    ("All pages — national board covering multi-state credential holders",
     "All pages (national board covering multi-state credential holders)"),

    # Article title in month plan
    ("CSAC vs LCAS — Which Path is Right?",
     "CSAC vs LCAS: Which Path is Right?"),

    # M4 table
    ("North Carolina hub (existing)</td><td>Expand content depth — CSAC",
     "North Carolina hub (existing)</td><td>Expand content depth; CSAC"),
    ("Ohio hub to Ohio credential pages</td><td>Enforce bidirectional internal linking — hub links down",
     "Ohio hub to Ohio credential pages</td><td>Enforce bidirectional internal linking: hub links down"),
]

count = 0
for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        count += 1
    else:
        print(f"  WARNING: not found — {old[:60]!r}")

print(f"\nApplied {count}/{len(replacements)} replacements")

# Final check: count remaining em dashes in visible text (skip null cells and HTML comments)
remaining = []
for i, line in enumerate(html.splitlines(), 1):
    if "—" in line:
        # skip null table cells and HTML comments
        stripped = line.strip()
        if stripped in (">—</td>", "<td class=\"dim\">—</td>") or stripped.startswith("<!--"):
            continue
        remaining.append(f"  Line {i}: {stripped[:100]}")

if remaining:
    print(f"\nRemaining em dashes in non-null/non-comment lines ({len(remaining)}):")
    for r in remaining:
        print(r)
else:
    print("No remaining em dashes in visible text.")

with open(DECK, "w", encoding="utf-8") as f:
    f.write(html)
print("\nDone — deck saved.")
