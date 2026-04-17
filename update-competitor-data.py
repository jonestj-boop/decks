#!/usr/bin/env python3
"""
Replace all 4 competitor analysis content slides with 5 updated slides:
  1. Domain Comparison Table — real SEMrush numbers
  2. Traffic Share visual — donut chart + non-branded/branded bars
  3. CASR — visual comparison cards + streamlined bullets
  4. CE4Less — visual comparison cards + streamlined bullets
  5. AllCEUs — visual comparison cards + streamlined bullets
"""

DECK = "/Users/deannaspallone/Documents/Claude Projects/embertribe-decks/decks/ceu-matrix-seo-foundation.html"

with open(DECK, "r", encoding="utf-8") as f:
    html = f.read()

START_MARKER = "<!-- Competitor Analysis — Domain Comparison -->"
END_MARKER   = "\n<!-- 6: Section divider: Keyword Strategy -->"

start_idx = html.find(START_MARKER)
end_idx   = html.find(END_MARKER)

if start_idx == -1 or end_idx == -1:
    print(f"ERROR: markers not found (start={start_idx}, end={end_idx})")
    raise SystemExit(1)

print(f"Replacing {end_idx - start_idx} chars with new competitor section...")

# SVG donut chart math
# r=70, circumference = 2*pi*70 = 439.8 ≈ 440
# Traffic share: ce4less 87%, CASR 5%, AllCEUs 6%, CEU Matrix 2%
# dashoffset = 110 - cumulative_start  (110 = circumference/4, positions arc at 12 o'clock)

