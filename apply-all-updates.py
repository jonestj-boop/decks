#!/usr/bin/env python3
"""
Single-pass update applying:
  1. Baseline slide: correct Oct GA4 value (1,679→4,064), fix +265%→+51%,
     update impressions (~50K→~84K), branded % (70%→66%), click legend,
     top queries table, annotation text
  2. Intake-based fixes: hack/spam context, migration context, Q3 alignment,
     CE/CEU keyword note, subscription timing note, 20-year authority reframe
  3. Backlink gap reframe: delivery commitment → opportunity map + guest posts
"""

DECK = "/Users/deannaspallone/Documents/Claude Projects/embertribe-decks/decks/ceu-matrix-seo-foundation.html"

with open(DECK, "r", encoding="utf-8") as f:
    html = f.read()

fixes = []

# ────────────────────────────────────────────────────────
# 1. BASELINE SLIDE — correct GA4 data
# ────────────────────────────────────────────────────────

# 1a. Impressions stat card: ~50K → ~84K
fixes.append((
    '<div class="stat-card"><div class="stat-value orange">~50K</div><div class="stat-label">Monthly Google impressions</div></div>',
    '<div class="stat-card"><div class="stat-value orange">~84K</div><div class="stat-label">Monthly Google impressions (Mar 2026, GSC)</div></div>'
))

# 1b. Branded stat card: ~70% → ~66%
fixes.append((
    '<div class="stat-card"><div class="stat-value red">~70%</div><div class="stat-label">Traffic that is branded</div></div>',
    '<div class="stat-card"><div class="stat-value red">~66%</div><div class="stat-label">Traffic that is branded (GSC, Feb–Apr 2026)</div></div>'
))

# 1c. Chart comment + Oct value: 1,679 → 4,064, y=84 → y=44
# SVG y = 112 - (value/6128)*102
# Oct 4,064: y = 112 - (4064/6128)*102 = 44
fixes.append((
    '''        <!-- area fill: points scaled to 0–102px height (max=6128)
             y = 112 - (value/6128)*102
             Oct:1679→84  Nov:3936→47  Dec:4836→32  Jan:5795→17  Feb:5662→19  Mar:6128→10 -->''',
    '''        <!-- area fill: points scaled to 0–102px height (max=6128)
             y = 112 - (value/6128)*102
             Oct:4064→44  Nov:3936→47  Dec:4836→32  Jan:5795→16  Feb:5662→18  Mar:6128→10 -->'''
))

# 1d. SVG area fill path — update Oct point from (55,84) to (55,44)
fixes.append((
    '<path d="M55,84 L103,47 L151,32 L199,17 L247,19 L295,10 L295,112 L55,112 Z" fill="url(#areaGrad)"/>',
    '<path d="M55,44 L103,47 L151,32 L199,16 L247,18 L295,10 L295,112 L55,112 Z" fill="url(#areaGrad)"/>'
))

# 1e. SVG polyline — update Oct point
fixes.append((
    '<polyline points="55,84 103,47 151,32 199,17 247,19 295,10" fill="none" stroke="#27AE60" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>',
    '<polyline points="55,44 103,47 151,32 199,16 247,18 295,10" fill="none" stroke="#27AE60" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>'
))

# 1f. Oct dot y position: cy=84 → cy=44
fixes.append((
    '<circle cx="55"  cy="84" r="4" fill="#ffffff" stroke="#e67e22" stroke-width="2"/>',
    '<circle cx="55"  cy="44" r="4" fill="#ffffff" stroke="#e67e22" stroke-width="2"/>'
))

# 1g. Oct data label: value 1,679 at y=78 → 4,064 at y=38
fixes.append((
    '<text x="55"  y="78"  text-anchor="middle" font-size="8" fill="#7f8c8d">1,679</text>',
    '<text x="55"  y="38"  text-anchor="middle" font-size="8" fill="#7f8c8d">4,064</text>'
))

