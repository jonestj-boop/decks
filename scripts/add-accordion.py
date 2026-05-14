#!/usr/bin/env python3
"""
Slide 5 overhaul:
- Remove Month 2 Fix Queue (it's covered in the deliverables slide)
- Replace two-col layout with full-width accordion issues table
- Each row expands on click to show what was found + fix approach
"""

DECK = "/Users/deannaspallone/Documents/Claude Projects/embertribe-decks/decks/ceu-matrix-seo-foundation.html"

with open(DECK, "r", encoding="utf-8") as f:
    html = f.read()

# ─────────────────────────────────────────────────────────────
# 1. CSS
# ─────────────────────────────────────────────────────────────
CSS = """
  /* ── Issue accordion ── */
  .issue-row { cursor: pointer; transition: background 0.15s; }
  .issue-row:hover { background: rgba(0,180,216,0.06) !important; }
  .issue-row td { user-select: none; }
  .issue-name-cell { display: flex; align-items: center; justify-content: space-between; }
  .issue-toggle { font-size: 9px; color: rgba(44,62,80,0.32); transition: transform 0.2s ease; flex-shrink: 0; margin-left: 8px; }
  .issue-toggle.open { transform: rotate(90deg); color: var(--ceu-teal); }
  .issue-detail { display: none; }
  .issue-detail.open { display: table-row; }
  .issue-detail > td { padding: 0 !important; border-top: none !important; }
  .issue-detail-inner { padding: 8px 16px 10px 16px; background: rgba(0,180,216,0.05); border-left: 3px solid rgba(0,180,216,0.5); font-size: 12px; color: rgba(44,62,80,0.72); line-height: 1.65; }
  .issue-detail-inner strong { color: rgba(44,62,80,0.88); }
"""

if "issue-accordion" not in html and "issue-row" not in html:
    html = html.replace("</style>", CSS + "\n</style>", 1)
    print("✓ CSS injected")
else:
    print("  CSS already present")

# ─────────────────────────────────────────────────────────────
# 2. Replace entire two-col block (table + fix queue) with
#    full-width accordion table
# ─────────────────────────────────────────────────────────────
OLD_BLOCK = """  <div class="two-col" style="margin-top:16px;">
    <div class="col">
      <table>
        <thead><tr><th class="th-red">Count</th><th class="th-red">Issue</th><th class="th-red">Impact</th><th class="th-red">Fix</th></tr></thead>
        <tbody>
          <tr><td class="bold red">59</td><td>Broken internal links</td><td class="red">High</td><td><span class="pill tech">M2</span></td></tr>
          <tr><td class="bold red">30</td><td>Missing meta descriptions (incl. homepage)</td><td class="red">High</td><td><span class="pill tech">M2</span></td></tr>
          <tr><td class="bold red">19</td><td>Multiple H1 tags per page</td><td class="red">High</td><td><span class="pill tech">M2</span></td></tr>
          <tr><td class="bold orange">58</td><td>Low text-to-HTML ratio (thin content)</td><td class="orange">Med</td><td><span class="pill content">M2–3</span></td></tr>
          <tr><td class="bold orange">31</td><td>Pages with only 1 internal link</td><td class="orange">Med</td><td><span class="pill content">M2–3</span></td></tr>
          <tr><td class="bold orange">6</td><td>Duplicate title tags</td><td class="orange">Med</td><td><span class="pill tech">M2</span></td></tr>
          <tr><td class="bold red">0</td><td>Schema markup / llms.txt</td><td class="red">High</td><td><span class="pill tech">M2</span></td></tr>
        </tbody>
      </table>
    </div>
    <div class="col">
      <h3>Month 2 Fix Queue</h3>
      <table>
        <thead><tr><th>#</th><th>Fix</th><th>Scope</th></tr></thead>
        <tbody>
          <tr><td class="bold">1</td><td>Resolve 59 broken internal links</td><td class="dim">Site-wide</td></tr>
          <tr><td class="bold">2</td><td>Fix 19 duplicate H1 tags</td><td class="dim">19 pages</td></tr>
          <tr><td class="bold">3</td><td>Fix 6 duplicate title tags</td><td class="dim">6 pages</td></tr>
          <tr><td class="bold">4</td><td>Write + implement 30 meta descriptions</td><td class="dim">30 pages</td></tr>
          <tr><td class="bold">5</td><td>WebPage + BreadcrumbList JSON-LD on Ohio pages</td><td class="dim">Ohio hub</td></tr>
          <tr><td class="bold">6</td><td>FAQPage JSON-LD on Ohio FAQ</td><td class="dim">/ohio-faq/</td></tr>
          <tr><td class="bold">7</td><td>Create + publish llms.txt</td><td class="dim">Root</td></tr>
          <tr><td class="bold">8</td><td>Organization schema on homepage</td><td class="dim">Homepage</td></tr>
          <tr><td class="bold">9</td><td>Canonical tags: /course/ vs /product/ credential pairs (4 pairs) + WooCommerce pagination</td><td class="dim">Product + category pages</td></tr>
          <tr><td class="bold">10</td><td>Add missing alt text</td><td class="dim">Site-wide</td></tr>
          <tr><td class="bold">11</td><td>Course schema on credential product pages</td><td class="dim">Product pages</td></tr>
          <tr><td class="bold">12</td><td>HowTo + FAQPage schema on Ohio hub</td><td class="dim">Ohio hub</td></tr>
        </tbody>
      </table>
    </div>
  </div>"""

