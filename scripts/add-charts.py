#!/usr/bin/env python3
"""Add SVG charts to CEU Matrix deck — Slide 5 (audit) and Slide 17 (trajectory)."""

DECK = "/Users/deannaspallone/Documents/Claude Projects/embertribe-decks/decks/ceu-matrix-seo-foundation.html"

with open(DECK, "r", encoding="utf-8") as f:
    html = f.read()

# ─────────────────────────────────────────────────────────────
# CHANGE 1: Slide 5 — Add horizontal bar chart above issue tables
# Insert right after <h2>Issues Found</h2>
# ─────────────────────────────────────────────────────────────

AUDIT_OLD = '  <h2>Issues Found</h2>\n\n  <div class="two-col" style="margin-top:16px;">'

AUDIT_CHART = """  <h2>Issues Found</h2>

  <!-- SVG audit bar chart -->
  <svg viewBox="0 0 620 132" style="width:100%;margin:10px 0 14px;" xmlns="http://www.w3.org/2000/svg" font-family="Inter,system-ui,sans-serif">
    <!-- subtle gridlines -->
    <line x1="155" y1="0" x2="155" y2="128" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
    <line x1="302" y1="0" x2="302" y2="128" stroke="rgba(255,255,255,0.06)" stroke-width="1" stroke-dasharray="3,3"/>
    <line x1="445" y1="0" x2="445" y2="128" stroke="rgba(255,255,255,0.06)" stroke-width="1" stroke-dasharray="3,3"/>

    <!-- Row 0: Broken links 59 (HIGH) -->
    <text x="148" y="13" text-anchor="end" fill="rgba(255,255,255,0.65)" font-size="10.5">Broken internal links</text>
    <rect x="155" y="2" width="290" height="13" rx="2" fill="rgba(231,76,60,0.75)"/>
    <text x="452" y="13" fill="#e74c3c" font-size="10.5" font-weight="700">59</text>
    <text x="472" y="13" fill="rgba(255,255,255,0.32)" font-size="9.5">HIGH</text>

    <!-- Row 1: Thin content 58 (MED) -->
    <text x="148" y="31" text-anchor="end" fill="rgba(255,255,255,0.65)" font-size="10.5">Thin content pages</text>
    <rect x="155" y="20" width="285" height="13" rx="2" fill="rgba(243,156,18,0.65)"/>
    <text x="447" y="31" fill="#f39c12" font-size="10.5" font-weight="700">58</text>
    <text x="467" y="31" fill="rgba(255,255,255,0.32)" font-size="9.5">MED</text>

    <!-- Row 2: Single-link pages 31 (MED) -->
    <text x="148" y="49" text-anchor="end" fill="rgba(255,255,255,0.65)" font-size="10.5">Pages w/ 1 internal link</text>
    <rect x="155" y="38" width="152" height="13" rx="2" fill="rgba(243,156,18,0.65)"/>
    <text x="314" y="49" fill="#f39c12" font-size="10.5" font-weight="700">31</text>
    <text x="334" y="49" fill="rgba(255,255,255,0.32)" font-size="9.5">MED</text>

    <!-- Row 3: Missing meta 30 (HIGH) -->
    <text x="148" y="67" text-anchor="end" fill="rgba(255,255,255,0.65)" font-size="10.5">Missing meta descriptions</text>
    <rect x="155" y="56" width="147" height="13" rx="2" fill="rgba(231,76,60,0.75)"/>
    <text x="309" y="67" fill="#e74c3c" font-size="10.5" font-weight="700">30</text>
    <text x="329" y="67" fill="rgba(255,255,255,0.32)" font-size="9.5">HIGH</text>

    <!-- Row 4: Multiple H1 19 (HIGH) -->
    <text x="148" y="85" text-anchor="end" fill="rgba(255,255,255,0.65)" font-size="10.5">Multiple H1 tags</text>
    <rect x="155" y="74" width="93" height="13" rx="2" fill="rgba(231,76,60,0.75)"/>
    <text x="255" y="85" fill="#e74c3c" font-size="10.5" font-weight="700">19</text>
    <text x="275" y="85" fill="rgba(255,255,255,0.32)" font-size="9.5">HIGH</text>

    <!-- Row 5: Duplicate titles 6 (MED) -->
    <text x="148" y="103" text-anchor="end" fill="rgba(255,255,255,0.65)" font-size="10.5">Duplicate title tags</text>
    <rect x="155" y="92" width="29" height="13" rx="2" fill="rgba(243,156,18,0.65)"/>
    <text x="191" y="103" fill="#f39c12" font-size="10.5" font-weight="700">6</text>
    <text x="211" y="103" fill="rgba(255,255,255,0.32)" font-size="9.5">MED</text>

    <!-- Row 6: Schema 0 (HIGH) -->
    <text x="148" y="121" text-anchor="end" fill="rgba(255,255,255,0.65)" font-size="10.5">Schema markup / llms.txt</text>
    <rect x="155" y="110" width="4" height="13" rx="1" fill="rgba(231,76,60,0.35)"/>
    <text x="166" y="121" fill="#e74c3c" font-size="10.5" font-weight="700">0</text>
    <text x="186" y="121" fill="rgba(255,255,255,0.32)" font-size="9.5">HIGH — Not implemented</text>
  </svg>

  <div class="two-col" style="margin-top:16px;">"""

