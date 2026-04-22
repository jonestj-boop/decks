#!/usr/bin/env python3
"""
Two changes:
1. Insert PageSpeed Insights visual on slide 5 (between bar chart and accordion table)
2. Convert slides 14+15 (Competitor Analysis / Backlink Gap) from white "Month 1 Deliverable"
   slides into dark section dividers, preserving their content as following content slides
"""

DECK = "/Users/deannaspallone/Documents/Claude Projects/embertribe-decks/decks/ceu-matrix-seo-foundation.html"

with open(DECK, "r", encoding="utf-8") as f:
    html = f.read()

# ─────────────────────────────────────────────────────────────────────────────
# 1. PAGESPEED INSIGHTS VISUAL — insert between bar chart SVG and accordion table
# ─────────────────────────────────────────────────────────────────────────────
# Data pulled live from pagespeed.web.dev Apr 2026:
#   Desktop: Performance=59, Accessibility=84, Best Practices=92, SEO=77
#   Mobile:  Performance=100, Accessibility=83, Best Practices=100, SEO=77
#   Lab CWV: FCP=0.3s, LCP=0.8s, TBT=0ms, CLS=0.002, Speed Index=0.6s
# Circle circumference for r=22: 2*pi*22 = 138.23
# dasharray = (score/100)*138.23 + " " + remainder

