#!/usr/bin/env python3
"""
Update CEU Matrix deck: North Carolina replaces Pennsylvania as Tier 1.
Also fix NAADAC provider number: #619 → #94564, add NBCC #6310.
"""

DECK = "/Users/deannaspallone/Documents/Claude Projects/embertribe-decks/decks/ceu-matrix-seo-foundation.html"

with open(DECK, "r", encoding="utf-8") as f:
    html = f.read()

changes = []

# ─────────────────────────────────────────────────────────────
# 1. Hub diagram spoke: Penn./CAC/CADC → N. Carolina/CSAC/LCAS
# ─────────────────────────────────────────────────────────────
old = '<div class="spoke t1" style="top:18px;right:44px;"><div class="sp-name">Penn.</div><div class="sp-cred">CAC/CADC</div></div>'
new = '<div class="spoke t1" style="top:18px;right:44px;"><div class="sp-name">N. Carolina</div><div class="sp-cred">CSAC/LCAS</div></div>'
if old in html:
    html = html.replace(old, new, 1)
    changes.append("✓ Hub diagram: Penn./CAC → N. Carolina/CSAC/LCAS")
else:
    changes.append("✗ Hub diagram spoke not found")

# ─────────────────────────────────────────────────────────────
# 2. State priority matrix: swap Pennsylvania Tier 1 → NC Tier 1
#    and demote PA to Tier 2
# ─────────────────────────────────────────────────────────────
old = '      <tr style="background:#FFF5F5;"><td><span class="pill p1">1</span></td><td class="bold">Pennsylvania</td><td>CAC I/II, CADC</td><td class="orange bold">#10</td><td class="orange">Top 5</td><td>200–350/mo</td><td class="bold teal">Build M2</td></tr>\n      <tr style="background:#FFFAF0;"><td><span class="pill p2">2</span></td><td class="bold">Florida</td><td>CAP, CCJP</td><td class="red bold">Not ranking</td><td class="orange">Ranking</td><td>200–400/mo</td><td>M3</td></tr>'
new = '      <tr style="background:#FFF5F5;"><td><span class="pill p1">1</span></td><td class="bold">North Carolina</td><td>CSAC, LCAS</td><td class="red bold">Not ranking (key terms)</td><td class="orange">Ranking</td><td>200–400/mo</td><td class="bold teal">Build M2</td></tr>\n      <tr style="background:#FFFAF0;"><td><span class="pill p2">2</span></td><td class="bold">Florida</td><td>CAP, CCJP</td><td class="red bold">Not ranking</td><td class="orange">Ranking</td><td>200–400/mo</td><td>M3</td></tr>'
if old in html:
    html = html.replace(old, new, 1)
    changes.append("✓ State matrix: Pennsylvania Tier 1 → North Carolina Tier 1")
else:
    changes.append("✗ State matrix PA row not found")

# Also update California row to add PA after it (PA now Tier 2)
old = '      <tr style="background:#FFFAF0;"><td><span class="pill p2">2</span></td><td class="bold">California</td><td>CATC, CADC</td><td class="red bold">Not ranking</td><td class="green">Top 5</td><td>200–400/mo</td><td>M3</td></tr>\n      <tr style="background:#FFFAF0;"><td><span class="pill p2">2</span></td><td class="bold">New York</td><td>CASAC</td><td class="red bold">Not ranking</td><td class="green">Top 5</td><td>200–300/mo</td><td>M4</td></tr>'
new = '      <tr style="background:#FFFAF0;"><td><span class="pill p2">2</span></td><td class="bold">Pennsylvania</td><td>CAC I/II, CADC</td><td class="orange bold">#10</td><td class="orange">Top 5</td><td>200–350/mo</td><td>M3</td></tr>\n      <tr style="background:#FFFAF0;"><td><span class="pill p2">2</span></td><td class="bold">California</td><td>CATC, CADC</td><td class="red bold">Not ranking</td><td class="green">Top 5</td><td>200–400/mo</td><td>M3</td></tr>\n      <tr style="background:#FFFAF0;"><td><span class="pill p2">2</span></td><td class="bold">New York</td><td>CASAC</td><td class="red bold">Not ranking</td><td class="green">Top 5</td><td>200–300/mo</td><td>M4</td></tr>'
if old in html:
    html = html.replace(old, new, 1)
    changes.append("✓ State matrix: Pennsylvania added to Tier 2")
else:
    changes.append("✗ State matrix CA/NY block not found for PA insert")

