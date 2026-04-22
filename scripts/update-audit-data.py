#!/usr/bin/env python3
"""
Update Issues Found slide with real crawl data from ceu-matrix-full-audit.json.
Updates: bar chart numbers + widths, accordion row counts, accordion detail URL lists.

Real findings:
  Broken links:       20 instances, 4 unique broken URLs
  Thin content:       199 pages (site-wide; full course/product catalog)
  Single inbound:     83 pages
  Missing meta:       122 pages
  Multiple H1:        81 pages
  Duplicate titles:   1 pair
  Schema / llms.txt:  0 custom schema, no llms.txt
"""

import json

DECK  = "/Users/deannaspallone/Documents/Claude Projects/embertribe-decks/decks/ceu-matrix-seo-foundation.html"
AUDIT = "/Users/deannaspallone/Documents/Claude Projects/embertribe-decks/ceu-matrix-full-audit.json"

with open(DECK, "r", encoding="utf-8") as f:
    html = f.read()

with open(AUDIT) as f:
    data = json.load(f)

# ── helpers ─────────────────────────────────────────────────────────────────

def url_list_html(urls, cols=2):
    """Compact two-column URL list."""
    items = "".join(
        f'<span style="font-family:monospace;font-size:11px;color:rgba(44,62,80,0.75);'
        f'display:inline-block;width:48%;white-space:nowrap;overflow:hidden;'
        f'text-overflow:ellipsis;">{u}</span>'
        for u in urls
    )
    return (
        f'<div style="max-height:130px;overflow-y:auto;padding:4px 0;'
        f'border-top:1px solid rgba(44,62,80,0.1);margin-top:6px;">'
        + items + '</div>'
    )

# ── Bar chart replacements ───────────────────────────────────────────────────
# Scale: max value 199 maps to bar width 438. width = round(val/200*440), min 5.
# Text outside bar except row 1 (199 thin) which puts number inside.

