#!/usr/bin/env python3
"""
Conservative trajectory update:
- M3: ~7,500 (was ~10,000)
- M6: ~12,000 (was ~18,000)
- M12: ~20,000 (was 30,000+)
- Trajectory chart: restore white/light labels (dark slide)
- Cover slide: update Month 12 target stat
"""

DECK = "/Users/deannaspallone/Documents/Claude Projects/embertribe-decks/decks/ceu-matrix-seo-foundation.html"

with open(DECK, "r", encoding="utf-8") as f:
    html = f.read()

# ─────────────────────────────────────────────────────────────
# CHANGE 1: Replace trajectory SVG with conservative numbers
# + restore white/light text (dark slide)
#
# Scale: y=155→0, y=112→10K, y=69→20K, y=26→30K (4.3px/K)
# New points:
#   Apr'26: 6,100 → y=129 (unchanged)
#   M3:     7,500 → y=155-(7.5*4.3)=155-32.3≈123
#   M6:    12,000 → y=155-(12*4.3)=155-51.6≈103
#   M12:   20,000 → y=155-(20*4.3)=155-86=69  (lands on 20K gridline)
# ─────────────────────────────────────────────────────────────

TRAJ_OLD = """  <!-- SVG projection chart: confirmed baseline → 12-month target -->
  <svg viewBox="0 0 600 185" style="width:100%;margin-top:6px;" xmlns="http://www.w3.org/2000/svg" font-family="Inter,system-ui,sans-serif">
    <defs>
      <linearGradient id="projGrad17" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#00B4D8" stop-opacity="0.22"/>
        <stop offset="100%" stop-color="#00B4D8" stop-opacity="0.03"/>
      </linearGradient>
    </defs>

    <!-- Y-axis gridlines -->
    <line x1="55" y1="155" x2="575" y2="155" stroke="rgba(44,62,80,0.15)" stroke-width="1"/>
    <line x1="55" y1="112" x2="575" y2="112" stroke="rgba(44,62,80,0.09)" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="55" y1="69" x2="575" y2="69" stroke="rgba(44,62,80,0.09)" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="55" y1="26" x2="575" y2="26" stroke="rgba(44,62,80,0.09)" stroke-width="1" stroke-dasharray="4,4"/>

    <!-- Y-axis labels -->
    <text x="48" y="159" text-anchor="end" fill="rgba(44,62,80,0.45)" font-size="9.5">0</text>
    <text x="48" y="116" text-anchor="end" fill="rgba(44,62,80,0.45)" font-size="9.5">10K</text>
    <text x="48" y="73" text-anchor="end" fill="rgba(44,62,80,0.45)" font-size="9.5">20K</text>
    <text x="48" y="30" text-anchor="end" fill="rgba(44,62,80,0.45)" font-size="9.5">30K</text>

    <!-- Projection area fill -->
    <!-- Points: (65,129) Apr26=6100  (205,112) M3=10K  (370,78) M6=18K  (565,26) M12=30K -->
    <path d="M65,129 L205,112 L370,78 L565,26 L565,155 L65,155 Z" fill="url(#projGrad17)"/>

    <!-- Confirmed area (solid stub under baseline dot) -->
    <rect x="58" y="129" width="7" height="26" rx="1" fill="rgba(39,174,96,0.3)"/>

    <!-- Projection line (dashed teal) -->
    <polyline points="65,129 205,112 370,78 565,26" fill="none" stroke="#0093b0" stroke-width="2" stroke-dasharray="7,3.5" stroke-linejoin="round" stroke-linecap="round"/>

    <!-- Confirmed line (solid green, short) -->
    <line x1="55" y1="129" x2="65" y2="129" stroke="#27AE60" stroke-width="2"/>

    <!-- Data points -->
    <circle cx="65" cy="129" r="5.5" fill="#27AE60" stroke="rgba(255,255,255,0.85)" stroke-width="1.5"/>
    <circle cx="205" cy="112" r="4.5" fill="#0093b0" stroke="rgba(255,255,255,0.7)" stroke-width="1.5"/>
    <circle cx="370" cy="78" r="4.5" fill="#0093b0" stroke="rgba(255,255,255,0.7)" stroke-width="1.5"/>
    <circle cx="565" cy="26" r="5.5" fill="#0093b0" stroke="rgba(255,255,255,0.9)" stroke-width="1.5"/>

    <!-- Data labels -->
    <text x="65" y="120" text-anchor="middle" fill="#1e8449" font-size="11" font-weight="700">6,100</text>
    <text x="205" y="103" text-anchor="middle" fill="#0093b0" font-size="10.5" font-weight="700">~10K</text>
    <text x="370" y="69" text-anchor="middle" fill="#0093b0" font-size="10.5" font-weight="700">~18K</text>
    <text x="565" y="17" text-anchor="middle" fill="#0093b0" font-size="12" font-weight="700">30K+</text>

    <!-- X-axis labels -->
    <text x="65" y="170" text-anchor="middle" fill="rgba(44,62,80,0.6)" font-size="10">Apr '26</text>
    <text x="65" y="181" text-anchor="middle" fill="#1e8449" font-size="9" font-weight="600">Confirmed</text>
    <text x="205" y="170" text-anchor="middle" fill="rgba(44,62,80,0.6)" font-size="10">Month 3</text>
    <text x="370" y="170" text-anchor="middle" fill="rgba(44,62,80,0.6)" font-size="10">Month 6</text>
    <text x="565" y="170" text-anchor="middle" fill="rgba(44,62,80,0.6)" font-size="10">Month 12</text>

    <!-- Legend -->
    <circle cx="330" cy="10" r="4" fill="#27AE60"/>
    <text x="338" y="14" fill="rgba(44,62,80,0.6)" font-size="9.5">Confirmed (GA4)</text>
    <line x1="420" y1="10" x2="438" y2="10" stroke="#0093b0" stroke-width="2" stroke-dasharray="5,2.5"/>
    <circle cx="429" cy="10" r="3" fill="#0093b0" stroke="rgba(255,255,255,0.6)" stroke-width="1"/>
    <text x="442" y="14" fill="rgba(44,62,80,0.6)" font-size="9.5">Projected</text>
  </svg>"""