# 1h. Jan label y=11 → y=10
fixes.append((
    '<text x="199" y="11"  text-anchor="middle" font-size="8" fill="#27AE60">5,795</text>',
    '<text x="199" y="10"  text-anchor="middle" font-size="8" fill="#27AE60">5,795</text>'
))

# 1i. Feb label y=13 → y=12
fixes.append((
    '<text x="247" y="13"  text-anchor="middle" font-size="8" fill="#27AE60">5,662</text>',
    '<text x="247" y="12"  text-anchor="middle" font-size="8" fill="#27AE60">5,662</text>'
))

# 1j. Remove +265% badge, replace with +51%
fixes.append((
    '        <!-- +265% badge -->\n        <rect x="234" y="130" width="72" height="16" rx="8" fill="#E8F5E9"/>\n        <text x="270" y="141" text-anchor="middle" font-size="9" fill="#27AE60" font-weight="700">+265% YTD</text>',
    '        <!-- +51% Oct→Mar badge -->\n        <rect x="234" y="130" width="72" height="16" rx="8" fill="#E8F5E9"/>\n        <text x="270" y="141" text-anchor="middle" font-size="9" fill="#27AE60" font-weight="700">+51% Oct→Mar</text>'
))

# 1k. Annotation text under chart
fixes.append((
    '<strong>Traffic grew 3.6x in 5 months.</strong> Branded searches are driving most of it. Non-branded is the growth engine this Foundation builds.',
    '<strong>New site migration (Feb 2026) drove a traffic bump; April is normalizing.</strong> The underlying trend is flat-to-declining since May 2025. Non-branded organic is the growth engine this Foundation builds.'
))

# 1l. Donut chart: 70% → 66%, update SVG values
# Circumference r=38: 2*pi*38 = 238.8
# Branded 66%: 238.8*0.66 = 157.6; Non-branded 34%: 81.2
# Branded dashoffset stays 60 (top start); Non-branded offset: 60-157.6 = -97.6
fixes.append((
    '        <!-- donut chart: circumference of r=38 = 238.8; branded 70%=167, non-branded 30%=72 -->\n        <svg viewBox="0 0 100 100" style="width:90px;flex-shrink:0;" xmlns="http://www.w3.org/2000/svg">\n          <circle cx="50" cy="50" r="38" fill="none" stroke="#FFEBEE" stroke-width="18"/>\n          <!-- branded 70% — start at top (-90°), draw 252° -->\n          <circle cx="50" cy="50" r="38" fill="none" stroke="#E74C3C" stroke-width="18"\n            stroke-dasharray="167 72" stroke-dashoffset="60" stroke-linecap="butt"/>\n          <!-- non-branded 30% — follows after branded -->\n          <circle cx="50" cy="50" r="38" fill="none" stroke="#00B4D8" stroke-width="18"\n            stroke-dasharray="72 167" stroke-dashoffset="-107" stroke-linecap="butt"/>\n          <text x="50" y="47" text-anchor="middle" font-size="13" font-weight="700" fill="#2c3e50">70%</text>\n          <text x="50" y="59" text-anchor="middle" font-size="8" fill="#7f8c8d">branded</text>\n        </svg>',
    '        <!-- donut chart: circumference of r=38 = 238.8; branded 66%=157.6, non-branded 34%=81.2 -->\n        <svg viewBox="0 0 100 100" style="width:90px;flex-shrink:0;" xmlns="http://www.w3.org/2000/svg">\n          <circle cx="50" cy="50" r="38" fill="none" stroke="#FFEBEE" stroke-width="18"/>\n          <!-- branded 66% — start at top -->\n          <circle cx="50" cy="50" r="38" fill="none" stroke="#E74C3C" stroke-width="18"\n            stroke-dasharray="157.6 81.2" stroke-dashoffset="60" stroke-linecap="butt"/>\n          <!-- non-branded 34% — follows after branded -->\n          <circle cx="50" cy="50" r="38" fill="none" stroke="#00B4D8" stroke-width="18"\n            stroke-dasharray="81.2 157.6" stroke-dashoffset="-97.6" stroke-linecap="butt"/>\n          <text x="50" y="47" text-anchor="middle" font-size="13" font-weight="700" fill="#2c3e50">66%</text>\n          <text x="50" y="59" text-anchor="middle" font-size="8" fill="#7f8c8d">branded</text>\n        </svg>'
))