BAR_REPLACEMENTS = [
    # Row 0: Broken links 59 → 20
    (
        '    <!-- Row 0: Broken links 59 (HIGH) -->\n'
        '    <text x="153" y="16" text-anchor="end" fill="rgba(44,62,80,0.75)" font-size="12">Broken internal links</text>\n'
        '    <rect x="160" y="3" width="299" height="17" rx="2.5" fill="rgba(231,76,60,0.8)"/>\n'
        '    <text x="467" y="16" fill="#c0392b" font-size="12" font-weight="700">59</text>\n'
        '    <text x="490" y="16" fill="rgba(44,62,80,0.42)" font-size="10.5">HIGH</text>',

        '    <!-- Row 0: Broken links 20 (HIGH) -->\n'
        '    <text x="153" y="16" text-anchor="end" fill="rgba(44,62,80,0.75)" font-size="12">Broken internal links</text>\n'
        '    <rect x="160" y="3" width="44" height="17" rx="2.5" fill="rgba(231,76,60,0.8)"/>\n'
        '    <text x="212" y="16" fill="#c0392b" font-size="12" font-weight="700">20</text>\n'
        '    <text x="234" y="16" fill="rgba(44,62,80,0.42)" font-size="10.5">HIGH</text>',
    ),
    # Row 1: Thin content 58 → 199 (full-width bar, text inside)
    (
        '    <!-- Row 1: Thin content 58 (MED) -->\n'
        '    <text x="153" y="40" text-anchor="end" fill="rgba(44,62,80,0.75)" font-size="12">Thin content pages</text>\n'
        '    <rect x="160" y="27" width="294" height="17" rx="2.5" fill="rgba(243,156,18,0.7)"/>\n'
        '    <text x="462" y="40" fill="#d68910" font-size="12" font-weight="700">58</text>\n'
        '    <text x="485" y="40" fill="rgba(44,62,80,0.42)" font-size="10.5">MED</text>',

        '    <!-- Row 1: Thin content 199 (MED, site-wide) -->\n'
        '    <text x="153" y="40" text-anchor="end" fill="rgba(44,62,80,0.75)" font-size="12">Thin content pages</text>\n'
        '    <rect x="160" y="27" width="438" height="17" rx="2.5" fill="rgba(243,156,18,0.7)"/>\n'
        '    <text x="594" y="40" text-anchor="end" fill="white" font-size="12" font-weight="700">199</text>\n'
        '    <text x="602" y="40" fill="rgba(44,62,80,0.42)" font-size="10.5">MED</text>',
    ),
    # Row 2: Single-link pages 31 → 83
    (
        '    <!-- Row 2: Single-link pages 31 (MED) -->\n'
        '    <text x="153" y="64" text-anchor="end" fill="rgba(44,62,80,0.75)" font-size="12">Pages w/ 1 internal link</text>\n'
        '    <rect x="160" y="51" width="157" height="17" rx="2.5" fill="rgba(243,156,18,0.7)"/>\n'
        '    <text x="325" y="64" fill="#d68910" font-size="12" font-weight="700">31</text>\n'
        '    <text x="348" y="64" fill="rgba(44,62,80,0.42)" font-size="10.5">MED</text>',

        '    <!-- Row 2: Single-link pages 83 (MED) -->\n'
        '    <text x="153" y="64" text-anchor="end" fill="rgba(44,62,80,0.75)" font-size="12">Pages w/ 1 internal link</text>\n'
        '    <rect x="160" y="51" width="183" height="17" rx="2.5" fill="rgba(243,156,18,0.7)"/>\n'
        '    <text x="351" y="64" fill="#d68910" font-size="12" font-weight="700">83</text>\n'
        '    <text x="373" y="64" fill="rgba(44,62,80,0.42)" font-size="10.5">MED</text>',
    ),
    # Row 3: Missing meta 30 → 122
    (
        '    <!-- Row 3: Missing meta 30 (HIGH) -->\n'
        '    <text x="153" y="88" text-anchor="end" fill="rgba(44,62,80,0.75)" font-size="12">Missing meta descriptions</text>\n'
        '    <rect x="160" y="75" width="152" height="17" rx="2.5" fill="rgba(231,76,60,0.8)"/>\n'
        '    <text x="320" y="88" fill="#c0392b" font-size="12" font-weight="700">30</text>\n'
        '    <text x="343" y="88" fill="rgba(44,62,80,0.42)" font-size="10.5">HIGH</text>',

        '    <!-- Row 3: Missing meta 122 (HIGH) -->\n'
        '    <text x="153" y="88" text-anchor="end" fill="rgba(44,62,80,0.75)" font-size="12">Missing meta descriptions</text>\n'
        '    <rect x="160" y="75" width="268" height="17" rx="2.5" fill="rgba(231,76,60,0.8)"/>\n'
        '    <text x="436" y="88" fill="#c0392b" font-size="12" font-weight="700">122</text>\n'
        '    <text x="465" y="88" fill="rgba(44,62,80,0.42)" font-size="10.5">HIGH</text>',
    ),
    # Row 4: Multiple H1 19 → 81
    (
        '    <!-- Row 4: Multiple H1 19 (HIGH) -->\n'
        '    <text x="153" y="112" text-anchor="end" fill="rgba(44,62,80,0.75)" font-size="12">Multiple H1 tags</text>\n'
        '    <rect x="160" y="99" width="96" height="17" rx="2.5" fill="rgba(231,76,60,0.8)"/>\n'
        '    <text x="264" y="112" fill="#c0392b" font-size="12" font-weight="700">19</text>\n'
        '    <text x="287" y="112" fill="rgba(44,62,80,0.42)" font-size="10.5">HIGH</text>',

        '    <!-- Row 4: Multiple H1 81 (HIGH) -->\n'
        '    <text x="153" y="112" text-anchor="end" fill="rgba(44,62,80,0.75)" font-size="12">Multiple H1 tags</text>\n'
        '    <rect x="160" y="99" width="178" height="17" rx="2.5" fill="rgba(231,76,60,0.8)"/>\n'
        '    <text x="346" y="112" fill="#c0392b" font-size="12" font-weight="700">81</text>\n'
        '    <text x="368" y="112" fill="rgba(44,62,80,0.42)" font-size="10.5">HIGH</text>',
    ),
    # Row 5: Duplicate titles 6 → 1
    (
        '    <!-- Row 5: Duplicate titles 6 (MED) -->\n'
        '    <text x="153" y="136" text-anchor="end" fill="rgba(44,62,80,0.75)" font-size="12">Duplicate title tags</text>\n'
        '    <rect x="160" y="123" width="30" height="17" rx="2.5" fill="rgba(243,156,18,0.7)"/>\n'
        '    <text x="198" y="136" fill="#d68910" font-size="12" font-weight="700">6</text>\n'
        '    <text x="221" y="136" fill="rgba(44,62,80,0.42)" font-size="10.5">MED</text>',

        '    <!-- Row 5: Duplicate titles 1 (MED) -->\n'
        '    <text x="153" y="136" text-anchor="end" fill="rgba(44,62,80,0.75)" font-size="12">Duplicate title tags</text>\n'
        '    <rect x="160" y="123" width="8" height="17" rx="2.5" fill="rgba(243,156,18,0.7)"/>\n'
        '    <text x="176" y="136" fill="#d68910" font-size="12" font-weight="700">1</text>\n'
        '    <text x="190" y="136" fill="rgba(44,62,80,0.42)" font-size="10.5">MED</text>',
    ),
]