if AUDIT_OLD in html:
    html = html.replace(AUDIT_OLD, AUDIT_CHART, 1)
    print("✓ Slide 5: audit bar chart inserted")
else:
    print("✗ Slide 5: anchor string not found — check whitespace")

# ─────────────────────────────────────────────────────────────
# CHANGE 2: Slide 17 — Replace text bar-chart with SVG projection
# ─────────────────────────────────────────────────────────────

TRAJ_OLD = """  <h3 style="margin-top:24px;">Traffic Trajectory</h3>
  <div class="bar-chart" style="margin-top:10px;">
    <div class="bar-row"><div class="bar-label" style="color:rgba(255,255,255,0.6);">Apr '26 (today)</div><div class="bar-track"><div class="bar-fill ember-fill" style="width:20%;">~6,100/mo</div></div><div class="bar-value" style="color:rgba(255,255,255,0.4);">Branded-heavy</div></div>
    <div class="bar-row"><div class="bar-label" style="color:rgba(255,255,255,0.6);">Month 3</div><div class="bar-track"><div class="bar-fill" style="width:34%;background:linear-gradient(90deg,var(--yellow),#e67e22);">~10,000/mo</div></div><div class="bar-value" style="color:rgba(255,255,255,0.4);">Indexing</div></div>
    <div class="bar-row"><div class="bar-label" style="color:rgba(255,255,255,0.6);">Month 6</div><div class="bar-track"><div class="bar-fill" style="width:60%;background:linear-gradient(90deg,var(--yellow),#e67e22);">~18,000/mo</div></div><div class="bar-value" style="color:rgba(255,255,255,0.4);">Climbing</div></div>
    <div class="bar-row"><div class="bar-label" style="color:rgba(255,255,255,0.6);">Month 12</div><div class="bar-track"><div class="bar-fill green-fill" style="width:100%;">30,000+/mo</div></div><div class="bar-value" style="color:rgba(255,255,255,0.4);">Compounding</div></div>
  </div>"""

