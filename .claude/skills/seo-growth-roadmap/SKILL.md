# SEO Growth Roadmap Skill

Produce a tripwire-priced ($97–$197) SEO growth roadmap for a prospect —
**two deliverables** that the sales team presents on a strategy call:

1. **Opportunity deck** (13-slide HTML) — opportunity-first narrative including the integrated 90-day content plan; ends on the projected trajectory
2. **Keyword research workbook** (xlsx) — full keyword universe, 4 sheets (Article Plan, Universe, Excluded, Read Me)

The deck is the cohesive presentation surface. The spreadsheet is the receipt
the prospect can sort, filter, and forward to internal stakeholders. Both live
at `decks.embertribe.com`.

**Visual references:**
- Deck (slides 1–9, 13): `embertribe-clients/ceu-matrix/seo-foundation.html` (CEU Matrix Foundation)
- Content plan slides (10–12): `embertribe-clients/entraworld/3-month-content-plan.html` (Entraworld plan, integrated into the deck)
- Synthetic dial-in: `embertribe-decks/decks/coastal-crate-pet-co-*`

**Companion skill:** `seo-foundation` is the *paid client* Month 1 deliverable.
This skill is the *pre-sale* tripwire that demonstrates opportunity. They share
scripts and visual system; they do not share scope. Deliverables here are
designed to be presented on a sales call — not handed off as a finished plan.

---

## When to Use

- Sales team running a report ahead of a discovery call ("warm" mode, has call notes)
- Self-serve from the GHL landing page after a buyer pays $97/$197 ("cold" mode)
- User says "run an SEO growth roadmap for {prospect}"
- User says "build a tripwire deck for {prospect}"

---

## Output

Two repos receive output:

```
embertribe-decks/decks/                                ← SALES-FACING DELIVERABLES
├── images/
│   └── casestudy-500k.jpg                               shared case-study screenshot (used by every client)
└── {client-slug}/                                       per-client folder
    ├── growth-roadmap.html                      the 13-slide deck (includes content plan)
    └── keyword-research.xlsx                            the full keyword workbook (NOT linked publicly)

The deck deploys to decks.embertribe.com/{client-slug}/growth-roadmap.html.
The xlsx lives in the same folder for organizational reasons but isn't linked
from anywhere public — sales team grabs it via the repo or shares directly
with the prospect via email/GHL.

EmberTribe/site/clients/{prospect-slug}/               ← WORKING DATA (internal)
└── growth-roadmap/
    ├── intake.json                  Prospect inputs (URL, brand, competitors, services)
    ├── crawl-results.json
    ├── pagespeed-results.json
    ├── ga4-baseline.json            (only if connected)
    ├── gsc-baseline.json            (only if connected)
    └── semrush/
        ├── domain-overview-{domain}.csv
        ├── organic-positions.csv
        ├── keyword-gap.csv
        ├── keyword-strategy-builder.csv     (full keyword universe export)
        └── backlink-gap.csv
```

The bundle goes to `embertribe-decks` (Cloudflare Pages auto-deploys to
`decks.embertribe.com`). Working data stays in `EmberTribe/site/clients/`.

---

## Phase 0: Intake