# ─────────────────────────────────────────────────────────────
# 3. Keyword map: Update CAC row (PA → NC context) + add NC/CSAC
# ─────────────────────────────────────────────────────────────
old = '      <tr><td class="bold">CAC</td><td>PA, CO</td><td>cac certification pennsylvania, cac 1 certification pa</td><td>100–300</td><td class="orange bold">#10 (PA)</td><td><span class="pill p2">High: M1 articles · M2</span></td></tr>'
new = '      <tr><td class="bold">CSAC / LCAS</td><td class="bold">North Carolina</td><td>csac certification nc, nc substance abuse counselor requirements</td><td>150–400</td><td class="red bold">Not ranking</td><td><span class="pill p1">Critical: M2</span></td></tr>\n      <tr><td class="bold">CAC</td><td>PA, CO</td><td>cac certification pennsylvania, cac 1 certification pa</td><td>100–300</td><td class="orange bold">#10 (PA)</td><td><span class="pill p2">High: M3</span></td></tr>'
if old in html:
    html = html.replace(old, new, 1)
    changes.append("✓ Keyword map: NC/CSAC row added, CAC updated to M3")
else:
    changes.append("✗ Keyword map CAC row not found")

# ─────────────────────────────────────────────────────────────
# 4. M2 page builds badge
# ─────────────────────────────────────────────────────────────
old = '3 Page Builds: Ohio hub · Texas hub · Pennsylvania hub'
new = '3 Page Builds: Ohio hub · Texas hub · North Carolina hub'
if old in html:
    html = html.replace(old, new, 1)
    changes.append("✓ M2 badge: Pennsylvania hub → North Carolina hub")
else:
    changes.append("✗ M2 page builds badge not found")

# ─────────────────────────────────────────────────────────────
# 5. M2 on-page implementations: PA schema row → NC
# ─────────────────────────────────────────────────────────────
old = '<tr><td>4</td><td>WebPage + BreadcrumbList schema: Pennsylvania unified hub</td><td class="dim">Consistent schema across all 3 state hubs</td></tr>'
new = '<tr><td>4</td><td>WebPage + BreadcrumbList schema: North Carolina unified hub</td><td class="dim">Consistent schema across all 3 state hubs</td></tr>'
if old in html:
    html = html.replace(old, new, 1)
    changes.append("✓ M2 schema row: PA → NC")
else:
    changes.append("✗ M2 PA schema row not found")

# ─────────────────────────────────────────────────────────────
# 6. M2 page builds table: Pennsylvania → North Carolina
# ─────────────────────────────────────────────────────────────
old = '<tr><td><strong>Pennsylvania Unified Hub</strong></td><td class="mono teal">/pennsylvania-substance-abuse-certification/</td><td>3,000+ words · PCBDD cited · CAC I/II + CADC tables · FAQ schema · internal links to PA course pages</td></tr>'
new = '<tr><td><strong>North Carolina Unified Hub</strong></td><td class="mono teal">/north-carolina-substance-abuse-certification/</td><td>3,000+ words · NCSAPPB cited · CSAC + LCAS tables · FAQ schema · internal links to NC course pages</td></tr>'
if old in html:
    html = html.replace(old, new, 1)
    changes.append("✓ M2 page builds table: PA hub → NC hub")
else:
    changes.append("✗ M2 PA hub table row not found")

# ─────────────────────────────────────────────────────────────
# 7. M2 milestone note
# ─────────────────────────────────────────────────────────────
old = 'Ohio, Texas, and Pennsylvania hub pages indexed. GSC shows new keywords entering the index across all three priority states. First non-branded rankings begin to appear.'
new = 'Ohio, Texas, and North Carolina hub pages indexed. GSC shows new keywords entering the index across all three priority states. First non-branded rankings begin to appear.'
if old in html:
    html = html.replace(old, new, 1)
    changes.append("✓ M2 milestone: PA → NC")
else:
    changes.append("✗ M2 milestone text not found")

# ─────────────────────────────────────────────────────────────
# 8. M3 on-page: PA hub → NC hub
# ─────────────────────────────────────────────────────────────
old = '<tr><td>3</td><td>Pennsylvania hub (existing)</td><td>Expand content depth — CEU Matrix ranks #10 for PA addiction counselor certification; defend and push to top 5</td></tr>'
new = '<tr><td>3</td><td>North Carolina hub (existing)</td><td>Expand content depth — CSAC and LCAS requirement pages indexed; push toward top 5 for NC substance abuse counselor terms</td></tr>'
if old in html:
    html = html.replace(old, new, 1)
    changes.append("✓ M3 on-page: PA hub → NC hub")
else:
    changes.append("✗ M3 PA hub on-page row not found")