for old, new in BAR_REPLACEMENTS:
    if old in html:
        html = html.replace(old, new, 1)
        print(f"  Updated bar chart row")
    else:
        print(f"  WARNING: bar row not found — {old[:60]!r}")

# ── Accordion row counts + detail text ──────────────────────────────────────

# 1. Broken links: 59 → 20
# Unique broken URLs with source counts
from collections import Counter
broken_url_counts = Counter(b['broken_url'] for b in data['broken_links'])
broken_rows = ""
for url, count in broken_url_counts.most_common():
    sources = [b['source_page'] for b in data['broken_links'] if b['broken_url'] == url]
    status  = next(b['status_code'] for b in data['broken_links'] if b['broken_url'] == url)
    broken_rows += (
        f'<div style="padding:4px 0;border-top:1px solid rgba(44,62,80,0.08);">'
        f'<span style="font-family:monospace;font-size:11.5px;color:#c0392b;">{url}</span>'
        f' <span style="font-size:11px;color:rgba(44,62,80,0.5);">({status}) — linked from {count} page{"s" if count>1 else ""}</span>'
        f'</div>'
    )

broken_detail = (
    f'<b>4 unique broken URLs across 20 internal link instances.</b> The dominant issue is '
    f'<code style="font-size:11px;">/product-category/available-courses</code> returning 404 on 17 product pages — '
    f'a WooCommerce category archive removed during migration. Fix: create a redirect from '
    f'/product-category/available-courses to /courses-we-offer + fix the remaining 3 URLs.'
    + broken_rows
)

html = html.replace(
    '        <td class="bold red">59</td>\n'
    '        <td><div class="issue-name-cell">Broken internal links<span class="issue-toggle">▶</span></div></td>',
    '        <td class="bold red">20</td>\n'
    '        <td><div class="issue-name-cell">Broken internal links<span class="issue-toggle">▶</span></div></td>',
    1
)
html = html.replace(
    '      <tr class="issue-detail"><td colspan="4"><div class="issue-detail-inner">59 broken links found across the site, primarily in product category navigation and WooCommerce migration artifacts (links pointing to <strong>/courses/</strong> pages moved to <strong>/product/</strong>). Fix: redirect map + systematic link repair across all affected pages.</div></td></tr>',
    f'      <tr class="issue-detail"><td colspan="4"><div class="issue-detail-inner">{broken_detail}</div></td></tr>',
    1
)
print("  Updated broken links row")

