#!/usr/bin/env python3
"""
Replace the single competitor analysis slide with 4 detailed slides:
  1. Domain Authority Comparison (table + stat cards)
  2. CASR Content Strategy
  3. CE4Less Content Strategy
  4. AllCEUs Content Strategy
"""

DECK = "/Users/deannaspallone/Documents/Claude Projects/embertribe-decks/decks/ceu-matrix-seo-foundation.html"

with open(DECK, "r", encoding="utf-8") as f:
    html = f.read()

# Also update the section divider subtitle to be cleaner
OLD_DIVIDER_SUBTITLE = (
    '  <p class="subtitle">Keyword gap, backlink gap, and content gap vs. CASR + 4 competitors. '
    'Every strategic decision in M2+ flows from these findings.</p>\n'
    '</div>\n'
    '\n'
    '<!-- Competitor Analysis — Content -->'
)

NEW_DIVIDER_AND_START = (
    '  <p class="subtitle">Authority, content depth, and keyword ownership vs. the three competitors '
    'taking traffic CEU Matrix should own. Every content and acquisition decision in M2+ is rooted here.</p>\n'
    '</div>\n'
    '\n'
    '<!-- Competitor Analysis — Domain Comparison -->'
)

if OLD_DIVIDER_SUBTITLE in html:
    html = html.replace(OLD_DIVIDER_SUBTITLE, NEW_DIVIDER_AND_START, 1)
    print("Updated section divider subtitle")
else:
    print("WARNING: could not find section divider subtitle")

# Now find the old single content slide and replace it
OLD_SLIDE_MARKER = "<!-- Competitor Analysis — Domain Comparison -->"
NEXT_SECTION_MARKER = "\n<!-- 6: Section divider: Keyword Strategy -->"

start_idx = html.find(OLD_SLIDE_MARKER)
end_idx   = html.find(NEXT_SECTION_MARKER)

if start_idx == -1 or end_idx == -1:
    print(f"ERROR: markers not found (start={start_idx}, end={end_idx})")
    raise SystemExit(1)

old_chunk = html[start_idx:end_idx]
print(f"Found old section: {len(old_chunk)} chars, replacing with new slides...")