TRAJ_NEW = """  <!-- SVG projection chart: confirmed baseline → 12-month conservative target -->
  <svg viewBox="0 0 600 185" style="width:100%;margin-top:6px;" xmlns="http://www.w3.org/2000/svg" font-family="Inter,system-ui,sans-serif">
    <defs>
      <linearGradient id="projGrad17" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#00B4D8" stop-opacity="0.28"/>
        <stop offset="100%" stop-color="#00B4D8" stop-opacity="0.04"/>
      </linearGradient>
    </defs>

    <!-- Y-axis gridlines -->
    <line x1="55" y1="155" x2="575" y2="155" stroke="rgba(255,255,255,0.14)" stroke-width="1"/>
    <line x1="55" y1="112" x2="575" y2="112" stroke="rgba(255,255,255,0.07)" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="55" y1="69" x2="575" y2="69" stroke="rgba(255,255,255,0.15)" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="55" y1="26" x2="575" y2="26" stroke="rgba(255,255,255,0.07)" stroke-width="1" stroke-dasharray="4,4"/>

    <!-- Y-axis labels -->
    <text x="48" y="159" text-anchor="end" fill="rgba(255,255,255,0.3)" font-size="9.5">0</text>
    <text x="48" y="116" text-anchor="end" fill="rgba(255,255,255,0.3)" font-size="9.5">10K</text>
    <text x="48" y="73" text-anchor="end" fill="rgba(255,255,255,0.55)" font-size="9.5">20K</text>
    <text x="48" y="30" text-anchor="end" fill="rgba(255,255,255,0.3)" font-size="9.5">30K</text>

    <!-- Projection area fill -->
    <!-- Points: (65,129)=6,100  (205,123)=7,500  (370,103)=12,000  (565,69)=20,000 -->
    <path d="M65,129 L205,123 L370,103 L565,69 L565,155 L65,155 Z" fill="url(#projGrad17)"/>

    <!-- Confirmed area stub -->
    <rect x="58" y="129" width="7" height="26" rx="1" fill="rgba(39,174,96,0.4)"/>

    <!-- Projection line (dashed teal) -->
    <polyline points="65,129 205,123 370,103 565,69" fill="none" stroke="#00B4D8" stroke-width="2" stroke-dasharray="7,3.5" stroke-linejoin="round" stroke-linecap="round"/>

    <!-- Confirmed line (solid green, short) -->
    <line x1="55" y1="129" x2="65" y2="129" stroke="#27AE60" stroke-width="2"/>

    <!-- Data points -->
    <circle cx="65" cy="129" r="5.5" fill="#27AE60" stroke="rgba(255,255,255,0.85)" stroke-width="1.5"/>
    <circle cx="205" cy="123" r="4.5" fill="#00B4D8" stroke="rgba(255,255,255,0.7)" stroke-width="1.5"/>
    <circle cx="370" cy="103" r="4.5" fill="#00B4D8" stroke="rgba(255,255,255,0.7)" stroke-width="1.5"/>
    <circle cx="565" cy="69" r="5.5" fill="#00B4D8" stroke="rgba(255,255,255,0.9)" stroke-width="1.5"/>

    <!-- Data labels -->
    <text x="65" y="120" text-anchor="middle" fill="#27AE60" font-size="11" font-weight="700">6,100</text>
    <text x="205" y="114" text-anchor="middle" fill="rgba(255,255,255,0.8)" font-size="10.5" font-weight="700">~7,500</text>
    <text x="370" y="94" text-anchor="middle" fill="rgba(255,255,255,0.8)" font-size="10.5" font-weight="700">~12,000</text>
    <text x="565" y="60" text-anchor="middle" fill="#00B4D8" font-size="12" font-weight="700">~20,000</text>

    <!-- X-axis labels -->
    <text x="65" y="170" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="10">Apr '26</text>
    <text x="65" y="181" text-anchor="middle" fill="#27AE60" font-size="9" font-weight="600">Confirmed</text>
    <text x="205" y="170" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="10">Month 3</text>
    <text x="370" y="170" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="10">Month 6</text>
    <text x="565" y="170" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="10">Month 12</text>

    <!-- Legend -->
    <circle cx="330" cy="10" r="4" fill="#27AE60"/>
    <text x="338" y="14" fill="rgba(255,255,255,0.55)" font-size="9.5">Confirmed (GA4)</text>
    <line x1="420" y1="10" x2="438" y2="10" stroke="#00B4D8" stroke-width="2" stroke-dasharray="5,2.5"/>
    <circle cx="429" cy="10" r="3" fill="#00B4D8" stroke="rgba(255,255,255,0.6)" stroke-width="1"/>
    <text x="442" y="14" fill="rgba(255,255,255,0.55)" font-size="9.5">Projected</text>
  </svg>"""