NEW_CONTENT = """\
<!-- Competitor Analysis — Domain Comparison -->
<div class="slide">
  <div class="slide-label">Competitor Analysis</div>
  <h2>Domain Comparison</h2>
  <p class="subtitle" style="margin-bottom:14px;">Real SEMrush data across all four domains. The data surfaces a key insight: the gap between CEU Matrix and CASR is not in links — it is entirely in content.</p>

  <table style="margin-bottom:14px;font-size:12.5px;">
    <thead>
      <tr>
        <th class="th-red">Domain</th>
        <th class="th-red">Auth Score</th>
        <th class="th-red" style="min-width:110px;">Score Bar</th>
        <th class="th-red">Org. Traffic</th>
        <th class="th-red">Org. Keywords</th>
        <th class="th-red">Backlinks</th>
        <th class="th-red">Ref. Domains</th>
        <th class="th-red">Paid KW</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background:rgba(0,180,216,0.05);">
        <td><strong>ceumatrix.com</strong>&nbsp;<span class="pill p4">You</span></td>
        <td style="font-weight:700;color:var(--ceu-teal);">22</td>
        <td><div style="background:#e9ecef;border-radius:3px;height:10px;"><div style="background:var(--ceu-teal);border-radius:3px;height:10px;width:22%;"></div></div></td>
        <td>769</td>
        <td>894</td>
        <td style="font-weight:600;color:var(--green);">1.7M</td>
        <td style="font-weight:600;color:var(--green);">1,200</td>
        <td>0</td>
      </tr>
      <tr>
        <td>centerforaddictionstudies.com <span style="color:var(--text-light);font-size:11px;">(CASR)</span></td>
        <td style="font-weight:600;">24</td>
        <td><div style="background:#e9ecef;border-radius:3px;height:10px;"><div style="background:var(--ember-red);border-radius:3px;height:10px;width:24%;"></div></div></td>
        <td>1,900</td>
        <td>3,000</td>
        <td>734</td>
        <td>189</td>
        <td>0</td>
      </tr>
      <tr>
        <td>allceus.com</td>
        <td style="font-weight:600;">28</td>
        <td><div style="background:#e9ecef;border-radius:3px;height:10px;"><div style="background:var(--ember-red);border-radius:3px;height:10px;width:28%;"></div></div></td>
        <td>1,900</td>
        <td>2,100</td>
        <td>8,200</td>
        <td>1,000</td>
        <td>0</td>
      </tr>
      <tr>
        <td>ce4less.com</td>
        <td style="font-weight:600;">38</td>
        <td><div style="background:#e9ecef;border-radius:3px;height:10px;"><div style="background:var(--ember-red);border-radius:3px;height:10px;width:38%;"></div></div></td>
        <td>32,200</td>
        <td>6,900</td>
        <td>4,000</td>
        <td>957</td>
        <td>123</td>
      </tr>
    </tbody>
  </table>

  <div class="three-col" style="margin-bottom:12px;">
    <div class="stat-card">
      <div class="stat-value red">42x</div>
      <div class="stat-label">less monthly traffic than CE4Less</div>
    </div>
    <div class="stat-card">
      <div class="stat-value orange">67%</div>
      <div class="stat-label">of visits are branded — only 33% is discovery</div>
    </div>
    <div class="stat-card">
      <div class="stat-value green">#1</div>
      <div class="stat-label">in referring domains — 1,200 vs CASR's 189</div>
    </div>
  </div>

  <div class="annotation success">
    <strong>CEU Matrix has more referring domains than all three competitors.</strong> The existing link profile should be producing rankings — but there are no content pages to rank. Building the hub architecture in M1–M2 turns existing link authority directly into keyword positions.
  </div>
</div>

<!-- Competitor Analysis — Traffic Share -->
<div class="slide">
  <div class="slide-label">Competitor Analysis</div>
  <h2>Traffic Share &amp; Search Intent Mix</h2>
  <p class="subtitle" style="margin-bottom:16px;">CE4Less holds 87% of shared traffic — but 84% of it is branded. CASR wins purely on discovery. That is the content model CEU Matrix replicates in M2.</p>

  <div style="display:flex;gap:36px;align-items:flex-start;">

    <!-- Donut chart -->
    <div style="flex-shrink:0;text-align:center;">
      <div style="font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:var(--text-light);margin-bottom:8px;">Traffic Share</div>
      <svg width="200" height="200" viewBox="0 0 220 220">
        <!-- CE4Less 87%: dash=382.8, offset=110 -->
        <circle cx="110" cy="110" r="70" fill="none" stroke="#E67E22" stroke-width="40"
          stroke-dasharray="382.8 57.2" stroke-dashoffset="110"/>
        <!-- CEU Matrix 2%: dash=8.8, cumulative=382.8, offset=110-382.8=-272.8 -->
        <circle cx="110" cy="110" r="70" fill="none" stroke="#00B4D8" stroke-width="40"
          stroke-dasharray="8.8 431.2" stroke-dashoffset="-272.8"/>
        <!-- CASR 5%: dash=22, cumulative=391.6, offset=110-391.6=-281.6 -->
        <circle cx="110" cy="110" r="70" fill="none" stroke="#27AE60" stroke-width="40"
          stroke-dasharray="22 418" stroke-dashoffset="-281.6"/>
        <!-- AllCEUs 6%: dash=26.4, cumulative=413.6, offset=110-413.6=-303.6 -->
        <circle cx="110" cy="110" r="70" fill="none" stroke="#8E44AD" stroke-width="40"
          stroke-dasharray="26.4 413.6" stroke-dashoffset="-303.6"/>
        <!-- Center label -->
        <text x="110" y="102" text-anchor="middle" font-size="26" font-weight="800" fill="#2c3e50">87%</text>
        <text x="110" y="118" text-anchor="middle" font-size="10" fill="#7f8c8d">ce4less.com</text>
        <text x="110" y="131" text-anchor="middle" font-size="10" fill="#7f8c8d">of shared traffic</text>
      </svg>
      <!-- Legend -->
      <div style="display:flex;flex-direction:column;gap:5px;margin-top:4px;text-align:left;">
        <div style="display:flex;align-items:center;gap:6px;font-size:11px;"><span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:#E67E22;flex-shrink:0;"></span>ce4less.com — 87%</div>
        <div style="display:flex;align-items:center;gap:6px;font-size:11px;"><span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:#8E44AD;flex-shrink:0;"></span>allceus.com — 6%</div>
        <div style="display:flex;align-items:center;gap:6px;font-size:11px;"><span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:#27AE60;flex-shrink:0;"></span>centerforaddictionstudies.com — 5%</div>
        <div style="display:flex;align-items:center;gap:6px;font-size:11px;"><span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:#00B4D8;flex-shrink:0;"></span>ceumatrix.com — 2%</div>
      </div>
    </div>

    <!-- Non-branded / Branded bars -->
    <div style="flex:1;">
      <div style="font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:var(--text-light);margin-bottom:12px;">Non-branded vs. Branded Traffic</div>

      <!-- ceumatrix -->
      <div style="margin-bottom:12px;">
        <div style="display:flex;justify-content:space-between;font-size:12px;font-weight:600;margin-bottom:4px;">
          <span>ceumatrix.com <span class="pill p4" style="font-size:9px;">You</span></span>
          <span style="color:var(--text-light);font-size:11px;">~254 non-branded visits/mo</span>
        </div>
        <div style="display:flex;height:20px;border-radius:4px;overflow:hidden;">
          <div style="width:33%;background:#00B4D8;" title="33% non-branded"></div>
          <div style="width:67%;background:#e9ecef;" title="67% branded"></div>
        </div>
        <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--text-light);margin-top:2px;">
          <span style="color:#00B4D8;font-weight:600;">33% non-branded</span><span>67% branded</span>
        </div>
      </div>

      <!-- CASR -->
      <div style="margin-bottom:12px;">
        <div style="display:flex;justify-content:space-between;font-size:12px;font-weight:600;margin-bottom:4px;">
          <span>centerforaddictionstudies.com</span>
          <span style="color:var(--text-light);font-size:11px;">~1,786 non-branded visits/mo</span>
        </div>
        <div style="display:flex;height:20px;border-radius:4px;overflow:hidden;">
          <div style="width:94%;background:#27AE60;" title="94% non-branded"></div>
          <div style="width:6%;background:#e9ecef;" title="6% branded"></div>
        </div>
        <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--text-light);margin-top:2px;">
          <span style="color:#27AE60;font-weight:600;">94% non-branded</span><span>6% branded</span>
        </div>
      </div>

      <!-- ce4less -->
      <div style="margin-bottom:12px;">
        <div style="display:flex;justify-content:space-between;font-size:12px;font-weight:600;margin-bottom:4px;">
          <span>ce4less.com</span>
          <span style="color:var(--text-light);font-size:11px;">~5,152 non-branded visits/mo</span>
        </div>
        <div style="display:flex;height:20px;border-radius:4px;overflow:hidden;">
          <div style="width:16%;background:#E67E22;" title="16% non-branded"></div>
          <div style="width:84%;background:#e9ecef;" title="84% branded"></div>
        </div>
        <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--text-light);margin-top:2px;">
          <span style="color:#E67E22;font-weight:600;">16% non-branded</span><span>84% branded</span>
        </div>
      </div>

      <!-- AllCEUs -->
      <div style="margin-bottom:12px;">
        <div style="display:flex;justify-content:space-between;font-size:12px;font-weight:600;margin-bottom:4px;">
          <span>allceus.com</span>
          <span style="color:var(--text-light);font-size:11px;">~1,349 non-branded visits/mo</span>
        </div>
        <div style="display:flex;height:20px;border-radius:4px;overflow:hidden;">
          <div style="width:71%;background:#8E44AD;" title="71% non-branded"></div>
          <div style="width:29%;background:#e9ecef;" title="29% branded"></div>
        </div>
        <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--text-light);margin-top:2px;">
          <span style="color:#8E44AD;font-weight:600;">71% non-branded</span><span>29% branded</span>
        </div>
      </div>

      <div class="annotation info" style="margin-top:8px;">
        CASR generates 7x more discovery traffic than CEU Matrix despite identical authority scores. The entire delta is content: CASR has credential research pages that rank for generic searches. CEU Matrix does not.
      </div>
    </div>

  </div>
</div>

<!-- Competitor Analysis — CASR -->
<div class="slide">
  <div class="slide-label">Competitor Analysis</div>
  <h2>CASR (centerforaddictionstudies.com)</h2>
  <p class="subtitle" style="margin-bottom:14px;">Same authority score as CEU Matrix. 7x more traffic. The gap is entirely content: CASR built the credential research pages that capture discovery searches.</p>

  <!-- Comparison cards -->
  <div style="display:flex;gap:12px;margin-bottom:16px;">
    <div class="stat-card" style="flex:1;text-align:center;">
      <div style="font-size:11px;color:var(--text-light);margin-bottom:4px;">Authority Score</div>
      <div style="display:flex;align-items:center;justify-content:center;gap:10px;">
        <div><div style="font-size:26px;font-weight:800;color:var(--ceu-teal);">22</div><div style="font-size:10px;color:var(--text-light);">You</div></div>
        <div style="font-size:18px;color:var(--border);">|</div>
        <div><div style="font-size:26px;font-weight:800;color:var(--ember-red);">24</div><div style="font-size:10px;color:var(--text-light);">CASR</div></div>
      </div>
    </div>
    <div class="stat-card" style="flex:1;text-align:center;">
      <div style="font-size:11px;color:var(--text-light);margin-bottom:4px;">Monthly Traffic</div>
      <div style="display:flex;align-items:center;justify-content:center;gap:10px;">
        <div><div style="font-size:26px;font-weight:800;color:var(--ceu-teal);">769</div><div style="font-size:10px;color:var(--text-light);">You</div></div>
        <div style="font-size:18px;color:var(--border);">|</div>
        <div><div style="font-size:26px;font-weight:800;color:var(--ember-red);">1,900</div><div style="font-size:10px;color:var(--text-light);">CASR</div></div>
      </div>
    </div>
    <div class="stat-card" style="flex:1;text-align:center;">
      <div style="font-size:11px;color:var(--text-light);margin-bottom:4px;">Ranking Keywords</div>
      <div style="display:flex;align-items:center;justify-content:center;gap:10px;">
        <div><div style="font-size:26px;font-weight:800;color:var(--ceu-teal);">894</div><div style="font-size:10px;color:var(--text-light);">You</div></div>
        <div style="font-size:18px;color:var(--border);">|</div>
        <div><div style="font-size:26px;font-weight:800;color:var(--ember-red);">3,000</div><div style="font-size:10px;color:var(--text-light);">CASR</div></div>
      </div>
    </div>
    <div class="stat-card" style="flex:1;text-align:center;">
      <div style="font-size:11px;color:var(--text-light);margin-bottom:4px;">Non-branded Traffic</div>
      <div style="display:flex;align-items:center;justify-content:center;gap:10px;">
        <div><div style="font-size:26px;font-weight:800;color:var(--ceu-teal);">33%</div><div style="font-size:10px;color:var(--text-light);">You</div></div>
        <div style="font-size:18px;color:var(--border);">|</div>
        <div><div style="font-size:26px;font-weight:800;color:var(--ember-red);">94%</div><div style="font-size:10px;color:var(--text-light);">CASR</div></div>
      </div>
    </div>
  </div>

  <div class="two-col" style="gap:24px;align-items:start;margin-bottom:12px;">
    <div>
      <h3 style="margin-bottom:8px;color:var(--red);">What CASR Does Well</h3>
      <ul style="list-style:none;display:flex;flex-direction:column;gap:7px;font-size:12.5px;line-height:1.5;">
        <li style="padding:7px 11px;background:#FFEBEE;border-radius:5px;border-left:3px solid var(--red);">Deep Ohio credential pages for CDCA, LICDC, and MAADC with requirements, exam prep, and renewal guides on each</li>
        <li style="padding:7px 11px;background:#FFEBEE;border-radius:5px;border-left:3px solid var(--red);">OCDP Provider citation on every applicable page, building state-specific trust signals</li>
        <li style="padding:7px 11px;background:#FFEBEE;border-radius:5px;border-left:3px solid var(--red);">Consistent internal linking: hub pages link down to credential pages, credential pages link back up</li>
      </ul>
    </div>
    <div>
      <h3 style="margin-bottom:8px;color:var(--green);">Where CEU Matrix Wins</h3>
      <ul style="list-style:none;display:flex;flex-direction:column;gap:7px;font-size:12.5px;line-height:1.5;">
        <li style="padding:7px 11px;background:#E8F5E9;border-radius:5px;border-left:3px solid var(--green);">Multi-state coverage: OCDP, NAADAC, IC&amp;RC, CADC, CSAC approvals. CASR is Ohio-only.</li>
        <li style="padding:7px 11px;background:#E8F5E9;border-radius:5px;border-left:3px solid var(--green);">Criminal justice credentials (CJCA/CCJP): CASR has zero content here — defensible moat for CEU Matrix</li>
        <li style="padding:7px 11px;background:#E8F5E9;border-radius:5px;border-left:3px solid var(--green);">No AI infrastructure: no llms.txt, no FAQ or HowTo schema. CEU Matrix appears in AI Overviews where CASR does not.</li>
        <li style="padding:7px 11px;background:#E8F5E9;border-radius:5px;border-left:3px solid var(--green);">6x more referring domains (1,200 vs 189). Once content pages exist, existing link equity accelerates rankings.</li>
      </ul>
    </div>
  </div>

  <div class="annotation">
    <strong>M2 priority:</strong> Ohio hub to 4,000+ words, OCDP Provider #50-19236 on every Ohio page, FAQ schema on CDCA and LICDC pages. Every CASR advantage flipped by end of M2.
  </div>
</div>

<!-- Competitor Analysis — CE4Less -->
<div class="slide">
  <div class="slide-label">Competitor Analysis</div>
  <h2>CE4Less (ce4less.com)</h2>
  <p class="subtitle" style="margin-bottom:14px;">The traffic leader — but 84% of those visits come from branded searches. Discovery traffic is 5,152/mo, barely 20x CEU Matrix. Breadth is their moat; depth is the counterstrategy.</p>

  <!-- Comparison cards -->
  <div style="display:flex;gap:12px;margin-bottom:16px;">
    <div class="stat-card" style="flex:1;text-align:center;">
      <div style="font-size:11px;color:var(--text-light);margin-bottom:4px;">Authority Score</div>
      <div style="display:flex;align-items:center;justify-content:center;gap:10px;">
        <div><div style="font-size:26px;font-weight:800;color:var(--ceu-teal);">22</div><div style="font-size:10px;color:var(--text-light);">You</div></div>
        <div style="font-size:18px;color:var(--border);">|</div>
        <div><div style="font-size:26px;font-weight:800;color:var(--ember-red);">38</div><div style="font-size:10px;color:var(--text-light);">CE4Less</div></div>
      </div>
    </div>
    <div class="stat-card" style="flex:1;text-align:center;">
      <div style="font-size:11px;color:var(--text-light);margin-bottom:4px;">Monthly Traffic</div>
      <div style="display:flex;align-items:center;justify-content:center;gap:10px;">
        <div><div style="font-size:26px;font-weight:800;color:var(--ceu-teal);">769</div><div style="font-size:10px;color:var(--text-light);">You</div></div>
        <div style="font-size:18px;color:var(--border);">|</div>
        <div><div style="font-size:26px;font-weight:800;color:var(--ember-red);">32.2K</div><div style="font-size:10px;color:var(--text-light);">CE4Less</div></div>
      </div>
    </div>
    <div class="stat-card" style="flex:1;text-align:center;">
      <div style="font-size:11px;color:var(--text-light);margin-bottom:4px;">Ref. Domains</div>
      <div style="display:flex;align-items:center;justify-content:center;gap:10px;">
        <div><div style="font-size:26px;font-weight:800;color:var(--green);">1,200</div><div style="font-size:10px;color:var(--text-light);">You</div></div>
        <div style="font-size:18px;color:var(--border);">|</div>
        <div><div style="font-size:26px;font-weight:800;color:var(--ember-red);">957</div><div style="font-size:10px;color:var(--text-light);">CE4Less</div></div>
      </div>
    </div>
    <div class="stat-card" style="flex:1;text-align:center;">
      <div style="font-size:11px;color:var(--text-light);margin-bottom:4px;">Non-branded Traffic</div>
      <div style="display:flex;align-items:center;justify-content:center;gap:10px;">
        <div><div style="font-size:26px;font-weight:800;color:var(--ceu-teal);">33%</div><div style="font-size:10px;color:var(--text-light);">You</div></div>
        <div style="font-size:18px;color:var(--border);">|</div>
        <div><div style="font-size:26px;font-weight:800;color:var(--ember-red);">16%</div><div style="font-size:10px;color:var(--text-light);">CE4Less</div></div>
      </div>
    </div>
  </div>

  <div class="two-col" style="gap:24px;align-items:start;margin-bottom:12px;">
    <div>
      <h3 style="margin-bottom:8px;color:var(--red);">What CE4Less Does Well</h3>
      <ul style="list-style:none;display:flex;flex-direction:column;gap:7px;font-size:12.5px;line-height:1.5;">
        <li style="padding:7px 11px;background:#FFEBEE;border-radius:5px;border-left:3px solid var(--red);">957 referring domains including 45 links from naadac.org alone — built through years of directory submissions across all licensed professions</li>
        <li style="padding:7px 11px;background:#FFEBEE;border-radius:5px;border-left:3px solid var(--red);">Large multi-profession course catalog creating thousands of indexed pages and long-tail keyword coverage</li>
        <li style="padding:7px 11px;background:#FFEBEE;border-radius:5px;border-left:3px solid var(--red);">CE broker platform listings (CE Broker, CECH) that generate passive backlinks and referral traffic</li>
      </ul>
    </div>
    <div>
      <h3 style="margin-bottom:8px;color:var(--green);">Where CEU Matrix Wins</h3>
      <ul style="list-style:none;display:flex;flex-direction:column;gap:7px;font-size:12.5px;line-height:1.5;">
        <li style="padding:7px 11px;background:#E8F5E9;border-radius:5px;border-left:3px solid var(--green);">CEU Matrix already has more referring domains (1,200 vs 957). The link foundation is stronger — the content pages just need to be built.</li>
        <li style="padding:7px 11px;background:#E8F5E9;border-radius:5px;border-left:3px solid var(--green);">Topical authority: CE4Less serves all licensed professions. Google rewards a site that exclusively covers addiction counselor credentials.</li>
        <li style="padding:7px 11px;background:#E8F5E9;border-radius:5px;border-left:3px solid var(--green);">State compliance depth: CE4Less has no Ohio CDCA page, no LICDC renewal guide, no LCDC Texas hub. Every state page CEU Matrix builds is unchallenged.</li>
      </ul>
    </div>
  </div>

  <div class="annotation info">
    <strong>CE4Less's dominance is brand traffic, not content traffic.</strong> Their non-branded discovery is only ~5K/mo. Niche-specific credential pages CEU Matrix builds are not content CE4Less competes for.
  </div>
</div>

<!-- Competitor Analysis — AllCEUs -->
<div class="slide">
  <div class="slide-label">Competitor Analysis</div>
  <h2>AllCEUs (allceus.com)</h2>
  <p class="subtitle" style="margin-bottom:14px;">Similar authority and traffic to CASR, but 71% non-branded traffic means they rank on discovery. Their weakness: mental health generalist. No addiction-counselor-specific positioning anywhere on the site.</p>

  <!-- Comparison cards -->
  <div style="display:flex;gap:12px;margin-bottom:16px;">
    <div class="stat-card" style="flex:1;text-align:center;">
      <div style="font-size:11px;color:var(--text-light);margin-bottom:4px;">Authority Score</div>
      <div style="display:flex;align-items:center;justify-content:center;gap:10px;">
        <div><div style="font-size:26px;font-weight:800;color:var(--ceu-teal);">22</div><div style="font-size:10px;color:var(--text-light);">You</div></div>
        <div style="font-size:18px;color:var(--border);">|</div>
        <div><div style="font-size:26px;font-weight:800;color:var(--ember-red);">28</div><div style="font-size:10px;color:var(--text-light);">AllCEUs</div></div>
      </div>
    </div>
    <div class="stat-card" style="flex:1;text-align:center;">
      <div style="font-size:11px;color:var(--text-light);margin-bottom:4px;">Monthly Traffic</div>
      <div style="display:flex;align-items:center;justify-content:center;gap:10px;">
        <div><div style="font-size:26px;font-weight:800;color:var(--ceu-teal);">769</div><div style="font-size:10px;color:var(--text-light);">You</div></div>
        <div style="font-size:18px;color:var(--border);">|</div>
        <div><div style="font-size:26px;font-weight:800;color:var(--ember-red);">1,900</div><div style="font-size:10px;color:var(--text-light);">AllCEUs</div></div>
      </div>
    </div>
    <div class="stat-card" style="flex:1;text-align:center;">
      <div style="font-size:11px;color:var(--text-light);margin-bottom:4px;">Ranking Keywords</div>
      <div style="display:flex;align-items:center;justify-content:center;gap:10px;">
        <div><div style="font-size:26px;font-weight:800;color:var(--ceu-teal);">894</div><div style="font-size:10px;color:var(--text-light);">You</div></div>
        <div style="font-size:18px;color:var(--border);">|</div>
        <div><div style="font-size:26px;font-weight:800;color:var(--ember-red);">2,100</div><div style="font-size:10px;color:var(--text-light);">AllCEUs</div></div>
      </div>
    </div>
    <div class="stat-card" style="flex:1;text-align:center;">
      <div style="font-size:11px;color:var(--text-light);margin-bottom:4px;">Non-branded Traffic</div>
      <div style="display:flex;align-items:center;justify-content:center;gap:10px;">
        <div><div style="font-size:26px;font-weight:800;color:var(--ceu-teal);">33%</div><div style="font-size:10px;color:var(--text-light);">You</div></div>
        <div style="font-size:18px;color:var(--border);">|</div>
        <div><div style="font-size:26px;font-weight:800;color:var(--ember-red);">71%</div><div style="font-size:10px;color:var(--text-light);">AllCEUs</div></div>
      </div>
    </div>
  </div>

  <div class="two-col" style="gap:24px;align-items:start;margin-bottom:12px;">
    <div>
      <h3 style="margin-bottom:8px;color:var(--red);">What AllCEUs Does Well</h3>
      <ul style="list-style:none;display:flex;flex-direction:column;gap:7px;font-size:12.5px;line-height:1.5;">
        <li style="padding:7px 11px;background:#FFEBEE;border-radius:5px;border-left:3px solid var(--red);">1,000 referring domains from mental health, counseling, and social work directories — steady passive acquisition through CE broker integrations</li>
        <li style="padding:7px 11px;background:#FFEBEE;border-radius:5px;border-left:3px solid var(--red);">71% non-branded traffic: ranking on generic mental health continuing education terms gives discovery coverage across professions</li>
        <li style="padding:7px 11px;background:#FFEBEE;border-radius:5px;border-left:3px solid var(--red);">Multiple course formats (video, audio, text) and affordable pricing maximize conversion across diverse learner profiles</li>
      </ul>
    </div>
    <div>
      <h3 style="margin-bottom:8px;color:var(--green);">Where CEU Matrix Wins</h3>
      <ul style="list-style:none;display:flex;flex-direction:column;gap:7px;font-size:12.5px;line-height:1.5;">
        <li style="padding:7px 11px;background:#E8F5E9;border-radius:5px;border-left:3px solid var(--green);">Addiction counselor exclusivity: AllCEUs covers all mental health professions. CEU Matrix's IC&amp;RC, NAADAC, and OCDP specificity builds topical authority AllCEUs cannot match in this niche.</li>
        <li style="padding:7px 11px;background:#E8F5E9;border-radius:5px;border-left:3px solid var(--green);">State compliance pages: no Ohio CDCA page, no LICDC renewal guide, no LCDC Texas hub. Every state hub CEU Matrix builds is uncontested by AllCEUs.</li>
        <li style="padding:7px 11px;background:#E8F5E9;border-radius:5px;border-left:3px solid var(--green);">Criminal justice credentials: zero AllCEUs content for CJCA/CCJP. Entirely uncontested territory starting M3.</li>
      </ul>
    </div>
  </div>

  <div class="annotation success">
    <strong>AllCEUs is the easiest competitor to outrank in this niche.</strong> Their authority comes from breadth across all mental health professions. Every state page and credential page CEU Matrix builds captures traffic AllCEUs is not competing for.
  </div>
</div>"""

html = html[:start_idx] + NEW_CONTENT + html[end_idx:]
print(f"Inserted 5 new competitor slides ({len(NEW_CONTENT)} chars)")

with open(DECK, "w", encoding="utf-8") as f:
    f.write(html)
print("Deck saved.")
print("  1. Domain Comparison (real SEMrush data)")
print("  2. Traffic Share (donut + non-branded bars)")
print("  3. CASR (comparison cards + streamlined bullets)")
print("  4. CE4Less (comparison cards + streamlined bullets)")
print("  5. AllCEUs (comparison cards + streamlined bullets)")