TRAJ_NEW = """  <h3 style="margin-top:20px;">Traffic Trajectory</h3>
  <!-- SVG projection chart: confirmed baseline → 12-month target -->
  <svg viewBox="0 0 600 185" style="width:100%;margin-top:6px;" xmlns="http://www.w3.org/2000/svg" font-family="Inter,system-ui,sans-serif">
    <defs>
      <linearGradient id="projGrad17" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#00B4D8" stop-opacity="0.3"/>
        <stop offset="100%" stop-color="#00B4D8" stop-opacity="0.04"/>
      </linearGradient>
    </defs>

    <!-- Y-axis gridlines -->
    <line x1="55" y1="155" x2="575" y2="155" stroke="rgba(255,255,255,0.14)" stroke-width="1"/>
    <line x1="55" y1="112" x2="575" y2="112" stroke="rgba(255,255,255,0.07)" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="55" y1="69" x2="575" y2="69" stroke="rgba(255,255,255,0.07)" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="55" y1="26" x2="575" y2="26" stroke="rgba(255,255,255,0.07)" stroke-width="1" stroke-dasharray="4,4"/>

    <!-- Y-axis labels -->
    <text x="48" y="159" text-anchor="end" fill="rgba(255,255,255,0.28)" font-size="9.5">0</text>
    <text x="48" y="116" text-anchor="end" fill="rgba(255,255,255,0.28)" font-size="9.5">10K</text>
    <text x="48" y="73" text-anchor="end" fill="rgba(255,255,255,0.28)" font-size="9.5">20K</text>
    <text x="48" y="30" text-anchor="end" fill="rgba(255,255,255,0.28)" font-size="9.5">30K</text>

    <!-- Projection area fill -->
    <!-- Points: (65,129) Apr26=6100  (205,112) M3=10K  (370,78) M6=18K  (565,26) M12=30K -->
    <path d="M65,129 L205,112 L370,78 L565,26 L565,155 L65,155 Z" fill="url(#projGrad17)"/>

    <!-- Confirmed area (solid stub under baseline dot) -->
    <rect x="58" y="129" width="7" height="26" rx="1" fill="rgba(39,174,96,0.35)"/>

    <!-- Projection line (dashed teal) -->
    <polyline points="65,129 205,112 370,78 565,26" fill="none" stroke="#00B4D8" stroke-width="2" stroke-dasharray="7,3.5" stroke-linejoin="round" stroke-linecap="round"/>

    <!-- Confirmed line (solid green, short) -->
    <line x1="55" y1="129" x2="65" y2="129" stroke="#27AE60" stroke-width="2"/>

    <!-- Data points -->
    <circle cx="65" cy="129" r="5.5" fill="#27AE60" stroke="rgba(255,255,255,0.85)" stroke-width="1.5"/>
    <circle cx="205" cy="112" r="4.5" fill="#00B4D8" stroke="rgba(255,255,255,0.7)" stroke-width="1.5"/>
    <circle cx="370" cy="78" r="4.5" fill="#00B4D8" stroke="rgba(255,255,255,0.7)" stroke-width="1.5"/>
    <circle cx="565" cy="26" r="5.5" fill="#00B4D8" stroke="rgba(255,255,255,0.9)" stroke-width="1.5"/>

    <!-- Data labels -->
    <text x="65" y="120" text-anchor="middle" fill="#27AE60" font-size="11" font-weight="700">6,100</text>
    <text x="205" y="103" text-anchor="middle" fill="#7ecfdf" font-size="10.5" font-weight="700">~10K</text>
    <text x="370" y="69" text-anchor="middle" fill="#7ecfdf" font-size="10.5" font-weight="700">~18K</text>
    <text x="565" y="17" text-anchor="middle" fill="#00B4D8" font-size="12" font-weight="700">30K+</text>

    <!-- X-axis labels -->
    <text x="65" y="170" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="10">Apr '26</text>
    <text x="65" y="181" text-anchor="middle" fill="#27AE60" font-size="9" font-weight="600">Confirmed</text>
    <text x="205" y="170" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="10">Month 3</text>
    <text x="370" y="170" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="10">Month 6</text>
    <text x="565" y="170" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="10">Month 12</text>

    <!-- Legend -->
    <circle cx="330" cy="10" r="4" fill="#27AE60"/>
    <text x="338" y="14" fill="rgba(255,255,255,0.55)" font-size="9.5">Confirmed (GA4)</text>
    <line x1="420" y1="10" x2="438" y2="10" stroke="#00B4D8" stroke-width="2" stroke-dasharray="5,2.5"/>
    <circle cx="429" cy="10" r="3" fill="#00B4D8" stroke="rgba(255,255,255,0.6)" stroke-width="1"/>
    <text x="442" y="14" fill="rgba(255,255,255,0.55)" font-size="9.5">Projected</text>
  </svg>"""

if TRAJ_OLD in html:
    html = html.replace(TRAJ_OLD, TRAJ_NEW, 1)
    print("✓ Slide 17: trajectory SVG chart inserted")
else:
    print("✗ Slide 17: anchor string not found — trying fallback")
    # Try to find partial match
    idx = html.find('<h3 style="margin-top:24px;">Traffic Trajectory</h3>')
    if idx != -1:
        print(f"  Found h3 at index {idx}, snippet:")
        print(repr(html[idx:idx+200]))
    else:
        print("  h3 not found either")

with open(DECK, "w", encoding="utf-8") as f:
    f.write(html)
print("\nDone — deck saved.")