if TRAJ_OLD in html:
    html = html.replace(TRAJ_OLD, TRAJ_NEW, 1)
    print("✓ Trajectory chart: conservative numbers + white labels restored")
else:
    print("✗ Trajectory chart anchor not found")

# ─────────────────────────────────────────────────────────────
# CHANGE 2: Cover slide — update Month 12 target stat
# ─────────────────────────────────────────────────────────────
html = html.replace(
    '<div class="stat-num green">30,000+</div>\n          <div class="stat-label">Month 12 traffic target</div>',
    '<div class="stat-num green">20,000+</div>\n          <div class="stat-label">Month 12 traffic target</div>',
    1
)

# Also handle if it's formatted slightly differently (single line)
old_cover_stat = '>30,000+</div>\n          <div class="stat-label">Month 12 traffic target</div>'
new_cover_stat = '>20,000+</div>\n          <div class="stat-label">Month 12 traffic target</div>'
if old_cover_stat in html:
    html = html.replace(old_cover_stat, new_cover_stat, 1)
    print("✓ Cover slide: Month 12 stat updated to 20,000+")
else:
    # Try a more flexible search
    import re
    match = re.search(r'(30,000\+)(</div>\s*<div class="stat-label">Month 12 traffic target)', html)
    if match:
        html = html.replace(match.group(0), '20,000+' + match.group(2), 1)
        print("✓ Cover slide (regex): Month 12 stat updated to 20,000+")
    else:
        print("  Cover stat — searching for all 30,000+ occurrences:")
        for i, line in enumerate(html.split('\n')):
            if '30,000' in line:
                print(f"    Line {i}: {line.strip()[:80]}")

# ─────────────────────────────────────────────────────────────
# CHANGE 3: Roadmap annotation — update trajectory note
# ─────────────────────────────────────────────────────────────
html = html.replace(
    '<strong>Directional, not guaranteed.</strong> Baseline is confirmed at 6,100 organic sessions/month (Mar 2026, GA4). Growth projection models non-branded traffic layering on top of the existing branded base. Rankings compound: Month 1 articles gain authority through Month 12. Assumes conservative backlink acquisition.',
    '<strong>Directional, not guaranteed.</strong> Baseline confirmed at 6,100/mo (Mar 2026, GA4). Conservative model: technical fixes + Ohio hub indexing drives M3 lift; credential content compounds through M12. Assumes moderate backlink acquisition and 6–9 month ranking ramp.',
    1
)
print("✓ Roadmap annotation updated")

with open(DECK, "w", encoding="utf-8") as f:
    f.write(html)
print("\nDone — deck saved.")
