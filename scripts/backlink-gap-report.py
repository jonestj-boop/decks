#!/usr/bin/env python3
"""
Replace the two-col domain categories / acquisition plan tables + internal annotation note
on the Backlink Gap slide with the actual SEMrush gap report table.
"""

DECK = "/Users/deannaspallone/Documents/Claude Projects/embertribe-decks/decks/ceu-matrix-seo-foundation.html"

with open(DECK, "r", encoding="utf-8") as f:
    html = f.read()

OLD = """  <div class="two-col" style="gap:24px;margin-bottom:20px;align-items:start;">
    <div>
      <h3 style="margin-bottom:10px;">Domain Categories in the Gap</h3>
      <table>
        <thead><tr><th class="th-red">Domain Type</th><th class="th-red">Why CASR Has It</th><th class="th-red">How CEU Matrix Gets In</th></tr></thead>
        <tbody>
          <tr><td><strong>State board directories</strong></td><td class="dim">CASR is OCDP-listed in Ohio</td><td>CEU Matrix is OCDP #50-19236 — submit listing update</td></tr>
          <tr><td><strong>NAADAC chapter sites</strong></td><td class="dim">CASR is an active NAADAC affiliate</td><td>CEU Matrix holds Provider #94564 (since 2005) — request partner listing</td></tr>
          <tr><td><strong>IC&amp;RC member board pages</strong></td><td class="dim">CASR is IC&amp;RC approved and listed</td><td>CEU Matrix is IC&amp;RC approved — request board directory entry</td></tr>
          <tr><td><strong>Addiction treatment directories</strong></td><td class="dim">CASR actively submits to niche directories</td><td>Manual outreach to 20+ addiction resource directories</td></tr>
          <tr><td><strong>State counseling associations</strong></td><td class="dim">CASR sponsors state-level orgs</td><td>Outreach to TX, PA, OH counseling associations</td></tr>
          <tr><td><strong>Criminal justice resource sites</strong></td><td class="dim">Minimal — gap exists for CASR too</td><td>First-mover advantage via IC&amp;RC CJ-affiliated outreach</td></tr>
        </tbody>
      </table>
    </div>
    <div>
      <h3 style="margin-bottom:10px;">Monthly Acquisition Plan</h3>
      <table>
        <thead><tr><th class="th-red">Month</th><th class="th-red">Links</th><th class="th-red">Domain Focus</th></tr></thead>
        <tbody>
          <tr><td><strong>Month 2</strong></td><td>6</td><td class="dim">State board directories, NAADAC affiliates, OH/TX/PA counseling associations</td></tr>
          <tr><td><strong>Month 3</strong></td><td>6</td><td class="dim">IC&amp;RC member boards, addiction treatment orgs, CJ-adjacent resource sites</td></tr>
          <tr><td><strong>Month 4</strong></td><td>6</td><td class="dim">Higher-DA directories, TX/PA board resources, top-performing pages from GSC data</td></tr>
        </tbody>
      </table>
      <div style="background:#E8F5E9;border-left:3px solid var(--green);padding:10px 14px;border-radius:0 8px 8px 0;font-size:13px;margin-top:12px;">
        <strong style="color:#2E7D32;">Why this beats cold outreach:</strong> Every domain in the report already links to competitors in this exact vertical. Relevance is pre-qualified. Acquisition rate is 3x higher than non-gap prospecting.
      </div>
    </div>
  </div>

  <div class="annotation info">
    <strong>Report format:</strong> Domain name · DA score · page that links to CASR · recommended anchor text for CEU Matrix · outreach pathway (directory submission, partner request, or editorial). Your link vendor works from this list directly starting in M2.
  </div>"""

