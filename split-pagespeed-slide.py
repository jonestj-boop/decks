#!/usr/bin/env python3
"""
Two changes:
1. Remove PageSpeed Insights block from Issues Found slide
2. Grow the bar chart SVG viewBox so it fills the extra space
3. Insert a dedicated new PageSpeed Insights slide after Issues Found,
   with expanded metric names and more readable styling
"""

DECK = "/Users/deannaspallone/Documents/Claude Projects/embertribe-decks/decks/ceu-matrix-seo-foundation.html"

with open(DECK, "r", encoding="utf-8") as f:
    html = f.read()

# ─────────────────────────────────────────────────────────────────────────────
# 1. Remove PageSpeed block from Issues Found slide AND grow bar chart
# ─────────────────────────────────────────────────────────────────────────────

OLD_CHART_AND_PS = """  <!-- SVG audit bar chart -->
  <svg viewBox="0 0 620 132" style="width:100%;margin:10px 0 14px;" xmlns="http://www.w3.org/2000/svg" font-family="Inter,system-ui,sans-serif">
    <!-- subtle gridlines -->
    <line x1="155" y1="0" x2="155" y2="128" stroke="rgba(44,62,80,0.1)" stroke-width="1"/>
    <line x1="302" y1="0" x2="302" y2="128" stroke="rgba(44,62,80,0.07)" stroke-width="1" stroke-dasharray="3,3"/>
    <line x1="445" y1="0" x2="445" y2="128" stroke="rgba(44,62,80,0.07)" stroke-width="1" stroke-dasharray="3,3"/>"""

NEW_CHART = """  <!-- SVG audit bar chart — taller now that PageSpeed is its own slide -->
  <svg viewBox="0 0 620 170" style="width:100%;margin:10px 0 16px;" xmlns="http://www.w3.org/2000/svg" font-family="Inter,system-ui,sans-serif">
    <!-- subtle gridlines -->
    <line x1="160" y1="0" x2="160" y2="165" stroke="rgba(44,62,80,0.1)" stroke-width="1"/>
    <line x1="312" y1="0" x2="312" y2="165" stroke="rgba(44,62,80,0.07)" stroke-width="1" stroke-dasharray="3,3"/>
    <line x1="460" y1="0" x2="460" y2="165" stroke="rgba(44,62,80,0.07)" stroke-width="1" stroke-dasharray="3,3"/>"""

if OLD_CHART_AND_PS in html:
    html = html.replace(OLD_CHART_AND_PS, NEW_CHART, 1)
    print("✓ Bar chart viewBox expanded to 620×170")
else:
    print("✗ Bar chart anchor not found")