Required:
- Prospect name + website URL
- Brand terms (for branded/non-branded GSC classification, even if GSC isn't connected — used to filter SEMrush queries)
- Mode: `warm` (sales team, has call notes) or `cold` (self-serve, post-payment)

In `warm` mode also collect:
- Known competitors (2–4)
- Services they're interested in (informs the "What's Possible" slide)
- Any pain points / urgency signals from the call (informs framing)

In `cold` mode the GHL form should capture:
- Main services / product categories
- Known competitors (optional, surface from SEMrush if blank)
- Whether they want to connect GA4/GSC for richer data (Y/N)

If `cold` mode and the buyer connects analytics, run the enrichment path
(see Phase 1d). If not, skip GA4/GSC and rely on SEMrush + crawl.

---

## Phase 1: Data Collection

### 1a. Site Crawl (always run — automatic)

```bash
python3 scripts/site-crawl.py \
  --site "{site_url}" \
  --max-pages 100 \
  --output site/clients/{slug}/growth-roadmap/crawl-results.json
```

100 pages is the cap for tripwire-tier — the full 500-page Foundation crawl
is overkill for this deliverable. ~5 minutes for most sites.

Flags broken links, missing meta, multiple H1s, thin content, missing schema,
and pages with low internal-link counts.

### 1b. PageSpeed Insights (always run — automatic)

```bash
python3 scripts/pagespeed-api.py \
  --url "{homepage}" \
  --url "{top-product-page}" \
  --url "{top-content-page}" \
  --api-key "{PAGESPEED_API_KEY}" \
  --output site/clients/{slug}/growth-roadmap/pagespeed-results.json
```

Homepage + 2 top pages. Identify mobile + desktop scores, LCP/FID/CLS, top
diagnostic flags.

### 1c. SEMrush exports (always required — manual upload)

Prompt the operator to export and drop into `site/clients/{slug}/growth-roadmap/semrush/`:

| Report | SEMrush path | File name |
|--------|-------------|-----------|
| Domain Overview | Domain Overview → export | `domain-overview-{domain}.csv` (one per competitor too) |
| Organic Positions | Organic Research → Positions → Top 200 by traffic % → export | `organic-positions.csv` |
| Keyword Gap | Keyword Gap → client + 2–3 competitors → Missing + Weak → export | `keyword-gap.csv` |
| Backlink Gap | Backlink Gap → all domains → Unique to competitors → export | `backlink-gap.csv` |

If competitors weren't named in intake, surface the top 3 organic competitors
from the Organic Research → Competitors tab and use those.

**v1.5 path:** swap the manual SEMrush exports for programmatic DataForSEO
calls — see Section "Future: DataForSEO" at the bottom. Wire this when buyer
volume justifies the API spend (~$0.50 per roadmap).

### 1d. GA4 + GSC (optional enrichment)

Only run if the prospect has connected analytics. Two paths:

**Path A — Manual service account add (MVP default):**
The prospect adds `embertribe-content-tools@embertribe-content-tools.iam.gserviceaccount.com`
as Viewer in GA4 and Restricted in GSC. Then:

```bash
python3 scripts/ga4-baseline.py --property {ga4_id} --months 6 --output site/clients/{slug}/growth-roadmap/ga4-baseline.json
python3 scripts/gsc-baseline.py --site "{gsc_url}" --brand "{brand1}" --brand "{brand2}" --days 90 --output site/clients/{slug}/growth-roadmap/gsc-baseline.json
```

**Path B — Windsor.ai (planned, v1.5):**
Buyer clicks "Connect Google" in the GHL onboarding flow → Windsor.ai's verified
OAuth app handles consent → connection lands in our Windsor workspace → we pull
via Windsor's API. See `scripts/windsor-fetch.py` (TBD).

The fetch should be isolated behind `analytics.fetch_baseline(prospect)` so
swapping Path A → Path B is one wrapper change. If neither path runs, the deck
gracefully omits the GA4 trend slide and the branded/non-branded donut, falling
back to SEMrush-derived organic traffic.

### 1e. Brand colors (for theming)

Visit the prospect's site and pull 2–3 brand colors from the homepage header /
hero section. Map to `--client-dark`, `--client-mid`, `--client-accent` in the
deck CSS variables.

---

## Phase 2: Analysis

Synthesize across data sources to identify the headline opportunity.

### Opportunity sizing (the hook)

From `keyword-gap.csv`, calculate:
- Sum of monthly search volume for top 10 missing keywords (where the prospect doesn't rank but at least one competitor does in top 10)
- Estimated traffic value if ranking position 5 for each (assume 15% CTR)
- Format as headline number on cover stat card

### Striking distance opportunities

From either GSC (if connected) or `organic-positions.csv` (always available):
- Filter to keywords ranking positions 11–30
- Sort by search volume × (1 / current_position)
- Top 8–10 candidates for the "Striking Distance" slide

These are the fast-win narrative — "you're already ranking, just one push from page 1."

### Tech triage

From `crawl-results.json` + `pagespeed-results.json`:
- **P1 (Fix in M1)** — broken links at scale, indexation blockers, canonical errors, mobile LCP > 4s
- **P2 (Fix in M2)** — missing meta descriptions, multiple H1s template-level, thin content on traffic pages
- **P3 (Monitor)** — image alt text, low-priority schema gaps

Pick the top 5 issues across P1+P2 for the slide. Show count of affected pages, not URLs (URLs go in the working JSON if they want to dig).

### Competitor gap

From `domain-overview-*.csv`:
- Authority score / traffic / keywords / referring domains for prospect + top 3 competitors
- Calculate the "biggest gap" metric to lead with (usually keyword count)
- If prospect's referring domains > competitor's but traffic < competitor's, frame as "link foundation is already there, content is the unlock"

### Projection model

Same model as `seo-foundation`, conservative:
```
Baseline = most recent monthly organic (GA4 if connected, else SEMrush traffic estimate)
M3  = baseline × 1.07–1.15
M6  = baseline × 1.25–1.40
M12 = baseline × 1.60–1.80
```

These are directional, never guaranteed. Always include the disclaimer:
"These are directional projections, not guarantees" (per `sales/SALES-PARAMETERS.md` §5B).

---

## Phase 3: Deck Assembly

### Template

Copy structure + CSS from `embertribe-clients/ceu-matrix/seo-foundation.html`.
Keep the slide framework, color tokens, chart components, stat cards. Replace
all CEU-specific content with prospect data.

### Theming

```css
:root {
  --client-dark:   {prospect dark color};
  --client-mid:    {prospect mid tone};
  --client-accent: {prospect accent / CTA color};
  --ember-red:     #ff333d;   /* always stays */
}
```

Dark slides: `linear-gradient(135deg, var(--client-dark) 0%, var(--client-mid) 50%, [third-tone] 100%)`

### Slide structure (13 slides — opportunity-first, content plan integrated, no CTA)

The deck is **presented on a sales call** — not handed off as a finished plan.
That means: no CTA slide (the call IS the CTA), no AEO case study (focus on
ClusterMagic only), and the trajectory slide is the closer. The 90-day content
plan is integrated as slides 10–12 so the prospect sees the full arc — gap →
plan → projection — in a single navigable surface.

| # | Slide | Type | Source | Purpose |
|---|-------|------|--------|---------|
| 1 | **Cover** | Dark | Intake + analysis | Prospect name, 4 stat cards: current organic (GA4 verified if connected) / opportunity gap / M12 target / EmberTribe years (4+) |
| 2 | **The big opportunity** | Light | keyword-gap.csv | Top 10 missing keywords + total monthly search volume + traffic value at pos 5. **Lead with this — the buyer paid to feel the gap.** |
| 3 | **Striking distance** | Light | GSC if connected, else organic-positions.csv | 8–10 keywords ranking 11–30. Annotation reframes for connected vs unconnected — the GSC version surfaces 3–5x more total striking-distance keywords (note count). |
| 4 | **Where you stand** *(conditional)* | Light | GA4 + GSC if connected, else SEMrush | **Two paths — see Conditional Analytics below.** Connected: GA4 6-month trend + GSC click mix donut + top non-branded queries. Not connected: SEMrush traffic estimate trend + site health snapshot stat cards. |
| 5 | **Tech roadblocks** | Light | crawl-results + pagespeed | Top 5 issues with P1/P2/P3 priority pills, affected page counts, "what fixing these unlocks" |
| 6 | **The competitor gap** | Light | domain-overview CSVs | Comparison table: prospect vs 2–3 competitors on traffic, keywords, refdomains, auth score. Bar chart. |
| 7 | **Section divider: How we capture it** | Red-full | — | Transition slide. Big text: "ClusterMagic." |
| 8 | **The ClusterMagic engine** | Dark | — | 3-column: Entity-rich content / AI-powered execution / Compounds over 4+ years. Mirror RankStack framing without naming it. |
| 9 | **Case study: 8,500/mo → 500K** | Light | ClusterMagic webinar | Real SEMrush screenshot (`images/casestudy-500k.jpg`) + headline metrics: ~59x growth, $20M Series A, ~$2M impression-share value, zero algorithm penalties across 4+ years |
| 10 | **Content Plan Overview** | Light | content-plan analysis | 4 stat cards (article count, total monthly searches, easy-win count, avg KD) + Coverage by Pillar bar chart + Funnel Mix bar chart |
| 11 | **The 120 Articles** | Light | content-plan analysis | Inline month tabs (M1 / M2 / M3) with sticky positioning. Each tab shows 40-row article table with pillar/funnel/intent chips + KD pills. Slide is internally scrollable. |
| 12 | **Why This Plan** | Light | content-plan analysis | 4 pillar cards with color-coded borders + "What we deliberately excluded" bullets + 4-step expectation timeline + "How each article is built" paragraph |
| 13 | **Your projected trajectory** | Dark | Projection model | Line chart with M3 / M6 / M12 dots based on GA4 baseline (or SEMrush if not connected). Disclaimer at bottom. **This is the closing slide** — the conversation continues on the call. |

**Minimum viable deck:** Cover, Opportunity, Striking Distance, Where You Stand, Tech, Competitor Gap, ClusterMagic, Case Study, Content Plan Overview, Trajectory (10 slides) — for sites with sparse SEMrush data, drop slides 11 (full article list) and 12 (Why This Plan) and put a smaller article sample on slide 10.

### Conditional analytics — slide 4 has two paths

The skill must branch slide 4 (and parts of slides 1, 3, 13) based on whether
GA4 + GSC are connected at run-time:

**Path A — Analytics CONNECTED** (preferred — richer demo, shown in the Coastal Crate dial-in):
- Slide 1 cover stat card: "Verified monthly organic visits (GA4, [month])" using GA4's last-month value
- Slide 3 annotation: "From your verified GSC data: N total keywords are sitting in striking distance (positions 11–30) right now. The top 8 are above. The full list is in the workbook."
- Slide 4 layout: GA4 6-month trend (left col) + GSC click mix donut (33% branded / 67% non-branded — verify against UI) + top 5 non-branded GSC queries table (right col). Annotations celebrate the verified data ("verified GA4 baseline", "the long tail SEMrush misses").
- Slide 13 baseline: GA4 last-month organic sessions; legend reads "Confirmed (GA4)".

**Path B — Analytics NOT CONNECTED** (fallback):
- Slide 1 cover stat card: "Current monthly organic visits (SEMrush, [month])" using SEMrush traffic estimate
- Slide 3 annotation: "Why connecting GSC matters — GSC reveals every keyword you're ranking for, including long-tail terms SEMrush misses. Striking distance from GSC is typically 3–5x larger than what SEMrush surfaces. This deck shows the SEMrush view only."
- Slide 4 layout: SEMrush traffic estimate trend (left col) + Site Health Snapshot stat cards: DA Score, ranking kw count, refdomains, pages driving traffic (right col). Bottom annotation pitches the value of connecting analytics during onboarding.
- Slide 13 baseline: SEMrush organic traffic estimate; legend reads "Confirmed (SEMrush)".

The Coastal Crate dial-in deck (`embertribe-decks/decks/coastal-crate-pet-co-growth-roadmap.html`)
is the **Path A reference** — copy its slide 4 structure when GA4 + GSC are connected.

### Companion deliverable: Keyword research workbook (xlsx)

A 4-sheet xlsx at `embertribe-decks/decks/{slug}-keyword-research.xlsx`,
generated by `scripts/build-{slug}-keyword-research.py` (one script per
prospect — articles are inline data; reuse the Coastal Crate script as
a template):

- **Sheet 1: Article Plan** — same 120 articles as the HTML plan, with all metadata
- **Sheet 2: Keyword Universe** — full keyword research (~300–500 keywords from SEMrush Strategy Builder), planned ones flagged "Yes (planned)", overflow flagged "Overflow"
- **Sheet 3: Excluded** — high-volume keywords intentionally cut, with category and reason (off-brand / regulatory / wrong-vertical)
- **Sheet 4: Read Me** — how to interpret, why these pillars, funnel mix philosophy, what's excluded and why, next step

Use color-coded pillar fills + KD bands for quick visual scanning. Reference
script: `scripts/build-coastal-crate-keyword-research.py`.

### Visuals checklist

- [ ] Cover stat cards (4) — sourced from data, no made-up numbers
- [ ] Opportunity slide table + summary stat block (top 10 keywords + estimated click lift + traffic value)
- [ ] Striking distance table with current position + volume + projected click lift + gap column
- [ ] Trend line chart (GA4) OR SEMrush traffic block (if not connected)
- [ ] Site health snapshot stat cards (auth score, ranking kw count, refdomains, pages driving traffic)
- [ ] Tech issue table with P1/P2/P3 pills + PageSpeed mobile/desktop scores + Core Web Vitals
- [ ] Competitor comparison table + bar chart (monthly organic + pages driving traffic)
- [ ] ClusterMagic 3-col explainer with icons (Entity-rich / AI-powered / Compounds)
- [ ] Case study screenshot embedded as `<img src="images/casestudy-500k.jpg">` (must exist in `decks/images/`)
- [ ] Trajectory line chart with M3/M6/M12 dots, 0-based y-axis, dashed projection line, solid confirmed stub

All charts must be 0-based axes. No truncated y-axis.

---

## Phase 4: Save and Deliver

Save both deliverables to `embertribe-decks/decks/{client-slug}/`:

1. **Deck** → `embertribe-decks/decks/{client-slug}/growth-roadmap.html` (13 slides — content plan integrated as slides 10–12)
2. **Keyword research** → `embertribe-decks/decks/{client-slug}/keyword-research.xlsx` (run the per-client generator script — the script's output path must point at the new client folder)

Slug: lowercase, hyphens, no special chars (e.g. `coastal-crate-pet-co`).

Image references inside the deck use `../images/casestudy-500k.jpg` to reach
the shared images folder one level up.

Commit + push both repos:
- `embertribe-decks` — Cloudflare Pages auto-deploys
- `EmberTribe` — for working data + the keyword-research generator script

Report:
- **Public deck URL:** `https://decks.embertribe.com/{client-slug}/growth-roadmap.html`
- **xlsx path** (internal — not linked publicly): `embertribe-decks/decks/{client-slug}/keyword-research.xlsx`. The xlsx is technically reachable at `https://decks.embertribe.com/{client-slug}/keyword-research.xlsx` but isn't surfaced anywhere — share directly with the prospect via email or GHL.

In `cold` mode, post the deck URL back to the buyer's GHL contact record
(custom field: `growth_roadmap_url`) and attach the xlsx file
directly to the contact / send via email — don't post the xlsx URL publicly.

---

## Mode-specific notes

### Warm mode (sales team running before a call)
- Operator runs the skill directly via Claude
- Has call notes → can hand-tune the framing, add specific pain-point callouts
- Output is shared with the prospect on the call as a "we put this together based on our conversation"
- Time-to-deliver: ~30 min including SEMrush exports

### Cold mode (post-payment, self-serve)
- Triggered by GHL webhook after $97/$197 charge
- GHL form fields → `intake.json` → skill runs end-to-end
- If buyer didn't connect analytics, skill skips Path B and delivers the SEMrush+crawl version
- Output URL posted to GHL contact record + emailed to buyer
- Time-to-deliver: target < 10 min from payment to delivered URL (limited by SEMrush — once we move to DataForSEO this drops to ~3 min)

---

## Quality Checklist

Before pushing the deck:

- [ ] All stat values sourced from actual data
- [ ] Cover M12 target matches trajectory slide
- [ ] Branded % (if shown) verified against GSC UI when connected
- [ ] Competitor names are real companies from SEMrush
- [ ] Case study slide matches master numbers (8,500 → 500K, ~59x, $20M Series A, ~$2M impression-share value, 0 algorithm penalties across 4+ years)
- [ ] `images/casestudy-500k.jpg` exists in `embertribe-decks/decks/images/` and renders inline on slide 9
- [ ] No performance guarantees (per `sales/SALES-PARAMETERS.md` §5A)
- [ ] Projection disclaimer present on trajectory slide
- [ ] No em dashes in prose copy
- [ ] No broken HTML — single-file, self-contained for both deck and content plan
- [ ] Brand colors match the prospect's website
- [ ] All charts 0-based, no truncated y-axis
- [ ] Deck slide counter shows 1 / 13 (or 1 / 10 for minimum viable — drop slides 11 + 12)
- [ ] Content plan slides (10–12) render: stats + pillar/funnel charts (slide 10), inline month tabs work and switch between 40-row tables (slide 11), pillar cards + exclusions + timeline (slide 12)
- [ ] If GA4 + GSC connected: slide 4 shows GA4 trend + GSC click-mix donut + top non-branded queries (verified data path)
- [ ] If GA4 + GSC NOT connected: slide 4 shows SEMrush traffic + site health stat cards + connect-analytics annotation
- [ ] xlsx: 4 sheets present (Article Plan, Keyword Universe, Excluded, Read Me); KD bands and pillars color-coded
- [ ] Deck saved to `embertribe-decks/decks/{client-slug}/growth-roadmap.html`
- [ ] xlsx saved to `embertribe-decks/decks/{client-slug}/keyword-research.xlsx`
- [ ] Image references in deck use `../images/casestudy-500k.jpg` (one level up to shared folder)
- [ ] Both repos pushed before reporting delivery

---

## Reference: ClusterMagic case study numbers

These are the master figures. Use them on every deck unless updated:

**Flagship organic growth:**
- 8,500 monthly visits → 500,000+ monthly organic visits (~59x growth)
- Zero algorithm penalties across 4+ years
- Client raised $20M Series A — search traffic was a key board narrative
- ~$2M annual value from impression share alone (per their CMO)
- Site improves with each Google update
- Asset: `images/casestudy-500k.jpg` (live SEMrush screenshot — Organic Traffic + Keywords climbing together)

**AEO benchmark (NOT in this deck — kept for reference; the AEO case is for the AEO Benchmark deliverable, not the SEO Growth Roadmap):**
- 0% → 32.7% AI visibility in 30 days, 0% → 67% citation rate, category rank #30+ → #5

**Positioning:**
- ClusterMagic is "an AI-powered content engine that builds entity-rich content
  architectures for compounding authority"
- Differentiator: "4+ years of growth with zero penalties" — most AI-content
  strategies get hit by Google's algorithm updates; ClusterMagic content
  improves with each update
- 3-pillar framework: Entity-rich content / AI-powered execution / Compounds for years

---

## Future: DataForSEO (v1.5)

The `aeo-benchmark` skill already wraps DataForSEO at:
`.claude/skills/aeo-benchmark/scripts/dataforseo.py`

Currently uses AI-optimization endpoints only. To replace SEMrush in this skill,
extend with:
- `/keywords_data/google_ads/keywords_for_site/live` — pull keywords a domain ranks for
- `/dataforseo_labs/google/ranked_keywords/live` — current ranking positions
- `/dataforseo_labs/google/keyword_suggestions/live` — keyword expansion
- `/backlinks/summary/live` — backlink profile
- `/backlinks/competitors/live` — competitor backlink gap

Estimated cost per roadmap: ~$0.30–$0.50.

Wire this when buyer volume > 20/mo (point at which SEMrush manual lift outweighs DataForSEO API spend).

---

## Future: Windsor.ai integration (v1.5)

Account: Basic plan ($23/mo annual), purchased April 2026.

**Validation needed before integration:**
1. Confirm Basic tier includes API access (rate limits 600/min, 10K/day published, but tier-specific gating unclear)
2. Confirm "External authentication" link flow is multi-tenant — 50+ buyers each connecting their own GA4/GSC under our workspace
3. Confirm auth flow can be co-branded or domain-masked (buyer mid-checkout shouldn't see "Windsor.ai" prominently)

**Integration shape:**
1. GHL form → buyer clicks "Connect Google" → Windsor external-auth link
2. Buyer OAuths into their Google account → connection appears in our Windsor workspace
3. Webhook to our system on connect → triggers roadmap skill
4. `analytics.fetch_baseline(prospect)` calls Windsor API → returns parsed GA4 + GSC data
5. Skill assembles deck with enriched data

If Windsor's external-auth doesn't pan out, fallback to manual service-account-add
(Path A above) plus a 30-second loom showing GA4/GSC permission steps.

---

## Example Usage

### Warm mode

```
User: Run an SEO growth roadmap for Coastal Crate Pet Co. (coastalcrate.com).
      Mode: warm. Brand terms: "coastal crate", "coastalcrate".
      Competitors: The Farmer's Dog, Nom Nom, Open Farm.
      They mentioned struggling with content velocity and AEO is a new priority.

Skill:
  Phase 0: Intake captured to site/clients/coastal-crate-pet-co/growth-roadmap/intake.json
  Phase 1: Crawl + PageSpeed running. Prompting for SEMrush exports for the 4 domains.
  Phase 2: Analysis — opportunity sized at 28K monthly searches across 10 missing keywords;
           5 striking-distance keywords; LCP mobile = 4.1s flagged P1.
  Phase 3: Deck assembled, 12 slides. Brand colors pulled from coastalcrate.com (ocean blue + sand).
  Phase 4: Saved to embertribe-decks/decks/coastal-crate-pet-co-growth-roadmap.html.
           Live at https://decks.embertribe.com/coastal-crate-pet-co-growth-roadmap.html
```

### Cold mode

```
GHL webhook: POST /growth-roadmap with payload {
  email, prospect_name, url, services, competitors, ga4_connected, gsc_connected
}

Skill:
  → Saves intake.json from payload
  → Runs Phase 1 (crawl + PageSpeed always; GA4/GSC if connected)
  → If SEMrush data not yet uploaded, queues for sales-team manual export OR
    falls back to DataForSEO if v1.5 is live
  → Runs Phase 2-3
  → Phase 4: posts URL back to GHL contact custom field + emails buyer
```