# 1m. Branded/non-branded legend: update click numbers and the % in callout
fixes.append((
    '<div><span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:#E74C3C;margin-right:5px;vertical-align:middle;"></span><strong>Branded</strong>: ~1,260 clicks/mo</div>',
    '<div><span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:#E74C3C;margin-right:5px;vertical-align:middle;"></span><strong>Branded</strong>: ~1,800 clicks/mo</div>'
))

fixes.append((
    '<div><span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:#00B4D8;margin-right:5px;vertical-align:middle;"></span><strong>Non-branded</strong>: ~540 clicks/mo</div>',
    '<div><span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:#00B4D8;margin-right:5px;vertical-align:middle;"></span><strong>Non-branded</strong>: ~940 clicks/mo</div>'
))

# 1n. Top queries table — update click numbers with real GSC Feb-Apr 2026 data (monthly avg)
fixes.append((
    '          <tr><td class="mono teal">cdca certification ohio</td><td>26</td><td class="bold" style="color:var(--green);">2.5</td><td class="dim">—</td></tr>',
    '          <tr><td class="mono teal">cdca certification ohio</td><td>33</td><td class="bold" style="color:var(--green);">2.7</td><td class="dim">—</td></tr>'
))

fixes.append((
    '          <tr><td class="mono teal">cdca certification</td><td>22</td><td class="bold" style="color:var(--green);">2.4</td><td class="dim">—</td></tr>',
    '          <tr><td class="mono teal">cdca certification</td><td>26</td><td class="bold" style="color:var(--green);">3.0</td><td class="dim">—</td></tr>'
))

fixes.append((
    '          <tr><td class="mono teal">cdca certification online ohio</td><td>16</td><td class="bold" style="color:var(--green);">1.2</td><td class="dim">—</td></tr>',
    '          <tr><td class="mono teal">cdca certification online ohio</td><td>14</td><td class="bold" style="color:var(--green);">1.2</td><td class="dim">—</td></tr>'
))

fixes.append((
    '          <tr><td class="mono teal">cadc certification</td><td>8</td><td style="color:var(--yellow);">3.8</td><td class="dim">—</td></tr>',
    '          <tr><td class="mono teal">cadc certification</td><td>11</td><td style="color:var(--yellow);">4.1</td><td class="dim">—</td></tr>'
))

fixes.append((
    '          <tr><td class="mono teal">online lcdc programs in texas</td><td>7</td><td style="color:var(--yellow);">6.0</td><td class="dim">—</td></tr>',
    '          <tr><td class="mono teal">online lcdc programs in texas</td><td>6</td><td style="color:var(--yellow);">6.5</td><td class="dim">—</td></tr>'
))

fixes.append((
    '          <tr><td class="mono teal">substance abuse counselor certification online</td><td>4</td><td style="color:var(--red);">22.6</td><td class="dim">1,800+</td></tr>',
    '          <tr><td class="mono teal">substance abuse counselor certification</td><td>4</td><td style="color:var(--red);">14.2</td><td class="dim">—</td></tr>'
))

# 1o. Callout: 70% → 66%, update last row reference
fixes.append((
    '<strong>The ceiling is branded.</strong> 70% of clicks come from people who already know you. The last row (4 clicks on 1,800 impressions at position 22) shows the non-branded opportunity hiding in page 2.',
    '<strong>The ceiling is branded.</strong> 66% of clicks come from people who already know you. The remaining 34% (non-branded) is the addressable growth engine. Ranking for the long tail of credential and state queries converts this ratio.'
))