# 2. Thin content: 58 → 199
thin_urls = [p['url'] for p in data['thin_content']]
thin_list  = url_list_html(thin_urls)
thin_detail = (
    f'<b>199 pages have a text-to-HTML ratio below 15% — effectively the entire crawled site.</b> '
    f'WooCommerce course and product pages account for the majority; they carry large HTML templates '
    f'with minimal visible text. Google can render the JS content but the thin HTML is still a '
    f'ranking disadvantage. Priority fix: content expansion on the highest-traffic credential and '
    f'state pages, starting with Ohio, Texas, and Pennsylvania hub pages in M2.'
    + thin_list
)
html = html.replace(
    '        <td class="bold orange">58</td>\n'
    '        <td><div class="issue-name-cell">Low text-to-HTML ratio (thin content)<span class="issue-toggle">▶</span></div></td>',
    '        <td class="bold orange">199</td>\n'
    '        <td><div class="issue-name-cell">Low text-to-HTML ratio (thin content)<span class="issue-toggle">▶</span></div></td>',
    1
)
html = html.replace(
    '      <tr class="issue-detail"><td colspan="4"><div class="issue-detail-inner">58 pages with &lt;15% text-to-HTML ratio, primarily WooCommerce product and category pages with boilerplate copy and little substantive content. Google classifies these as "thin." Fix: content expansion pass starting with the highest-traffic credential product pages.</div></td></tr>',
    f'      <tr class="issue-detail"><td colspan="4"><div class="issue-detail-inner">{thin_detail}</div></td></tr>',
    1
)
print("  Updated thin content row")

# 3. Single inbound link: 31 → 83
single_urls = [p['url'] for p in data['single_inbound_link']]
single_list  = url_list_html(single_urls)
single_detail = (
    f'<b>83 pages receive only 1 inbound internal link</b>, leaving them isolated in the site architecture. '
    f'Low internal PageRank flow makes these pages significantly harder to rank regardless of content quality. '
    f'Fix: systematic internal linking pass — every credential and state page should receive 3+ contextual links from hub pages and new articles.'
    + single_list
)
html = html.replace(
    '        <td class="bold orange">31</td>\n'
    '        <td><div class="issue-name-cell">Pages with only 1 internal link<span class="issue-toggle">▶</span></div></td>',
    '        <td class="bold orange">83</td>\n'
    '        <td><div class="issue-name-cell">Pages with only 1 internal link<span class="issue-toggle">▶</span></div></td>',
    1
)
html = html.replace(
    '      <tr class="issue-detail"><td colspan="4"><div class="issue-detail-inner">31 pages receive only one inbound internal link, leaving them isolated in the site architecture. Low PageRank flow = harder to rank. Fix: systematic internal linking pass from new hub and article pages so every credential page receives 3+ contextual links.</div></td></tr>',
    f'      <tr class="issue-detail"><td colspan="4"><div class="issue-detail-inner">{single_detail}</div></td></tr>',
    1
)
print("  Updated single inbound link row")