# ─────────────────────────────────────────────────────────────
# 9. M3 articles: replace PA-focused articles with NC articles
# ─────────────────────────────────────────────────────────────
old = '        <tr><td>2</td><td>Pennsylvania CADC: Requirements, Cost &amp; Provider Guide</td><td class="mono teal">cadc certification pennsylvania</td><td>80–150</td><td>Mid-funnel</td></tr>\n        <tr><td>3</td><td>How to Get Your CAC I in Pennsylvania: Step-by-Step</td><td class="mono teal">cac 1 certification pennsylvania</td><td>30–60</td><td>Mid-funnel</td></tr>'
new = '        <tr><td>2</td><td>CSAC Certification in North Carolina: Requirements &amp; Application Guide</td><td class="mono teal">csac certification north carolina</td><td>100–250</td><td>Mid-funnel</td></tr>\n        <tr><td>3</td><td>LCAS Certification in North Carolina: Requirements &amp; Renewal</td><td class="mono teal">lcas certification north carolina</td><td>80–150</td><td>Mid-funnel</td></tr>'
if old in html:
    html = html.replace(old, new, 1)
    changes.append("✓ M3 articles: PA CADC/CAC articles → NC CSAC/LCAS articles")
else:
    changes.append("✗ M3 PA articles block not found")

old = '        <tr><td>7</td><td>Addiction Counselor Salary in Pennsylvania (2026)</td><td class="mono teal">addiction counselor salary pennsylvania</td><td>80–150</td><td>Top-of-funnel</td></tr>\n        <tr><td>8</td><td>How to Become an Addiction Counselor in Pennsylvania</td><td class="mono teal">how to become addiction counselor pennsylvania</td><td>50–100</td><td>Top-of-funnel</td></tr>\n        <tr><td>9</td><td>PA CADC Renewal: State Board Approved CEUs</td><td class="mono teal">pa cadc renewal requirements</td><td>30–60</td><td>Bottom-funnel</td></tr>'
new = '        <tr><td>7</td><td>Addiction Counselor Salary in North Carolina (2026)</td><td class="mono teal">addiction counselor salary north carolina</td><td>80–200</td><td>Top-of-funnel</td></tr>\n        <tr><td>8</td><td>How to Become an Addiction Counselor in North Carolina</td><td class="mono teal">how to become addiction counselor north carolina</td><td>50–150</td><td>Top-of-funnel</td></tr>\n        <tr><td>9</td><td>NC CSAC Renewal: NCSAPPB Approved CEU Courses</td><td class="mono teal">nc csac renewal requirements</td><td>30–80</td><td>Bottom-funnel</td></tr>'
if old in html:
    html = html.replace(old, new, 1)
    changes.append("✓ M3 articles: PA salary/how-to/renewal → NC equivalents")
else:
    changes.append("✗ M3 PA salary/how-to block not found")

old = '        <tr><td>14</td><td>CAC II Pennsylvania: Upgrading from CAC I: Requirements</td><td class="mono teal">cac 2 pennsylvania requirements</td><td>20–40</td><td>Mid-funnel</td></tr>'
new = '        <tr><td>14</td><td>NC Substance Abuse Counselor: CSAC vs LCAS — Which Path is Right?</td><td class="mono teal">csac vs lcas north carolina</td><td>30–80</td><td>Mid-funnel</td></tr>'
if old in html:
    html = html.replace(old, new, 1)
    changes.append("✓ M3 articles: CAC II PA → CSAC vs LCAS NC")
else:
    changes.append("✗ M3 CAC II PA article not found")

# ─────────────────────────────────────────────────────────────
# 10. M1 article list: CAC Certification in Pennsylvania → NC
# ─────────────────────────────────────────────────────────────
old = '      <tr><td>3</td><td>CAC Certification in Pennsylvania: Requirements, Application &amp; Renewal</td><td class="mono teal">cac certification pennsylvania</td><td>100–200</td><td>Mid-funnel</td></tr>'
new = '      <tr><td>3</td><td>CSAC Certification in North Carolina: Requirements, Application &amp; Renewal</td><td class="mono teal">csac certification north carolina</td><td>100–250</td><td>Mid-funnel</td></tr>'
if old in html:
    html = html.replace(old, new, 1)
    changes.append("✓ M1 articles: CAC PA → CSAC NC")
else:
    changes.append("✗ M1 CAC PA article not found")