PAGESPEED_HTML = """
  <!-- PageSpeed Insights — live data Apr 2026 -->
  <div style="margin:14px 0 14px;background:rgba(0,180,216,0.04);border:1px solid rgba(0,180,216,0.18);border-radius:8px;padding:12px 16px;">
    <div style="font-size:10px;font-weight:700;color:rgba(44,62,80,0.45);letter-spacing:.08em;text-transform:uppercase;margin-bottom:10px;">PageSpeed Insights — ceumatrix.com (Apr 2026)</div>
    <div style="display:flex;gap:20px;align-items:flex-start;">

      <!-- Desktop score circles -->
      <div style="flex:1.3;">
        <div style="font-size:9px;font-weight:600;color:rgba(44,62,80,0.4);letter-spacing:.05em;text-transform:uppercase;margin-bottom:2px;">Desktop</div>
        <svg viewBox="0 0 320 68" xmlns="http://www.w3.org/2000/svg" font-family="Inter,system-ui,sans-serif" style="width:100%;">
          <!-- Performance 59 — orange (50-89 range) -->
          <g>
            <circle cx="40" cy="28" r="22" fill="none" stroke="rgba(44,62,80,0.08)" stroke-width="5"/>
            <circle cx="40" cy="28" r="22" fill="none" stroke="#e67e22" stroke-width="5"
              stroke-dasharray="81.6 56.6" transform="rotate(-90 40 28)" stroke-linecap="round"/>
            <text x="40" y="33" text-anchor="middle" fill="#e67e22" font-size="12" font-weight="700">59</text>
            <text x="40" y="60" text-anchor="middle" fill="rgba(44,62,80,0.52)" font-size="8.5">Performance</text>
          </g>
          <!-- Accessibility 84 — orange -->
          <g transform="translate(80,0)">
            <circle cx="40" cy="28" r="22" fill="none" stroke="rgba(44,62,80,0.08)" stroke-width="5"/>
            <circle cx="40" cy="28" r="22" fill="none" stroke="#e67e22" stroke-width="5"
              stroke-dasharray="116.1 22.1" transform="rotate(-90 40 28)" stroke-linecap="round"/>
            <text x="40" y="33" text-anchor="middle" fill="#e67e22" font-size="12" font-weight="700">84</text>
            <text x="40" y="60" text-anchor="middle" fill="rgba(44,62,80,0.52)" font-size="8.5">Accessibility</text>
          </g>
          <!-- Best Practices 92 — green (90-100 range) -->
          <g transform="translate(160,0)">
            <circle cx="40" cy="28" r="22" fill="none" stroke="rgba(44,62,80,0.08)" stroke-width="5"/>
            <circle cx="40" cy="28" r="22" fill="none" stroke="#27AE60" stroke-width="5"
              stroke-dasharray="127.2 11.1" transform="rotate(-90 40 28)" stroke-linecap="round"/>
            <text x="40" y="33" text-anchor="middle" fill="#27AE60" font-size="12" font-weight="700">92</text>
            <text x="40" y="60" text-anchor="middle" fill="rgba(44,62,80,0.52)" font-size="8.5">Best Practices</text>
          </g>
          <!-- SEO 77 — orange -->
          <g transform="translate(240,0)">
            <circle cx="40" cy="28" r="22" fill="none" stroke="rgba(44,62,80,0.08)" stroke-width="5"/>
            <circle cx="40" cy="28" r="22" fill="none" stroke="#e67e22" stroke-width="5"
              stroke-dasharray="106.4 31.8" transform="rotate(-90 40 28)" stroke-linecap="round"/>
            <text x="40" y="33" text-anchor="middle" fill="#e67e22" font-size="12" font-weight="700">77</text>
            <text x="40" y="60" text-anchor="middle" fill="rgba(44,62,80,0.52)" font-size="8.5">SEO</text>
          </g>
        </svg>
      </div>

      <!-- Core Web Vitals table -->
      <div style="flex:1;">
        <div style="font-size:9px;font-weight:600;color:rgba(44,62,80,0.4);letter-spacing:.05em;text-transform:uppercase;margin-bottom:2px;">Core Web Vitals (Lab)</div>
        <table style="width:100%;margin:0;font-size:11.5px;">
          <tbody>
            <tr>
              <td style="padding:3px 8px 3px 0;color:rgba(44,62,80,0.65);font-weight:600;width:90px;">FCP</td>
              <td style="color:#27AE60;font-weight:700;">0.3 s</td>
              <td style="color:rgba(44,62,80,0.38);font-size:9.5px;">Good &lt; 1.8s</td>
            </tr>
            <tr>
              <td style="padding:3px 8px 3px 0;color:rgba(44,62,80,0.65);font-weight:600;">LCP</td>
              <td style="color:#27AE60;font-weight:700;">0.8 s</td>
              <td style="color:rgba(44,62,80,0.38);font-size:9.5px;">Good &lt; 2.5s</td>
            </tr>
            <tr>
              <td style="padding:3px 8px 3px 0;color:rgba(44,62,80,0.65);font-weight:600;">CLS</td>
              <td style="color:#27AE60;font-weight:700;">0.002</td>
              <td style="color:rgba(44,62,80,0.38);font-size:9.5px;">Good &lt; 0.1</td>
            </tr>
            <tr>
              <td style="padding:3px 8px 3px 0;color:rgba(44,62,80,0.65);font-weight:600;">TBT</td>
              <td style="color:#27AE60;font-weight:700;">0 ms</td>
              <td style="color:rgba(44,62,80,0.38);font-size:9.5px;">Good &lt; 200ms</td>
            </tr>
            <tr>
              <td style="padding:3px 8px 3px 0;color:rgba(44,62,80,0.65);font-weight:600;">Speed Index</td>
              <td style="color:#27AE60;font-weight:700;">0.6 s</td>
              <td style="color:rgba(44,62,80,0.38);font-size:9.5px;">Good &lt; 3.4s</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div style="margin-top:8px;font-size:9.5px;color:rgba(44,62,80,0.45);border-left:2px solid rgba(231,126,34,0.5);padding-left:7px;">
      <strong style="color:rgba(44,62,80,0.6);">Key gap:</strong> Desktop Performance 59 — driven by unminified CSS/JS and render-blocking resources. Mobile scores 100. M2 tech fixes address this.
    </div>
  </div>

"""

ANCHOR_BEFORE_TABLE = "  <table style=\"margin-top:16px;width:100%;\">"

if "PageSpeed Insights" not in html:
    if ANCHOR_BEFORE_TABLE in html:
        html = html.replace(ANCHOR_BEFORE_TABLE, PAGESPEED_HTML + ANCHOR_BEFORE_TABLE, 1)
        print("✓ PageSpeed Insights visual inserted")
    else:
        print("✗ Accordion table anchor not found — check whitespace")
else:
    print("  PageSpeed already present")