# ────────────────────────────────────────────────────────
# 2. INTAKE FIXES
# ────────────────────────────────────────────────────────

# 2a. Hack/spam context: add disavow to M1 technical work
# Find the M1 technical items and add a disavow row
fixes.append((
    '        <tr><td>7</td><td>Broken internal links: all 20 instances resolved</td><td class="dim">4 unique broken URLs across 20 link instances per audit</td></tr>',
    '        <tr><td>7</td><td>Broken internal links: all 20 instances resolved</td><td class="dim">4 unique broken URLs across 20 link instances per audit</td></tr>\n        <tr><td>8</td><td>Spam backlink disavow file</td><td class="dim">Site was compromised 2023–2024 with casino/spam links; disavow file submitted to Google to remove toxic link signals depressing authority score</td></tr>'
))

# 2b. Domain comparison annotation: add hack context to backlink narrative
fixes.append((
    '<strong>CEU Matrix has more referring domains than all three competitors.</strong> The existing link profile should be producing rankings — but there are no content pages to rank. Building the hub architecture in M1–M2 turns existing link authority directly into keyword positions.',
    '<strong>CEU Matrix has 1,200 referring domains — more than all three competitors.</strong> However, the 2023–2024 site hack introduced a large volume of casino/spam backlinks that are suppressing the authority score. A disavow file in M1 cleans the profile. Once resolved, the legitimate link equity converts directly to rankings as content pages go live.'
))

# 2c. Migration/decline context on baseline slide subtitle
fixes.append((
    '  <p class="subtitle" style="margin-bottom:16px;">Everything measured before the first optimization.</p>',
    '  <p class="subtitle" style="margin-bottom:16px;">Everything measured before the first optimization. Organic traffic has declined ~24% since the May 2025 peak; the February 2026 site migration caused a temporary bounce now normalizing. This is the true starting line.</p>'
))

# 2d. 20-year language: "20+ years in business" → "20+ years of board-verified credentialing"
fixes.append((
    '          <tr><td><strong>20+ years in business</strong></td><td>Homepage, About, every state page trust section</td></tr>',
    '          <tr><td><strong>20+ years of board-verified credentialing</strong></td><td>Homepage, About, every state page trust section — framed as established authority, not longevity</td></tr>'
))

# 2e. Q3 certification guide alignment note — add to M2 Ohio hub row
fixes.append((
    '      <h3 style="margin-top:20px;margin-bottom:10px;">Hub Page Architecture</h3>',
    '      <div class="annotation info" style="margin-bottom:12px;font-size:12px;"><strong>Q3 2026 alignment:</strong> The client plans to launch a dedicated state certification guide section in Q3 2026. The hub pages built in M2–M3 serve as the SEO-optimized foundation for that launch. Coordinate URL structure and navigation with their dev timeline.</div>\n      <h3 style="margin-top:20px;margin-bottom:10px;">Hub Page Architecture</h3>'
))

# 2f. Subscription timing note in M1 content strategy
fixes.append((
    '    <p>Build backlinks from state boards, accreditation bodies, and addiction counseling directories, the same sources CASR uses to outrank you.</p>',
    '    <p>Build backlinks from state boards, accreditation bodies, and addiction counseling directories, the same sources CASR uses to outrank you.</p>\n    <p style="font-size:12px;color:var(--text-light);margin-top:8px;"><strong>Note:</strong> CEU Matrix is transitioning to an unlimited subscription model. Article CTAs currently point to state/package pages; update CTA copy and links when the subscription model launches.</p>'
))