# ─────────────────────────────────────────────────────────────
# 11. M3 backlinks: PA reference → NC
# ─────────────────────────────────────────────────────────────
old = '        <tr><td class="mono">/pennsylvania-cadc-certification/</td><td>Pennsylvania CADC requirements</td><td class="dim">PA counseling board resource</td></tr>'
new = '        <tr><td class="mono">/north-carolina-csac-certification/</td><td>North Carolina CSAC requirements</td><td class="dim">NCSAPPB board resource</td></tr>'
if old in html:
    html = html.replace(old, new)  # replace all occurrences
    changes.append("✓ Backlinks: PA CADC → NC CSAC")
else:
    changes.append("✗ Backlinks PA row not found")

# ─────────────────────────────────────────────────────────────
# 12. M4 on-page: Pennsylvania hub → North Carolina hub
# ─────────────────────────────────────────────────────────────
old = '<tr><td>10</td><td>Pennsylvania hub to PA credential sub-page</td><td>Bidirectional linking pass — enforce hub architecture consistency across all 3 states</td></tr>'
new = '<tr><td>10</td><td>North Carolina hub to NC credential sub-pages</td><td>Bidirectional linking pass — enforce hub architecture consistency across all 3 states</td></tr>'
if old in html:
    html = html.replace(old, new, 1)
    changes.append("✓ M4 on-page: PA hub → NC hub")
else:
    changes.append("✗ M4 PA hub row not found")

# ─────────────────────────────────────────────────────────────
# 13. NAADAC #619 → #94564 everywhere
# ─────────────────────────────────────────────────────────────
count = html.count('619')
html = html.replace('NAADAC Provider #619', 'NAADAC Provider #94564')
html = html.replace('NAADAC #619', 'NAADAC #94564')
html = html.replace('naadac #619', 'naadac #94564')
changes.append(f"✓ NAADAC number: #619 → #94564 (was in ~{count} places with '619')")

# ─────────────────────────────────────────────────────────────
# 14. E-E-A-T card: add NBCC #6310, update NAADAC description
# ─────────────────────────────────────────────────────────────
old = '<div class="eeat-card"><div class="ec-icon">🎓</div><div class="ec-label" style="color:var(--ceu-sky);">Expertise</div><div class="ec-desc">NAADAC Provider #94564 since 2005 · Credential-specific content · Author credentials</div></div>'
new = '<div class="eeat-card"><div class="ec-icon">🎓</div><div class="ec-label" style="color:var(--ceu-sky);">Expertise</div><div class="ec-desc">NAADAC Provider #94564 · NBCC Provider #6310 · IC&amp;RC approved · Credential-specific content</div></div>'
if old in html:
    html = html.replace(old, new, 1)
    changes.append("✓ E-E-A-T card: NBCC #6310 added")
else:
    changes.append("✗ E-E-A-T expertise card not found (NAADAC may not have been replaced yet)")

# ─────────────────────────────────────────────────────────────
# 15. Authority Signal Plan: add NBCC row
# ─────────────────────────────────────────────────────────────
old = '          <tr><td><strong>OCDP Provider #50-19236</strong></td><td>Ohio hub, Ohio credential pages, Ohio product pages</td></tr>'
new = '          <tr><td><strong>NBCC Provider #6310</strong></td><td>All pages — national board covering multi-state credential holders</td></tr>\n          <tr><td><strong>TCB Provider #1758-07</strong></td><td>Texas hub, Texas LCDC pages, TX product pages</td></tr>\n          <tr><td><strong>NCSAPPB approved</strong></td><td>North Carolina hub, NC credential pages</td></tr>\n          <tr><td><strong>OCDP Provider #50-19236</strong></td><td>Ohio hub, Ohio credential pages, Ohio product pages</td></tr>'
if old in html:
    html = html.replace(old, new, 1)
    changes.append("✓ Authority signal plan: NBCC #6310, TCB #1758-07, NCSAPPB rows added")
else:
    changes.append("✗ Authority signal OCDP row not found")

# ─────────────────────────────────────────────────────────────
# 16. E-E-A-T Authority card: update "15+ states" to "50 states"
# ─────────────────────────────────────────────────────────────
old = '<div class="ec-desc">State board approvals in 15+ states · Board provider numbers cited on-page</div>'
new = '<div class="ec-desc">Approved in all 50 states via IC&amp;RC, NAADAC &amp; NBCC · 15+ state-specific board approvals · Provider numbers cited on-page</div>'
if old in html:
    html = html.replace(old, new, 1)
    changes.append("✓ E-E-A-T authority card: updated to reflect 50-state coverage")
else:
    changes.append("✗ E-E-A-T authority card not found")

# ─────────────────────────────────────────────────────────────
# Save
# ─────────────────────────────────────────────────────────────
with open(DECK, "w", encoding="utf-8") as f:
    f.write(html)

print("\n".join(changes))
print(f"\nDone — deck saved.")