# ─────────────────────────────────────────────────────────────────────────────
# 2a. SLIDE 14 — Competitor Analysis Report → Section Divider + Content Slide
# ─────────────────────────────────────────────────────────────────────────────

OLD_COMP_OPEN = """<!-- Competitor Analysis Report -->
<div class="slide">
  <div class="slide-label">Month 1 Deliverable</div>
  <h2>Competitor Analysis Report</h2>
  <p class="subtitle" style="margin-bottom:16px;">Keyword gap, backlink gap, and content gap vs. CASR + 4 competitors. Delivered end of Week 2. Every strategic decision in M2+ flows from these findings.</p>"""

NEW_COMP_OPEN = """<!-- Competitor Analysis — Section Divider -->
<div class="slide divider">
  <div class="divider-box">
    <div class="slide-label">SEO Foundation Deliverable</div>
    <h2>Competitor Analysis</h2>
  </div>
  <p class="subtitle">Keyword gap, backlink gap, and content gap vs. CASR + 4 competitors. Every strategic decision in M2+ flows from these findings.</p>
</div>

<!-- Competitor Analysis — Content -->
<div class="slide">
  <div class="slide-label">Competitor Analysis Report</div>
  <h2>Who CEU Matrix Is Losing To &amp; Why</h2>
  <p class="subtitle" style="margin-bottom:16px;">Full SEMrush competitor profile delivered end of Week 2. The keyword gaps, content gaps, and backlink gaps below define the entire M2–M4 content and acquisition strategy.</p>"""

if OLD_COMP_OPEN in html:
    html = html.replace(OLD_COMP_OPEN, NEW_COMP_OPEN, 1)
    print("✓ Slide 14: Competitor Analysis → section divider + content slide")
else:
    print("✗ Slide 14 anchor not found")

# ─────────────────────────────────────────────────────────────────────────────
# 2b. SLIDE 15 — Backlink Gap Report → Section Divider + Content Slide
# ─────────────────────────────────────────────────────────────────────────────

OLD_BL_OPEN = """<!-- Backlink Gap Report -->
<div class="slide">
  <div class="slide-label">Month 1 Deliverable</div>
  <h2>Backlink Gap Report</h2>
  <p class="subtitle" style="margin-bottom:16px;">Every domain linking to CASR, CE4Less, or Sober College that does not link to CEU Matrix — annotated with DA, relevance, and outreach pathway. The acquisition hit list for 18 backlinks over M2–M4.</p>"""

NEW_BL_OPEN = """<!-- Backlink Gap — Section Divider -->
<div class="slide divider">
  <div class="divider-box">
    <div class="slide-label">SEO Foundation Deliverable</div>
    <h2>Backlink Gap Analysis</h2>
  </div>
  <p class="subtitle">Every domain linking to CASR, CE4Less, or Sober College that does not link to CEU Matrix — annotated with DA, relevance, and outreach pathway.</p>
</div>

<!-- Backlink Gap — Content -->
<div class="slide">
  <div class="slide-label">Backlink Gap Report</div>
  <h2>The Acquisition Hit List</h2>
  <p class="subtitle" style="margin-bottom:16px;">18 backlinks over M2–M4, sourced entirely from domains already linking to competitors. Relevance is pre-qualified — acquisition rate 3x higher than cold prospecting.</p>"""

if OLD_BL_OPEN in html:
    html = html.replace(OLD_BL_OPEN, NEW_BL_OPEN, 1)
    print("✓ Slide 15: Backlink Gap → section divider + content slide")
else:
    print("✗ Slide 15 anchor not found")

# ─────────────────────────────────────────────────────────────────────────────
# 2c. Fix NAADAC provider number in Backlink Gap slide (#619 → #94564)
# ─────────────────────────────────────────────────────────────────────────────
html = html.replace(
    "CEU Matrix holds Provider #619 (since 2005)",
    "CEU Matrix holds Provider #94564 (since 2005)",
    1
)
print("✓ NAADAC provider number fixed in Backlink Gap slide")

with open(DECK, "w", encoding="utf-8") as f:
    f.write(html)
print("\nDone — deck saved.")