NEW_BLOCK = """  <table style="margin-top:16px;width:100%;">
    <thead><tr><th class="th-red" style="width:70px;">Count</th><th class="th-red">Issue</th><th class="th-red" style="width:70px;">Impact</th><th class="th-red" style="width:60px;">Fix</th></tr></thead>
    <tbody>
      <tr class="issue-row" onclick="toggleIssue(this)">
        <td class="bold red">59</td>
        <td><div class="issue-name-cell">Broken internal links<span class="issue-toggle">▶</span></div></td>
        <td class="red">High</td><td><span class="pill tech">M2</span></td>
      </tr>
      <tr class="issue-detail"><td colspan="4"><div class="issue-detail-inner">59 broken links found across the site — primarily in product category navigation and WooCommerce migration artifacts (links pointing to <strong>/courses/</strong> pages moved to <strong>/product/</strong>). Fix: redirect map + systematic link repair across all affected pages.</div></td></tr>

      <tr class="issue-row" onclick="toggleIssue(this)">
        <td class="bold orange">58</td>
        <td><div class="issue-name-cell">Low text-to-HTML ratio (thin content)<span class="issue-toggle">▶</span></div></td>
        <td class="orange">Med</td><td><span class="pill content">M2–3</span></td>
      </tr>
      <tr class="issue-detail"><td colspan="4"><div class="issue-detail-inner">58 pages with &lt;15% text-to-HTML ratio — primarily WooCommerce product and category pages with boilerplate copy and little substantive content. Google classifies these as "thin." Fix: content expansion pass starting with the highest-traffic credential product pages.</div></td></tr>

      <tr class="issue-row" onclick="toggleIssue(this)">
        <td class="bold orange">31</td>
        <td><div class="issue-name-cell">Pages with only 1 internal link<span class="issue-toggle">▶</span></div></td>
        <td class="orange">Med</td><td><span class="pill content">M2–3</span></td>
      </tr>
      <tr class="issue-detail"><td colspan="4"><div class="issue-detail-inner">31 pages receive only one inbound internal link, leaving them isolated in the site architecture. Low PageRank flow = harder to rank. Fix: systematic internal linking pass from new hub and article pages so every credential page receives 3+ contextual links.</div></td></tr>

      <tr class="issue-row" onclick="toggleIssue(this)">
        <td class="bold red">30</td>
        <td><div class="issue-name-cell">Missing meta descriptions (incl. homepage)<span class="issue-toggle">▶</span></div></td>
        <td class="red">High</td><td><span class="pill tech">M2</span></td>
      </tr>
      <tr class="issue-detail"><td colspan="4"><div class="issue-detail-inner">30 pages — including the homepage — have no meta description. Google is auto-generating snippets, often pulling non-optimal text from the page body. Fix: write and implement 30 custom meta descriptions, prioritized by traffic and search impression volume.</div></td></tr>

      <tr class="issue-row" onclick="toggleIssue(this)">
        <td class="bold red">19</td>
        <td><div class="issue-name-cell">Multiple H1 tags per page<span class="issue-toggle">▶</span></div></td>
        <td class="red">High</td><td><span class="pill tech">M2</span></td>
      </tr>
      <tr class="issue-detail"><td colspan="4"><div class="issue-detail-inner">19 pages have more than one H1 — a common artifact of WooCommerce themes that inject a second H1 via the product title template, diluting the primary keyword signal Google reads for page topic. Fix: template-level override for WooCommerce pages + manual fix on static pages.</div></td></tr>

      <tr class="issue-row" onclick="toggleIssue(this)">
        <td class="bold orange">6</td>
        <td><div class="issue-name-cell">Duplicate title tags<span class="issue-toggle">▶</span></div></td>
        <td class="orange">Med</td><td><span class="pill tech">M2</span></td>
      </tr>
      <tr class="issue-detail"><td colspan="4"><div class="issue-detail-inner">6 pairs of pages share identical title tags, causing Google to treat them as near-duplicates and suppress one from results. Fix: audit the 6 affected pairs, write unique titles that distinguish each page's primary keyword intent.</div></td></tr>

      <tr class="issue-row" onclick="toggleIssue(this)">
        <td class="bold red">0</td>
        <td><div class="issue-name-cell">Schema markup / llms.txt<span class="issue-toggle">▶</span></div></td>
        <td class="red">High</td><td><span class="pill tech">M2</span></td>
      </tr>
      <tr class="issue-detail"><td colspan="4"><div class="issue-detail-inner">Zero structured data implemented site-wide — no FAQPage, HowTo, BreadcrumbList, Course, or Organization schema. No llms.txt for AI crawler routing (Perplexity, Gemini, ChatGPT). Competitors using schema appear in rich results and AI Overviews; CEU Matrix does not. Fix: implement 8 schema types starting with the Ohio hub + llms.txt at site root.</div></td></tr>
    </tbody>
  </table>"""

if OLD_BLOCK in html:
    html = html.replace(OLD_BLOCK, NEW_BLOCK, 1)
    print("✓ Two-col replaced: fix queue removed, full-width accordion table inserted")
else:
    print("✗ Two-col block not found — check exact whitespace")

# ─────────────────────────────────────────────────────────────
# 3. JS function
# ─────────────────────────────────────────────────────────────
JS = """
  function toggleIssue(row) {
    const detail = row.nextElementSibling;
    const toggle = row.querySelector('.issue-toggle');
    const isOpen = detail.classList.contains('open');
    document.querySelectorAll('.issue-detail.open').forEach(d => d.classList.remove('open'));
    document.querySelectorAll('.issue-toggle.open').forEach(t => t.classList.remove('open'));
    if (!isOpen) {
      detail.classList.add('open');
      toggle.classList.add('open');
    }
  }
"""

if "toggleIssue" not in html:
    html = html.replace("</script>", JS + "\n</script>", 1)
    print("✓ toggleIssue() JS injected")
else:
    print("  toggleIssue() already present")

with open(DECK, "w", encoding="utf-8") as f:
    f.write(html)
print("\nDone — deck saved.")