# Update the bar chart rows to match new baseline (x1=160 instead of 155, taller rows)
# Row 0: Broken links 59 (HIGH)
html = html.replace(
    """    <!-- Row 0: Broken links 59 (HIGH) -->
    <text x="148" y="13" text-anchor="end" fill="rgba(44,62,80,0.72)" font-size="10.5">Broken internal links</text>
    <rect x="155" y="2" width="290" height="13" rx="2" fill="rgba(231,76,60,0.75)"/>
    <text x="452" y="13" fill="#c0392b" font-size="10.5" font-weight="700">59</text>
    <text x="472" y="13" fill="rgba(44,62,80,0.4)" font-size="9.5">HIGH</text>

    <!-- Row 1: Thin content 58 (MED) -->
    <text x="148" y="31" text-anchor="end" fill="rgba(44,62,80,0.72)" font-size="10.5">Thin content pages</text>
    <rect x="155" y="20" width="285" height="13" rx="2" fill="rgba(243,156,18,0.65)"/>
    <text x="447" y="31" fill="#d68910" font-size="10.5" font-weight="700">58</text>
    <text x="467" y="31" fill="rgba(44,62,80,0.4)" font-size="9.5">MED</text>

    <!-- Row 2: Single-link pages 31 (MED) -->
    <text x="148" y="49" text-anchor="end" fill="rgba(44,62,80,0.72)" font-size="10.5">Pages w/ 1 internal link</text>
    <rect x="155" y="38" width="152" height="13" rx="2" fill="rgba(243,156,18,0.65)"/>
    <text x="314" y="49" fill="#d68910" font-size="10.5" font-weight="700">31</text>
    <text x="334" y="49" fill="rgba(44,62,80,0.4)" font-size="9.5">MED</text>

    <!-- Row 3: Missing meta 30 (HIGH) -->
    <text x="148" y="67" text-anchor="end" fill="rgba(44,62,80,0.72)" font-size="10.5">Missing meta descriptions</text>
    <rect x="155" y="56" width="147" height="13" rx="2" fill="rgba(231,76,60,0.75)"/>
    <text x="309" y="67" fill="#c0392b" font-size="10.5" font-weight="700">30</text>
    <text x="329" y="67" fill="rgba(44,62,80,0.4)" font-size="9.5">HIGH</text>

    <!-- Row 4: Multiple H1 19 (HIGH) -->
    <text x="148" y="85" text-anchor="end" fill="rgba(44,62,80,0.72)" font-size="10.5">Multiple H1 tags</text>
    <rect x="155" y="74" width="93" height="13" rx="2" fill="rgba(231,76,60,0.75)"/>
    <text x="255" y="85" fill="#c0392b" font-size="10.5" font-weight="700">19</text>
    <text x="275" y="85" fill="rgba(44,62,80,0.4)" font-size="9.5">HIGH</text>

    <!-- Row 5: Duplicate titles 6 (MED) -->
    <text x="148" y="103" text-anchor="end" fill="rgba(44,62,80,0.72)" font-size="10.5">Duplicate title tags</text>
    <rect x="155" y="92" width="29" height="13" rx="2" fill="rgba(243,156,18,0.65)"/>
    <text x="191" y="103" fill="#d68910" font-size="10.5" font-weight="700">6</text>
    <text x="211" y="103" fill="rgba(44,62,80,0.4)" font-size="9.5">MED</text>

    <!-- Row 6: Schema 0 (HIGH) -->
    <text x="148" y="121" text-anchor="end" fill="rgba(44,62,80,0.72)" font-size="10.5">Schema markup / llms.txt</text>
    <rect x="155" y="110" width="4" height="13" rx="1" fill="rgba(231,76,60,0.35)"/>
    <text x="166" y="121" fill="#c0392b" font-size="10.5" font-weight="700">0</text>
    <text x="186" y="121" fill="rgba(44,62,80,0.4)" font-size="9.5">HIGH — Not implemented</text>
  </svg>""",
    """    <!-- Row 0: Broken links 59 (HIGH) -->
    <text x="153" y="16" text-anchor="end" fill="rgba(44,62,80,0.75)" font-size="12">Broken internal links</text>
    <rect x="160" y="3" width="299" height="17" rx="2.5" fill="rgba(231,76,60,0.8)"/>
    <text x="467" y="16" fill="#c0392b" font-size="12" font-weight="700">59</text>
    <text x="490" y="16" fill="rgba(44,62,80,0.42)" font-size="10.5">HIGH</text>

    <!-- Row 1: Thin content 58 (MED) -->
    <text x="153" y="40" text-anchor="end" fill="rgba(44,62,80,0.75)" font-size="12">Thin content pages</text>
    <rect x="160" y="27" width="294" height="17" rx="2.5" fill="rgba(243,156,18,0.7)"/>
    <text x="462" y="40" fill="#d68910" font-size="12" font-weight="700">58</text>
    <text x="485" y="40" fill="rgba(44,62,80,0.42)" font-size="10.5">MED</text>

    <!-- Row 2: Single-link pages 31 (MED) -->
    <text x="153" y="64" text-anchor="end" fill="rgba(44,62,80,0.75)" font-size="12">Pages w/ 1 internal link</text>
    <rect x="160" y="51" width="157" height="17" rx="2.5" fill="rgba(243,156,18,0.7)"/>
    <text x="325" y="64" fill="#d68910" font-size="12" font-weight="700">31</text>
    <text x="348" y="64" fill="rgba(44,62,80,0.42)" font-size="10.5">MED</text>

    <!-- Row 3: Missing meta 30 (HIGH) -->
    <text x="153" y="88" text-anchor="end" fill="rgba(44,62,80,0.75)" font-size="12">Missing meta descriptions</text>
    <rect x="160" y="75" width="152" height="17" rx="2.5" fill="rgba(231,76,60,0.8)"/>
    <text x="320" y="88" fill="#c0392b" font-size="12" font-weight="700">30</text>
    <text x="343" y="88" fill="rgba(44,62,80,0.42)" font-size="10.5">HIGH</text>

    <!-- Row 4: Multiple H1 19 (HIGH) -->
    <text x="153" y="112" text-anchor="end" fill="rgba(44,62,80,0.75)" font-size="12">Multiple H1 tags</text>
    <rect x="160" y="99" width="96" height="17" rx="2.5" fill="rgba(231,76,60,0.8)"/>
    <text x="264" y="112" fill="#c0392b" font-size="12" font-weight="700">19</text>
    <text x="287" y="112" fill="rgba(44,62,80,0.42)" font-size="10.5">HIGH</text>

    <!-- Row 5: Duplicate titles 6 (MED) -->
    <text x="153" y="136" text-anchor="end" fill="rgba(44,62,80,0.75)" font-size="12">Duplicate title tags</text>
    <rect x="160" y="123" width="30" height="17" rx="2.5" fill="rgba(243,156,18,0.7)"/>
    <text x="198" y="136" fill="#d68910" font-size="12" font-weight="700">6</text>
    <text x="221" y="136" fill="rgba(44,62,80,0.42)" font-size="10.5">MED</text>

    <!-- Row 6: Schema 0 (HIGH) -->
    <text x="153" y="160" text-anchor="end" fill="rgba(44,62,80,0.75)" font-size="12">Schema markup / llms.txt</text>
    <rect x="160" y="147" width="5" height="17" rx="1.5" fill="rgba(231,76,60,0.3)"/>
    <text x="173" y="160" fill="#c0392b" font-size="12" font-weight="700">0</text>
    <text x="196" y="160" fill="rgba(44,62,80,0.42)" font-size="10.5">HIGH — Not implemented</text>
  </svg>""",
    1
)
print("✓ Bar chart rows updated to match new scale")