# 4. Missing meta: 30 → 122
meta_urls  = [p['url'] for p in data['missing_meta']]
meta_list   = url_list_html(meta_urls)
meta_detail = (
    f'<b>122 pages have no meta description</b> — Google is auto-generating snippets, often pulling '
    f'non-optimal text from the page body. Covers blog articles, course pages, product pages, and state pages. '
    f'Fix: write and implement custom meta descriptions starting with the highest-traffic pages; '
    f'use a WooCommerce template for bulk course/product page coverage.'
    + meta_list
)
html = html.replace(
    '        <td class="bold red">30</td>\n'
    '        <td><div class="issue-name-cell">Missing meta descriptions (incl. homepage)<span class="issue-toggle">▶</span></div></td>',
    '        <td class="bold red">122</td>\n'
    '        <td><div class="issue-name-cell">Missing meta descriptions (incl. homepage)<span class="issue-toggle">▶</span></div></td>',
    1
)
html = html.replace(
    '      <tr class="issue-detail"><td colspan="4"><div class="issue-detail-inner">30 pages, including the homepage, have no meta description. Google is auto-generating snippets, often pulling non-optimal text from the page body. Fix: write and implement 30 custom meta descriptions, prioritized by traffic and search impression volume.</div></td></tr>',
    f'      <tr class="issue-detail"><td colspan="4"><div class="issue-detail-inner">{meta_detail}</div></td></tr>',
    1
)
print("  Updated missing meta row")

# 5. Multiple H1: 19 → 81
h1_urls  = [p['url'] for p in data['multiple_h1']]
h1_list   = url_list_html(h1_urls)
h1_detail = (
    f'<b>81 pages have more than one H1 tag</b> — all on /course/ pages, a WooCommerce theme artifact '
    f'where the course title template injects a second H1 alongside the page H1. '
    f'This dilutes the primary keyword signal Google reads for page topic. '
    f'Fix: a single WooCommerce template override eliminates all 81 instances at once.'
    + h1_list
)
html = html.replace(
    '        <td class="bold red">19</td>\n'
    '        <td><div class="issue-name-cell">Multiple H1 tags per page<span class="issue-toggle">▶</span></div></td>',
    '        <td class="bold red">81</td>\n'
    '        <td><div class="issue-name-cell">Multiple H1 tags per page<span class="issue-toggle">▶</span></div></td>',
    1
)
html = html.replace(
    '      <tr class="issue-detail"><td colspan="4"><div class="issue-detail-inner">19 pages have more than one H1, a common artifact of WooCommerce themes that inject a second H1 via the product title template, diluting the primary keyword signal Google reads for page topic. Fix: template-level override for WooCommerce pages + manual fix on static pages.</div></td></tr>',
    f'      <tr class="issue-detail"><td colspan="4"><div class="issue-detail-inner">{h1_detail}</div></td></tr>',
    1
)
print("  Updated multiple H1 row")

# 6. Duplicate titles: 6 → 1
dup = data['duplicate_titles'][0]
dup_detail = (
    f'<b>1 duplicate title tag pair found.</b> Two pages share the title '
    f'"<em>{dup["title"]}</em>":<br>'
    + "".join(
        f'<span style="font-family:monospace;font-size:11.5px;display:block;margin-top:4px;">{u}</span>'
        for u in dup['urls']
    )
    + '<br>Fix: rename /courses-we-offer title to distinguish it from the archive page — e.g., '
    '"Online Addiction Counselor Courses | CEU Matrix".'
)
html = html.replace(
    '        <td class="bold orange">6</td>\n'
    '        <td><div class="issue-name-cell">Duplicate title tags<span class="issue-toggle">▶</span></div></td>',
    '        <td class="bold orange">1</td>\n'
    '        <td><div class="issue-name-cell">Duplicate title tags<span class="issue-toggle">▶</span></div></td>',
    1
)
html = html.replace(
    '      <tr class="issue-detail"><td colspan="4"><div class="issue-detail-inner">6 pairs of pages share identical title tags, causing Google to treat them as near-duplicates and suppress one from results. Fix: audit the 6 affected pairs, write unique titles that distinguish each page\'s primary keyword intent.</div></td></tr>',
    f'      <tr class="issue-detail"><td colspan="4"><div class="issue-detail-inner">{dup_detail}</div></td></tr>',
    1
)
print("  Updated duplicate titles row")

# ── Save ─────────────────────────────────────────────────────────────────────
with open(DECK, "w", encoding="utf-8") as f:
    f.write(html)
print("\nDone — deck saved.")