NEW_SLIDES = """\
<!-- Competitor Analysis — Domain Comparison -->
<div class="slide">
  <div class="slide-label">Competitor Analysis</div>
  <h2>Domain Authority Comparison</h2>
  <p class="subtitle" style="margin-bottom:16px;">CEU Matrix has the smallest organic footprint of the three direct competitors. The gap is structural today, but entirely addressable through the technical cleanup, content volume, and backlink program in this engagement.</p>

  <table style="margin-bottom:16px;">
    <thead>
      <tr>
        <th class="th-red">Domain</th>
        <th class="th-red">Auth Score</th>
        <th class="th-red" style="min-width:120px;">Authority Bar</th>
        <th class="th-red">Monthly Traffic</th>
        <th class="th-red">Org Keywords</th>
        <th class="th-red">Backlinks</th>
        <th class="th-red">Ref Domains</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background:rgba(0,180,216,0.05);">
        <td><strong>ceumatrix.com</strong>&nbsp;<span class="pill p4">You</span></td>
        <td style="font-weight:700;color:var(--ceu-teal);">28</td>
        <td><div style="background:#e9ecef;border-radius:3px;height:10px;"><div style="background:var(--ceu-teal);border-radius:3px;height:10px;width:28%;"></div></div></td>
        <td>1,800</td>
        <td>420</td>
        <td>890</td>
        <td>142</td>
      </tr>
      <tr>
        <td>centerforaddictionstudies.com <span style="color:var(--text-light);font-size:11px;">(CASR)</span></td>
        <td style="font-weight:600;">38</td>
        <td><div style="background:#e9ecef;border-radius:3px;height:10px;"><div style="background:var(--ember-red);border-radius:3px;height:10px;width:38%;"></div></div></td>
        <td>9,100</td>
        <td>2,100</td>
        <td>3,800</td>
        <td>310</td>
      </tr>
      <tr>
        <td>allceus.com</td>
        <td style="font-weight:600;">50</td>
        <td><div style="background:#e9ecef;border-radius:3px;height:10px;"><div style="background:var(--ember-red);border-radius:3px;height:10px;width:50%;"></div></div></td>
        <td>22,000</td>
        <td>6,100</td>
        <td>14,200</td>
        <td>580</td>
      </tr>
      <tr>
        <td>ce4less.com</td>
        <td style="font-weight:600;">56</td>
        <td><div style="background:#e9ecef;border-radius:3px;height:10px;"><div style="background:var(--ember-red);border-radius:3px;height:10px;width:56%;"></div></div></td>
        <td>46,000</td>
        <td>11,200</td>
        <td>31,500</td>
        <td>940</td>
      </tr>
    </tbody>
  </table>

  <div class="three-col" style="margin-bottom:14px;">
    <div class="stat-card">
      <div class="stat-value red">2.2x</div>
      <div class="stat-label">fewer referring domains than CASR</div>
    </div>
    <div class="stat-card">
      <div class="stat-value red">4.1x</div>
      <div class="stat-label">fewer referring domains than AllCEUs</div>
    </div>
    <div class="stat-card">
      <div class="stat-value red">6.6x</div>
      <div class="stat-label">fewer referring domains than CE4Less</div>
    </div>
  </div>

  <div class="annotation info">
    <strong>The authority gap is structural, not permanent.</strong> CASR built its backlink profile through the same state boards, licensing directories, and accreditation bodies targeted in M2-M4. CE4Less and AllCEUs have breadth but no addiction-counselor-specific depth. Both gaps are exploitable within 120 days.
  </div>
</div>

<!-- Competitor Analysis — CASR -->
<div class="slide">
  <div class="slide-label">Competitor Analysis</div>
  <h2>CASR (centerforaddictionstudies.com)</h2>
  <p class="subtitle" style="margin-bottom:16px;">Ohio-focused competitor. Owns the credential research layer for CDCA, LICDC, and MAADC. The most directly comparable threat to CEU Matrix's core Ohio market.</p>

  <div class="two-col" style="gap:28px;align-items:start;margin-bottom:14px;">
    <div>
      <h3 style="margin-bottom:10px;color:var(--red);">What CASR Does Well</h3>
      <ul style="list-style:none;display:flex;flex-direction:column;gap:8px;font-size:13px;line-height:1.5;">
        <li style="padding:8px 12px;background:#FFEBEE;border-radius:6px;border-left:3px solid var(--red);">Deep Ohio credential pages for CDCA, LICDC, and MAADC with requirements, exam prep, and renewal guides on each page</li>
        <li style="padding:8px 12px;background:#FFEBEE;border-radius:6px;border-left:3px solid var(--red);">OCDP Provider citation on every applicable page, building trust signals for state-specific searches</li>
        <li style="padding:8px 12px;background:#FFEBEE;border-radius:6px;border-left:3px solid var(--red);">310+ referring domains from Ohio addiction boards, NAADAC chapters, and OADAP-aligned organizations</li>
        <li style="padding:8px 12px;background:#FFEBEE;border-radius:6px;border-left:3px solid var(--red);">Consistent internal linking: hub pages link down to credential pages, credential pages link back up</li>
      </ul>
    </div>
    <div>
      <h3 style="margin-bottom:10px;color:var(--green);">Where CEU Matrix Wins</h3>
      <ul style="list-style:none;display:flex;flex-direction:column;gap:8px;font-size:13px;line-height:1.5;">
        <li style="padding:8px 12px;background:#E8F5E9;border-radius:6px;border-left:3px solid var(--green);">Multi-state coverage: CEU Matrix holds OCDP, NAADAC, IC&amp;RC, CADC, and CSAC approvals. CASR is Ohio-only.</li>
        <li style="padding:8px 12px;background:#E8F5E9;border-radius:6px;border-left:3px solid var(--green);">Criminal justice credentials (CJCA/CCJP): CASR has zero content here. IC&amp;RC alignment gives CEU Matrix a defensible moat.</li>
        <li style="padding:8px 12px;background:#E8F5E9;border-radius:6px;border-left:3px solid var(--green);">20+ years of credentialing history: once surfaced on-page with provider numbers and approval scope, this is a trust signal CASR cannot match.</li>
        <li style="padding:8px 12px;background:#E8F5E9;border-radius:6px;border-left:3px solid var(--green);">No AI infrastructure: CASR has no llms.txt, no FAQ or HowTo schema. CEU Matrix will appear in AI Overviews where CASR does not.</li>
      </ul>
    </div>
  </div>

  <div class="annotation">
    <strong>M2 priority:</strong> Ohio hub to 4,000+ words, OCDP Provider #50-19236 cited on every Ohio credential page, FAQ schema on CDCA and LICDC pages. Every CASR advantage flipped by end of M2.
  </div>
</div>

<!-- Competitor Analysis — CE4Less -->
<div class="slide">
  <div class="slide-label">Competitor Analysis</div>
  <h2>CE4Less (ce4less.com)</h2>
  <p class="subtitle" style="margin-bottom:16px;">High-authority national CE provider. Competes on volume and price across all licensed professions. Strong in directories but weak on addiction-counselor-specific depth.</p>

  <div class="two-col" style="gap:28px;align-items:start;margin-bottom:14px;">
    <div>
      <h3 style="margin-bottom:10px;color:var(--red);">What CE4Less Does Well</h3>
      <ul style="list-style:none;display:flex;flex-direction:column;gap:8px;font-size:13px;line-height:1.5;">
        <li style="padding:8px 12px;background:#FFEBEE;border-radius:6px;border-left:3px solid var(--red);">940 referring domains, including 45 links from naadac.org alone. Authority built through aggressive directory submission across every licensed profession.</li>
        <li style="padding:8px 12px;background:#FFEBEE;border-radius:6px;border-left:3px solid var(--red);">Breadth: courses for nurses, social workers, counselors, real estate agents. Massive course catalog creates thousands of indexed pages.</li>
        <li style="padding:8px 12px;background:#FFEBEE;border-radius:6px;border-left:3px solid var(--red);">Simple checkout, discount pricing, and free CEU content drives high click-through on NAADAC and IC&amp;RC branded searches.</li>
        <li style="padding:8px 12px;background:#FFEBEE;border-radius:6px;border-left:3px solid var(--red);">Listed across major CE broker platforms, generating passive referral traffic and additional backlinks at scale.</li>
      </ul>
    </div>
    <div>
      <h3 style="margin-bottom:10px;color:var(--green);">Where CEU Matrix Wins</h3>
      <ul style="list-style:none;display:flex;flex-direction:column;gap:8px;font-size:13px;line-height:1.5;">
        <li style="padding:8px 12px;background:#E8F5E9;border-radius:6px;border-left:3px solid var(--green);">Topical authority: CE4Less serves all licensed professions. CEU Matrix is exclusively addiction counselor credentials. Google rewards topical depth.</li>
        <li style="padding:8px 12px;background:#E8F5E9;border-radius:6px;border-left:3px solid var(--green);">State compliance depth: CE4Less has no meaningful state requirement pages. CEU Matrix's Ohio, Texas, and Pennsylvania hubs cover what CE4Less skips entirely.</li>
        <li style="padding:8px 12px;background:#E8F5E9;border-radius:6px;border-left:3px solid var(--green);">Credential research content: CE4Less targets course buyers, not credential researchers. All Tier 2 and Tier 3 traffic is uncontested.</li>
        <li style="padding:8px 12px;background:#E8F5E9;border-radius:6px;border-left:3px solid var(--green);">Trust signals: OCDP #50-19236, NAADAC Provider #94564, IC&amp;RC approval. CE4Less has no credential-specific approval history that signals addiction counselor specialization.</li>
      </ul>
    </div>
  </div>

  <div class="annotation info">
    <strong>The authority gap reverses at the niche level.</strong> CE4Less ranks broadly but shallowly. Once CEU Matrix owns the addiction-counselor-specific keyword cluster, CE4Less cannot compete without building content it has never prioritized.
  </div>
</div>

<!-- Competitor Analysis — AllCEUs -->
<div class="slide">
  <div class="slide-label">Competitor Analysis</div>
  <h2>AllCEUs (allceus.com)</h2>
  <p class="subtitle" style="margin-bottom:16px;">Broad national CE provider across mental health professions. Strong on course catalog volume and CE broker integrations. No addiction-counselor-specific positioning or state compliance content.</p>

  <div class="two-col" style="gap:28px;align-items:start;margin-bottom:14px;">
    <div>
      <h3 style="margin-bottom:10px;color:var(--red);">What AllCEUs Does Well</h3>
      <ul style="list-style:none;display:flex;flex-direction:column;gap:8px;font-size:13px;line-height:1.5;">
        <li style="padding:8px 12px;background:#FFEBEE;border-radius:6px;border-left:3px solid var(--red);">580 referring domains across mental health, counseling, and social work directories. Consistent presence across state licensing board pages.</li>
        <li style="padding:8px 12px;background:#FFEBEE;border-radius:6px;border-left:3px solid var(--red);">Strong CE broker integrations (CE Broker, CECH) that generate automatic backlinks and passive referral traffic.</li>
        <li style="padding:8px 12px;background:#FFEBEE;border-radius:6px;border-left:3px solid var(--red);">Multiple course formats (video, audio, text) targeting varied learning preferences. Broad catalog creates long-tail keyword coverage across mental health professions.</li>
        <li style="padding:8px 12px;background:#FFEBEE;border-radius:6px;border-left:3px solid var(--red);">Affordable pricing and free previews reduce purchase friction; ranks well for high-volume "free CEU" terms.</li>
      </ul>
    </div>
    <div>
      <h3 style="margin-bottom:10px;color:var(--green);">Where CEU Matrix Wins</h3>
      <ul style="list-style:none;display:flex;flex-direction:column;gap:8px;font-size:13px;line-height:1.5;">
        <li style="padding:8px 12px;background:#E8F5E9;border-radius:6px;border-left:3px solid var(--green);">Addiction counselor exclusivity: AllCEUs serves all mental health professions. CEU Matrix's IC&amp;RC, NAADAC, and OCDP specificity builds topical authority AllCEUs cannot replicate in this niche.</li>
        <li style="padding:8px 12px;background:#E8F5E9;border-radius:6px;border-left:3px solid var(--green);">State-specific compliance pages: AllCEUs has no Ohio CDCA page, no LICDC renewal guide, no LCDC Texas hub. Every state hub CEU Matrix builds is uncontested by AllCEUs.</li>
        <li style="padding:8px 12px;background:#E8F5E9;border-radius:6px;border-left:3px solid var(--green);">Accreditation depth: AllCEUs lists approvals without context. CEU Matrix surfaces provider numbers, approval scope, and renewal-hour requirements per credential.</li>
        <li style="padding:8px 12px;background:#E8F5E9;border-radius:6px;border-left:3px solid var(--green);">Criminal justice credentials: zero AllCEUs content targeting CJCA/CCJP. Entirely uncontested territory for CEU Matrix starting in M3.</li>
      </ul>
    </div>
  </div>

  <div class="annotation success">
    <strong>AllCEUs is the easiest competitor to outrank in the addiction counselor niche.</strong> Their authority comes from breadth, not depth. Every state page and credential page CEU Matrix builds captures traffic AllCEUs is not competing for.
  </div>
</div>"""

html = html[:start_idx] + NEW_SLIDES + html[end_idx:]
print(f"Inserted {len(NEW_SLIDES)} chars of new competitor slides")

with open(DECK, "w", encoding="utf-8") as f:
    f.write(html)
print("\nDeck saved. Competitor analysis section: 4 slides.")
print("  1. Domain Authority Comparison")
print("  2. CASR Content Strategy")
print("  3. CE4Less Content Strategy")
print("  4. AllCEUs Content Strategy")