# ─────────────────────────────────────────────────────────────────────────────
# 2. Remove the PageSpeed Insights block from Issues Found slide
# ─────────────────────────────────────────────────────────────────────────────
PS_START = "\n  <!-- PageSpeed Insights — live data Apr 2026 -->"
PS_END   = "\n  <table style=\"margin-top:16px;width:100%;\">"

ps_start_idx = html.find(PS_START)
ps_end_idx   = html.find(PS_END, ps_start_idx)

if ps_start_idx != -1 and ps_end_idx != -1:
    ps_block = html[ps_start_idx:ps_end_idx]
    html = html[:ps_start_idx] + html[ps_end_idx:]
    print(f"✓ PageSpeed block extracted from Issues Found slide ({len(ps_block)} chars)")
else:
    print(f"✗ PageSpeed block not found: start={ps_start_idx}, end={ps_end_idx}")
    ps_block = ""

# ─────────────────────────────────────────────────────────────────────────────
# 3. Build the new dedicated PageSpeed slide and insert after Issues Found
# ─────────────────────────────────────────────────────────────────────────────
NEW_PS_SLIDE = """
<!-- PageSpeed Insights — standalone slide -->
<div class="slide">
  <div class="slide-label">Technical Audit: Performance</div>
  <h2>PageSpeed Insights</h2>
  <p class="subtitle" style="margin-bottom:18px;">Live scores pulled from Google PageSpeed Insights for ceumatrix.com (April 2026). Desktop Performance is the primary flag.</p>

  <!-- Score circles — 2 rows: Desktop + Mobile -->
  <div style="display:flex;gap:32px;align-items:flex-start;margin-bottom:22px;">

    <!-- Desktop circles -->
    <div style="flex:1.5;">
      <div style="font-size:11px;font-weight:700;color:rgba(44,62,80,0.5);letter-spacing:.07em;text-transform:uppercase;margin-bottom:6px;">Desktop</div>
      <svg viewBox="0 0 520 90" xmlns="http://www.w3.org/2000/svg" font-family="Inter,system-ui,sans-serif" style="width:100%;">
        <!-- r=32, circumference=201.1 -->
        <!-- Performance 59 — orange -->
        <circle cx="52" cy="38" r="32" fill="none" stroke="rgba(44,62,80,0.08)" stroke-width="6"/>
        <circle cx="52" cy="38" r="32" fill="none" stroke="#e67e22" stroke-width="6"
          stroke-dasharray="118.6 82.5" transform="rotate(-90 52 38)" stroke-linecap="round"/>
        <text x="52" y="44" text-anchor="middle" fill="#e67e22" font-size="16" font-weight="700">59</text>
        <text x="52" y="78" text-anchor="middle" fill="rgba(44,62,80,0.6)" font-size="10">Performance</text>

        <!-- Accessibility 84 — orange -->
        <circle cx="182" cy="38" r="32" fill="none" stroke="rgba(44,62,80,0.08)" stroke-width="6"/>
        <circle cx="182" cy="38" r="32" fill="none" stroke="#e67e22" stroke-width="6"
          stroke-dasharray="168.9 32.2" transform="rotate(-90 182 38)" stroke-linecap="round"/>
        <text x="182" y="44" text-anchor="middle" fill="#e67e22" font-size="16" font-weight="700">84</text>
        <text x="182" y="78" text-anchor="middle" fill="rgba(44,62,80,0.6)" font-size="10">Accessibility</text>

        <!-- Best Practices 92 — green -->
        <circle cx="312" cy="38" r="32" fill="none" stroke="rgba(44,62,80,0.08)" stroke-width="6"/>
        <circle cx="312" cy="38" r="32" fill="none" stroke="#27AE60" stroke-width="6"
          stroke-dasharray="185.0 16.1" transform="rotate(-90 312 38)" stroke-linecap="round"/>
        <text x="312" y="44" text-anchor="middle" fill="#27AE60" font-size="16" font-weight="700">92</text>
        <text x="312" y="78" text-anchor="middle" fill="rgba(44,62,80,0.6)" font-size="10">Best Practices</text>

        <!-- SEO 77 — orange -->
        <circle cx="442" cy="38" r="32" fill="none" stroke="rgba(44,62,80,0.08)" stroke-width="6"/>
        <circle cx="442" cy="38" r="32" fill="none" stroke="#e67e22" stroke-width="6"
          stroke-dasharray="154.8 46.3" transform="rotate(-90 442 38)" stroke-linecap="round"/>
        <text x="442" y="44" text-anchor="middle" fill="#e67e22" font-size="16" font-weight="700">77</text>
        <text x="442" y="78" text-anchor="middle" fill="rgba(44,62,80,0.6)" font-size="10">SEO</text>
      </svg>
    </div>

    <!-- Mobile circles -->
    <div style="flex:1.5;">
      <div style="font-size:11px;font-weight:700;color:rgba(44,62,80,0.5);letter-spacing:.07em;text-transform:uppercase;margin-bottom:6px;">Mobile</div>
      <svg viewBox="0 0 520 90" xmlns="http://www.w3.org/2000/svg" font-family="Inter,system-ui,sans-serif" style="width:100%;">
        <!-- Performance 100 — green -->
        <circle cx="52" cy="38" r="32" fill="none" stroke="rgba(44,62,80,0.08)" stroke-width="6"/>
        <circle cx="52" cy="38" r="32" fill="none" stroke="#27AE60" stroke-width="6"
          stroke-dasharray="201.1 0" transform="rotate(-90 52 38)" stroke-linecap="round"/>
        <text x="52" y="44" text-anchor="middle" fill="#27AE60" font-size="16" font-weight="700">100</text>
        <text x="52" y="78" text-anchor="middle" fill="rgba(44,62,80,0.6)" font-size="10">Performance</text>

        <!-- Accessibility 83 — orange -->
        <circle cx="182" cy="38" r="32" fill="none" stroke="rgba(44,62,80,0.08)" stroke-width="6"/>
        <circle cx="182" cy="38" r="32" fill="none" stroke="#e67e22" stroke-width="6"
          stroke-dasharray="166.9 34.2" transform="rotate(-90 182 38)" stroke-linecap="round"/>
        <text x="182" y="44" text-anchor="middle" fill="#e67e22" font-size="16" font-weight="700">83</text>
        <text x="182" y="78" text-anchor="middle" fill="rgba(44,62,80,0.6)" font-size="10">Accessibility</text>

        <!-- Best Practices 100 — green -->
        <circle cx="312" cy="38" r="32" fill="none" stroke="rgba(44,62,80,0.08)" stroke-width="6"/>
        <circle cx="312" cy="38" r="32" fill="none" stroke="#27AE60" stroke-width="6"
          stroke-dasharray="201.1 0" transform="rotate(-90 312 38)" stroke-linecap="round"/>
        <text x="312" y="44" text-anchor="middle" fill="#27AE60" font-size="16" font-weight="700">100</text>
        <text x="312" y="78" text-anchor="middle" fill="rgba(44,62,80,0.6)" font-size="10">Best Practices</text>

        <!-- SEO 77 — orange -->
        <circle cx="442" cy="38" r="32" fill="none" stroke="rgba(44,62,80,0.08)" stroke-width="6"/>
        <circle cx="442" cy="38" r="32" fill="none" stroke="#e67e22" stroke-width="6"
          stroke-dasharray="154.8 46.3" transform="rotate(-90 442 38)" stroke-linecap="round"/>
        <text x="442" y="44" text-anchor="middle" fill="#e67e22" font-size="16" font-weight="700">77</text>
        <text x="442" y="78" text-anchor="middle" fill="rgba(44,62,80,0.6)" font-size="10">SEO</text>
      </svg>
    </div>
  </div>

  <!-- Core Web Vitals + key gap -->
  <div style="display:flex;gap:28px;align-items:flex-start;">

    <!-- CWV table -->
    <div style="flex:1;">
      <div style="font-size:11px;font-weight:700;color:rgba(44,62,80,0.5);letter-spacing:.07em;text-transform:uppercase;margin-bottom:10px;">Core Web Vitals (Lab Data)</div>
      <table style="width:100%;font-size:13px;">
        <thead>
          <tr>
            <th style="text-align:left;padding:5px 10px 5px 0;border-bottom:1px solid rgba(44,62,80,0.1);color:rgba(44,62,80,0.5);font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;">Metric</th>
            <th style="text-align:left;padding:5px 10px 5px 0;border-bottom:1px solid rgba(44,62,80,0.1);color:rgba(44,62,80,0.5);font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;">What it measures</th>
            <th style="text-align:right;padding:5px 0 5px 0;border-bottom:1px solid rgba(44,62,80,0.1);color:rgba(44,62,80,0.5);font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;">Score</th>
            <th style="text-align:right;padding:5px 0 5px 10px;border-bottom:1px solid rgba(44,62,80,0.1);color:rgba(44,62,80,0.5);font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;">Threshold</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="padding:6px 10px 6px 0;font-weight:700;color:rgba(44,62,80,0.8);">FCP</td>
            <td style="padding:6px 10px 6px 0;color:rgba(44,62,80,0.6);font-size:12px;">First Contentful Paint — first text/image visible</td>
            <td style="padding:6px 0;text-align:right;color:#27AE60;font-weight:700;">0.3 s</td>
            <td style="padding:6px 0 6px 10px;text-align:right;color:rgba(44,62,80,0.38);font-size:11px;">Good &lt; 1.8s</td>
          </tr>
          <tr style="background:rgba(44,62,80,0.02);">
            <td style="padding:6px 10px 6px 0;font-weight:700;color:rgba(44,62,80,0.8);">LCP</td>
            <td style="padding:6px 10px 6px 0;color:rgba(44,62,80,0.6);font-size:12px;">Largest Contentful Paint — main content loaded</td>
            <td style="padding:6px 0;text-align:right;color:#27AE60;font-weight:700;">0.8 s</td>
            <td style="padding:6px 0 6px 10px;text-align:right;color:rgba(44,62,80,0.38);font-size:11px;">Good &lt; 2.5s</td>
          </tr>
          <tr>
            <td style="padding:6px 10px 6px 0;font-weight:700;color:rgba(44,62,80,0.8);">CLS</td>
            <td style="padding:6px 10px 6px 0;color:rgba(44,62,80,0.6);font-size:12px;">Cumulative Layout Shift — visual stability</td>
            <td style="padding:6px 0;text-align:right;color:#27AE60;font-weight:700;">0.002</td>
            <td style="padding:6px 0 6px 10px;text-align:right;color:rgba(44,62,80,0.38);font-size:11px;">Good &lt; 0.1</td>
          </tr>
          <tr style="background:rgba(44,62,80,0.02);">
            <td style="padding:6px 10px 6px 0;font-weight:700;color:rgba(44,62,80,0.8);">TBT</td>
            <td style="padding:6px 10px 6px 0;color:rgba(44,62,80,0.6);font-size:12px;">Total Blocking Time — main thread blocked</td>
            <td style="padding:6px 0;text-align:right;color:#27AE60;font-weight:700;">0 ms</td>
            <td style="padding:6px 0 6px 10px;text-align:right;color:rgba(44,62,80,0.38);font-size:11px;">Good &lt; 200ms</td>
          </tr>
          <tr>
            <td style="padding:6px 10px 6px 0;font-weight:700;color:rgba(44,62,80,0.8);">Speed Index</td>
            <td style="padding:6px 10px 6px 0;color:rgba(44,62,80,0.6);font-size:12px;">How quickly content is visually populated</td>
            <td style="padding:6px 0;text-align:right;color:#27AE60;font-weight:700;">0.6 s</td>
            <td style="padding:6px 0 6px 10px;text-align:right;color:rgba(44,62,80,0.38);font-size:11px;">Good &lt; 3.4s</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Key gap callout -->
    <div style="flex:0.65;background:#FFF3E0;border-left:4px solid #e67e22;border-radius:0 8px 8px 0;padding:16px 18px;">
      <div style="font-size:12px;font-weight:700;color:#d35400;text-transform:uppercase;letter-spacing:.05em;margin-bottom:8px;">Key Gap</div>
      <div style="font-size:13.5px;color:rgba(44,62,80,0.85);line-height:1.65;">
        <strong>Desktop Performance: 59</strong> (needs improvement). Driven by unminified CSS/JS and render-blocking resources — not a Core Web Vitals problem, a load efficiency problem.
      </div>
      <div style="margin-top:10px;font-size:12px;color:rgba(44,62,80,0.65);line-height:1.55;">Mobile scores 100 — the site is fast when WooCommerce's asset payload is properly optimized. M2 tech fixes address this directly.</div>
      <div style="margin-top:12px;font-size:11.5px;color:#27AE60;font-weight:600;">✓ All Core Web Vitals pass — no UX penalties from Google</div>
    </div>
  </div>
</div>

"""

# Insert the new slide right after Issues Found (before Backlink Gap divider)
INSERT_MARKER = "\n<!-- Backlink Gap — Section Divider -->"
if INSERT_MARKER in html:
    html = html.replace(INSERT_MARKER, NEW_PS_SLIDE + "\n<!-- Backlink Gap — Section Divider -->", 1)
    print("✓ Dedicated PageSpeed Insights slide inserted after Issues Found")
else:
    print("✗ Insert marker not found")

with open(DECK, "w", encoding="utf-8") as f:
    f.write(html)
print("\nDone — deck saved.")