NEW = """  <div style="display:flex;gap:12px;margin-bottom:14px;">
    <div class="stat-card" style="min-width:auto;padding:8px 16px;">
      <div class="stat-value" style="font-size:22px;">3</div>
      <div class="stat-label">competitors analyzed</div>
    </div>
    <div class="stat-card" style="min-width:auto;padding:8px 16px;">
      <div class="stat-value" style="font-size:22px;">18</div>
      <div class="stat-label">target domains identified</div>
    </div>
    <div class="stat-card" style="min-width:auto;padding:8px 16px;">
      <div class="stat-value" style="font-size:22px;">3x</div>
      <div class="stat-label">higher acquisition rate vs. cold outreach</div>
    </div>
  </div>

  <table style="font-size:11.5px;width:100%;">
    <thead>
      <tr>
        <th class="th-red" style="width:19%;">Domain</th>
        <th class="th-red" style="width:4%;">DA</th>
        <th class="th-red" style="width:16%;">Links to</th>
        <th class="th-red" style="width:38%;">Anchor text rec</th>
        <th class="th-red" style="width:23%;">Pathway</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>naadac.org</td><td>40</td><td class="dim">CE4Less &times;45</td><td>NAADAC-approved CEU provider for addiction counselors</td><td style="color:#27AE60;font-weight:600;">Partner listing</td></tr>
      <tr><td>psychology.org</td><td>50</td><td class="dim">CE4Less, AllCEUs</td><td>addiction counselor continuing education online</td><td style="color:#E67E22;font-weight:600;">Resource listing</td></tr>
      <tr><td>theraplatform.com</td><td>44</td><td class="dim">CE4Less, AllCEUs</td><td>online CEU courses for addiction counselors</td><td style="color:#E67E22;font-weight:600;">Partner request</td></tr>
      <tr><td>socialworklicensemap.com</td><td>43</td><td class="dim">CE4Less, AllCEUs</td><td>CEU requirements for addiction counselor license renewal</td><td style="color:#8E44AD;font-weight:600;">Directory submission</td></tr>
      <tr><td>mhacbo.org</td><td>34</td><td class="dim">CASR, CE4Less</td><td>Ohio OCDP-approved CEU provider</td><td style="color:#27AE60;font-weight:600;">Partner listing</td></tr>
      <tr><td>wvsocialworkboard.org</td><td>31</td><td class="dim">CE4Less &times;3</td><td>approved CE provider for WV substance abuse counselors</td><td style="color:#2980B9;font-weight:600;">CE provider directory</td></tr>
      <tr><td>minnesotarecovery.org</td><td>30</td><td class="dim">CE4Less, AllCEUs</td><td>addiction counselor continuing education online</td><td style="color:#E67E22;font-weight:600;">Resource listing</td></tr>
      <tr><td>substanceabusecounselor.org</td><td>26</td><td class="dim">CASR &times;6, AllCEUs &times;3</td><td>NAADAC-approved online CEUs for substance abuse counselors</td><td style="color:#27AE60;font-weight:600;">Partner listing</td></tr>
      <tr><td>careersofsubstance.org</td><td>25</td><td class="dim">CASR &times;2</td><td>substance abuse counselor CEU courses</td><td style="color:#E67E22;font-weight:600;">Resource listing</td></tr>
      <tr><td>ipggc.org</td><td>25</td><td class="dim">CASR &times;8, CE4Less &times;3</td><td>IC&amp;RC-approved continuing education provider</td><td style="color:#2980B9;font-weight:600;">CE provider directory</td></tr>
      <tr><td>nevadacertboard.org</td><td>24</td><td class="dim">CE4Less</td><td>Nevada LADC CEU courses online</td><td style="color:#2980B9;font-weight:600;">CE provider directory</td></tr>
      <tr><td>socialworkdegreecenter.com</td><td>24</td><td class="dim">CE4Less &times;2, AllCEUs</td><td>continuing education for licensed addiction counselors</td><td style="color:#E67E22;font-weight:600;">Resource listing</td></tr>
      <tr><td>ibadcc.org</td><td>20</td><td class="dim">CE4Less</td><td>NAADAC-approved addiction counselor CE courses</td><td style="color:#2980B9;font-weight:600;">CE provider directory</td></tr>
      <tr><td>nextstepintervention.com</td><td>18</td><td class="dim">CASR, AllCEUs</td><td>online addiction counselor continuing education</td><td style="color:#E67E22;font-weight:600;">Partner request</td></tr>
      <tr><td>tncertification.org</td><td>17</td><td class="dim">CASR &times;2, AllCEUs</td><td>Tennessee LADAC continuing education provider</td><td style="color:#2980B9;font-weight:600;">CE provider directory</td></tr>
      <tr><td>getlicensemap.com</td><td>11</td><td class="dim">CASR &times;2, CE4Less &times;2</td><td>addiction counselor CEUs by state</td><td style="color:#8E44AD;font-weight:600;">Directory submission</td></tr>
      <tr><td>substanceabusecertification.org</td><td>8</td><td class="dim">CASR &times;2, AllCEUs</td><td>accredited substance abuse counselor CE courses</td><td style="color:#2980B9;font-weight:600;">CE provider directory</td></tr>
      <tr><td>floridasocialworkedu.org</td><td>11</td><td class="dim">CE4Less</td><td>Florida CAP approved online CEU provider</td><td style="color:#2980B9;font-weight:600;">CE provider directory</td></tr>
    </tbody>
  </table>"""

if OLD not in html:
    print("ERROR: old block not found — check whitespace")
    exit(1)

html = html.replace(OLD, NEW, 1)
print("Replaced backlink gap two-col + annotation with 18-row report table")

with open(DECK, "w", encoding="utf-8") as f:
    f.write(html)
print("Done — deck saved.")