# 2g. CE vs CEU keyword note — add to keyword strategy section
fixes.append((
    '  <p class="subtitle">Not all searches are the same. Your customers move through three distinct stages, and CEU Matrix only shows up at one of them today.</p>',
    '  <p class="subtitle">Not all searches are the same. Your customers move through three distinct stages, and CEU Matrix only shows up at one of them today.</p>\n  <div class="annotation info" style="margin-top:12px;font-size:12px;"><strong>Keyword note:</strong> Customers search both "CE" and "CEU" variants (e.g., "addiction counselor CE requirements" and "addiction counselor CEU requirements"). All content targets both forms — whichever has higher volume for that specific topic leads, with the alternate form used naturally in-copy.</div>'
))

# ────────────────────────────────────────────────────────
# 3. BACKLINK GAP REFRAME: delivery commitment → opportunity map
# ────────────────────────────────────────────────────────

# 3a. Backlink gap slide stat card: "18 backlinks" → "18 priority targets"
fixes.append((
    '      <div class="stat-value teal">18</div>\n      <div class="stat-label">backlinks targeted over M2–M4</div>',
    '      <div class="stat-value teal">18</div>\n      <div class="stat-label">priority acquisition targets identified</div>'
))

# 3b. Backlink gap slide subtitle — remove link count delivery language
fixes.append((
    '  <p class="subtitle" style="margin-bottom:16px;">18 backlinks over M2–M4, sourced entirely from domains already linking to competitors. Relevance is pre-qualified; acquisition rate is 3x higher than cold prospecting.</p>',
    '  <p class="subtitle" style="margin-bottom:16px;">18 pre-qualified acquisition targets — domains already linking to competitors that are relevant to CEU Matrix. Outreach pathway and anchor text mapped for each. Guest post and partner listing opportunities prioritized by domain authority.</p>'
))

# 3c. M2 backlink rows — reframe as guest posts/partner listings, not committed link count
fixes.append((
    '        <tr><td>9</td><td>Backlink outreach: Batch 1</td><td class="dim">Target 6 domains from gap report (Partner listing + CE provider directory pathways first)</td></tr>',
    '        <tr><td>9</td><td>Backlink outreach: Batch 1</td><td class="dim">Submit to partner listing and CE provider directory targets from gap report (pathways requiring no editorial negotiation first)</td></tr>'
))

fixes.append((
    '        <tr><td>9</td><td>Backlink outreach: Batch 2</td><td class="dim">Target 6 more domains (resource listing + partner request pathways)</td></tr>',
    '        <tr><td>9</td><td>Backlink outreach: Batch 2</td><td class="dim">Pursue resource listing and partner request targets; identify guest post placement opportunities on editorial sites in the gap report</td></tr>'
))

fixes.append((
    '        <tr><td>9</td><td>Backlink outreach: Batch 3 + close</td><td class="dim">Final 6 domains; confirm all M2–M3 links indexed</td></tr>',
    '        <tr><td>9</td><td>Backlink outreach: Batch 3</td><td class="dim">Pursue remaining gap report targets; confirm directory and partner listings from M2–M3 are indexed</td></tr>'
))

# 3d. Section divider subtitle for backlink gap
fixes.append((
    '  <p class="subtitle">Every domain linking to CASR, CE4Less, or AllCEUs that does not link to CEU Matrix, annotated with DA, relevance, and outreach pathway.</p>',
    '  <p class="subtitle">Every domain linking to CASR, CE4Less, or AllCEUs that does not link to CEU Matrix — annotated with DA, relevance, and recommended acquisition pathway (directory submission, partner listing, guest post, or resource page).</p>'
))

# ────────────────────────────────────────────────────────
# Apply all fixes
# ────────────────────────────────────────────────────────

applied = 0
for old, new in fixes:
    if old in html:
        html = html.replace(old, new, 1)
        applied += 1
    else:
        print(f"  WARNING: not found — {old[:80].strip()!r}")

with open(DECK, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nApplied {applied}/{len(fixes)} fixes. Deck saved.")
