# CRO Audit Skill

Generate a full conversion rate optimization audit as a branded slide deck for a client.
Single deliverable: a self-contained HTML presentation that educates on each audit pillar,
then surfaces the client's specific findings and prioritized action list.

**Visual template:** `embertribe-clients/dogizone/cro-audit.html`
Copy its CSS, slide framework, component patterns, and color token structure.
Replace all Dogizone-specific content with the new client's data and brand colors.

---

## When to Use

- User says "run a CRO audit for {client}"
- User says "build a CRO deck for {client}"
- User says "CRO audit for {url}"

---

## Output

```
embertribe-clients/{client-slug}/
└── cro-audit.html          ← single-file HTML presentation (public)

EmberTribe/site/clients/{slug}/cro-audit/
├── intake.json
├── pagespeed-results.json
└── ga4-data.json           (only if GA4 connected)
```

**Public URL:** `https://client.embertribe.com/{client-slug}/cro-audit.html`

Slug: lowercase, hyphens, no special chars (e.g. `dogizone`, `party-kids-america`).

---

## Phase 0: Intake

Collect at the start of every run. Save to `EmberTribe/site/clients/{slug}/cro-audit/intake.json`.

**Required:**
- Client name + website URL
- Platform (WordPress, Shopify, ERS, Webflow, Squarespace, WooCommerce, custom, etc.)
- GA4 access: Y or N
  - If Y: has the client added `embertribe-content-tools@embertribe-content-tools.iam.gserviceaccount.com` as Viewer in GA4?
  - If Y: what is the GA4 property ID? (numeric, found in GA4 Admin → Property Settings)
- Known competitors (2-4 names/URLs — local/regional competitors preferred over national chains)
  - If none provided, search for local competitors by city/region — not national franchise brands
- CTA email for the deck's final slide (default: sales@embertribe.com)

**GA4 pull (if connected) — run both scripts:**
```bash
# 6-month organic session trend
python3 scripts/ga4-baseline.py \
  --key-file embertribe-content-tools-e6776250739e.json \
  --property {ga4_property_id} \
  --months 6 \
  --output EmberTribe/site/clients/{slug}/cro-audit/ga4-baseline.json

# CRO funnel: conversion events, device split, form completion, new vs returning
python3 scripts/ga4-cro-funnel.py \
  --key-file embertribe-content-tools-e6776250739e.json \
  --property {ga4_property_id} \
  --funnel-pages "/" "{primary-service-page}" "{booking-or-checkout-page}" \
  --booking-page "{booking-or-checkout-page}" \
  --date-range "90daysAgo" \
  --output EmberTribe/site/clients/{slug}/cro-audit/ga4-cro-funnel.json
```

Key metrics to pull from ga4-cro-funnel.json for the deck:
- Sessions → booking page → confirmed conversion (step-by-step CVR)
- `reservation-submit-success` or equivalent completion event (the true conversion count)
- Device split on the booking/checkout page — mobile % is critical context for performance findings
- `form_start` vs `form_submit` vs completion event — reveals form abandonment
- Phone click events — quantifies offline demand
- New vs. returning breakdown

If GA4 is not connected, the deck falls back to PageSpeed + site crawl only.
Note the gap explicitly on slide 3 and what GA4 would unlock.

---

## Phase 1: Data Collection

### 1a. PageSpeed Insights (always run)

Run on 3 pages: homepage, primary product/service page, checkout or contact page.

```bash
python3 scripts/pagespeed-api.py \
  --url "{homepage}" \
  --url "{top-product-page}" \
  --url "{checkout-or-contact-page}" \
  --api-key "{PAGESPEED_API_KEY}" \
  --output EmberTribe/site/clients/{slug}/cro-audit/pagespeed-results.json
```

Capture for each page:
- Mobile + desktop performance score (0-100)
- Core Web Vitals: LCP, INP (or FID), CLS — pass/fail + actual values
- Top 3 diagnostic flags per page (largest contentful paint element, unused JS/CSS, render-blocking resources, image sizing)
- Time to Interactive (mobile)

Industry benchmarks to compare against (use in deck copy):
- Mobile score < 50: critical, 50-75: needs work, 75+: acceptable
- LCP > 4s mobile: critical, 2.5-4s: needs work, < 2.5s: good
- CLS > 0.25: critical, 0.1-0.25: needs work, < 0.1: good

### 1b. Site Browse (always run — use Claude in Chrome)

Browse the following and record findings per pillar (see Pillar Framework below):

1. **Homepage** — hero copy and CTA, value proposition clarity, trust signals above fold,
   navigation structure, social proof placement, mobile layout
2. **Category / product listing pages** — filtering/sorting, product card info, urgency signals,
   visual hierarchy
3. **Product / service detail pages** — CTA placement and copy, pricing display, reviews/ratings,
   product specs, related items, scarcity signals
4. **Cart / checkout flow** — steps to purchase, payment options displayed, shipping clarity,
   trust badges, field count, guest checkout availability, abandonment recovery signals
5. **About / FAQ / Contact pages** — policy clarity, return/shipping terms, contact accessibility
6. **Mobile** — resize to mobile viewport and note any layout breakdowns, tap target issues,
   sticky header behavior

Record all findings as issue objects with:
- `pillar`: one of the 6 pillars (see below)
- `page`: where it appears
- `observation`: what was found (factual, not opinionated)
- `recommendation`: specific fix
- `impact`: 1-5 (5 = highest conversion impact)
- `ease`: 1-5 (5 = easiest to implement on their platform)
- `score`: impact + ease (2-10)
- `priority`: Critical (9-10), High (7-8), Medium (5-6), Low (2-4)

### 1c. GA4 Analysis (if connected)

Pull and analyze:

**Purchase Funnel:**
- Sessions → Product/Service View → Add to Cart (or Lead Form) → Checkout Start → Purchase/Conversion
- Calculate drop-off % at each step
- Flag the step with the largest drop-off as the primary conversion bottleneck

**Traffic & Behavior:**
- 6-month organic session trend (growth, decline, or flat)
- Device split (desktop / mobile / tablet) with conversion rate per device
- Top 10 landing pages: sessions, bounce rate, avg engagement time, conversion rate
- Top acquisition channels + conversion rate per channel

**Revenue (if ecomm):**
- Top 10 products/services by revenue
- Average order value + trend (growing or shrinking)
- Revenue by device

**Branded vs. non-branded:** classify top queries if GSC also connected.

Save parsed output to `ga4-data.json`. Reference specific numbers in the deck — no ranges
or guesses when real data is available.

### 1d. Competitor Research

For each named competitor (or top 2-3 surfaced from local search):

**Always fetch the actual site — do not write competitor context from assumptions.**

For each competitor, record:
- **Hero headline**: exact text, not paraphrased
- **Pricing visibility**: does pricing appear on service/product pages? (Y/N + what they show)
- **Key offers**: any promotional or new-customer offers visible
- **Trust signals**: star rating displayed, review count, certifications, awards
- **Primary CTA**: what action they push visitors toward

Use this data to write specific comparisons in findings (e.g. "Dr. Boyd's shows $94.50/night upfront — DogiZone shows nothing"). Vague competitor mentions without specific observations add no value.

If competitors provided were national chains but the client is a local business, supplement with local competitors found via Google search for "{service} {city}" — local competitors are more relevant for positioning analysis.

### 1e. Brand Colors

Pull 2-3 colors from the client's homepage (header, hero, primary CTA button).
Map to CSS variables in the deck: `--client-dark`, `--client-mid`, `--client-accent`.

---

## Phase 2: Analysis — The 6 Pillars

Score every finding using the impact × ease matrix. Assign a priority tier:
- **Critical** (score 9-10): fix immediately, highest ROI
- **High** (score 7-8): significant lift, address after Critical
- **Medium** (score 5-6): meaningful improvement, next sprint
- **Low** (score 2-4): polish, address last

### Pillar 1 — Website Performance
*Technical foundation: speed, mobile, crawlability*

What to assess:
- Mobile + desktop PageSpeed scores vs. benchmarks
- Core Web Vitals pass/fail
- Image optimization (oversized, uncompressed)
- Render-blocking JS/CSS
- Unused apps or plugins adding load weight
- Mobile usability (tap targets, viewport fit, font sizes)
- Time to interactive on mobile

Key stat for education slide: "40% of visitors leave if a site takes more than 3 seconds to load"

### Pillar 2 — UX & Navigation
*Can users find what they need and move through the site without friction?*

What to assess:
- Navigation structure (depth, label clarity, dropdown vs. popup)
- Homepage exit rate (if GA4) — what % leave without going deeper
- Funnel drop-off by step (if GA4)
- Category/collection page organization — can users filter, sort, narrow?
- Internal linking — do product pages link to related items?
- Breadcrumbs — can users orient themselves?
- Search functionality (if applicable)
- Mobile navigation behavior

Key stat: "65%+ of revenue on most sites comes through 2+ touchpoints — smooth navigation is how you get them back"

### Pillar 3 — Visual Messaging
*Are copy and visuals converting browsers into buyers?*

What to assess:
- Homepage hero: does it have a clear value proposition in the first 3 seconds?
- CTA copy — specific and action-oriented ("Book Now", "Get a Quote") vs. generic ("Submit")
- Product/service copy — benefits-led or feature-led?
- Image quality — high resolution, showing product in use/context?
- Video presence on high-intent pages
- Above-fold content — is the most important information visible without scrolling?
- Headline hierarchy — does H1 match what the user searched for?

Key stat: "Customers are 85% more likely to purchase after watching a product video"

### Pillar 4 — Checkout Friction
*Are you losing buyers at the last step?*

What to assess:
- Steps to complete checkout — how many pages/fields?
- Guest checkout availability
- Payment options displayed (cards, Apple Pay, Google Pay, BNPL)
- Shipping cost disclosure — shown early or surprise at the end?
- Return/exchange policy — visible during checkout?
- Abandoned cart recovery — email/SMS in place?
- Upsell/cross-sell in cart or checkout
- Trust badges near the CTA (SSL, secure checkout, guarantees)
- Form field count — every unnecessary field loses conversions

Key stat: "70% of shopping carts are abandoned — most are recoverable with the right friction reduction"

### Pillar 5 — Urgency & Scarcity
*Are you giving buyers a reason to act now?*

What to assess:
- Low stock signals ("Only 3 left")
- Limited-time offers with deadlines
- Seasonal or promotional callouts in hero
- "Popular" or bestseller badges
- Booking/availability pressure (for service businesses)
- Countdown timers (if any)

Note: only flag genuine urgency — fabricated scarcity erodes trust. If the client doesn't have
real inventory or date constraints, focus on seasonal/promotional angles instead.

Key stat: "Scarcity and urgency signals can increase conversion rates 10-30% when authentic"

### Pillar 6 — De-risking & Social Proof
*Are you removing hesitation at the point of decision?*

What to assess:
- Review count + star ratings — visible on category and product pages?
- Review recency — are recent reviews surfaced?
- UGC photos in product listings
- Trust badges (industry certifications, awards, press mentions)
- Return/refund policy — clear and easy to find?
- Shipping policy — estimated delivery visible before checkout?
- "Contact us" accessibility — phone, chat, or email reachable from key pages?
- About Us — does it humanize the brand?
- Third-party credibility (BBB, Google rating, Trustpilot, etc.)

Key stat: "Adding reviews to product pages increases conversion by 15-20% on average"

---

## Phase 3: Deck Assembly

### Template

Copy structure, CSS, slide framework, and all component patterns from
`embertribe-clients/dogizone/cro-audit.html`.
Keep the full visual system. Replace all Dogizone content with the new client's data.

### Theming

```css
:root {
  --client-dark:   {client darkest brand color};
  --client-mid:    {client mid tone};
  --client-accent: {client CTA / accent color};
  --ember-red:     #ff333d;   /* always stays */
}
```

Dark slide gradient: `linear-gradient(135deg, var(--client-dark) 0%, var(--client-mid) 50%, [third] 100%)`

### Slide Structure (~16-18 slides)

| # | Slide | Type | Content |
|---|-------|------|---------|
| 1 | **Cover** | Dark | Client name, URL, audit date. 4 stat cards: overall CVR (if GA4), mobile score, issues found (count), top priority pillar |
| 2 | **What We Audited** | Light | Scope overview: 6 pillars listed with brief descriptions, data sources used (PageSpeed / GA4 / site browse / competitor research). Sets expectations. |
| 3 | **Your Funnel: Where the Drop-Off Is** | Light | GA4 purchase funnel with % drop at each step, device CVR comparison, top landing pages. **If GA4 not connected:** PageSpeed scores by page + site health snapshot + note on what GA4 would unlock. This is the "here's your current state" slide — specific numbers only, no estimates. |
| 4 | **Pillar 1: Website Performance** | Dark (pillar intro) | Education: why speed and mobile matter, 3-second stat, Core Web Vitals explained simply. Sets the "why" before the findings. |
| 5 | **Performance Findings** | Light | Client's actual PageSpeed scores (mobile + desktop, all 3 pages). Core Web Vitals pass/fail. Top 3 issues flagged. Priority-tagged action items for this pillar. |
| 6 | **Pillar 2: UX & Navigation** | Dark (pillar intro) | Education: how navigation friction kills conversions, homepage exit rate context, multi-touchpoint stat. |
| 7 | **UX & Navigation Findings** | Light | Funnel drop-off by step (if GA4), specific navigation issues found, priority-tagged action items. |
| 8 | **Pillar 3: Visual Messaging** | Dark (pillar intro) | Education: value proposition importance, video stat, above-fold content rules. |
| 9 | **Visual Messaging Findings** | Light | Hero assessment, CTA audit, copy quality notes, image/video gaps. Priority-tagged action items. |
| 10 | **Pillar 4: Checkout Friction** | Dark (pillar intro) | Education: cart abandonment rate, friction sources, recovery stats. |
| 11 | **Checkout Findings** | Light | Steps-to-purchase count, payment options, policy visibility, recovery gaps. Priority-tagged action items. |
| 12 | **Pillar 5: Urgency & Scarcity** | Dark (pillar intro) | Education: psychological drivers of urgency, authentic vs. fabricated scarcity. |
| 13 | **Urgency & Scarcity Findings** | Light | What signals are present vs. missing. Competitor comparison if relevant. Priority-tagged action items. |
| 14 | **Pillar 6: De-risking & Social Proof** | Dark (pillar intro) | Education: review conversion lift stat, trust barrier psychology, return policy impact. |
| 15 | **Social Proof Findings** | Light | Review visibility, trust badge audit, policy accessibility, brand humanization. Priority-tagged action items. |
| 16 | **Priority Roadmap** | Light | All issues across all pillars in a single ranked list. Critical → High → Medium → Low. Each item: pillar tag, issue name, effort badge. This is the "master checklist" view. |
| 17 | **Implementation Phases** | Light | Phase 1 (Critical, no developer needed), Phase 2 (High, dev or plugin work), Phase 3 (Medium+, ongoing optimization). Lists which specific items go in each phase. No week estimates — phasing only. |
| 18 | **Next Steps** | Dark | CTA. "Here's how we help you execute this." EmberTribe contact + call to action. |

**Minimum viable deck** (sparse data): drop slide 3 (funnel) if no GA4 and site is pre-revenue.
All other slides required.

### Priority Tag Visual System

Every finding on a findings slide gets a colored priority badge:

```html
<!-- Critical -->
<span style="background:#fef2f2;color:#dc2626;border:1px solid #fecaca;
     border-radius:4px;padding:2px 8px;font-size:11px;font-weight:700;">Critical</span>

<!-- High -->
<span style="background:#fff7ed;color:#ea580c;border:1px solid #fed7aa;
     border-radius:4px;padding:2px 8px;font-size:11px;font-weight:700;">High</span>

<!-- Medium -->
<span style="background:#fffbeb;color:#d97706;border:1px solid #fde68a;
     border-radius:4px;padding:2px 8px;font-size:11px;font-weight:700;">Medium</span>

<!-- Low -->
<span style="background:#f9fafb;color:#6b7280;border:1px solid #e5e7eb;
     border-radius:4px;padding:2px 8px;font-size:11px;font-weight:700;">Low</span>
```

### Platform-Specific Implementation Notes

On findings slides, tailor "how to fix" steps to the client's platform:

| Platform | Key paths to reference |
|----------|----------------------|
| WordPress | Plugins (WP Rocket, Smush, Yoast), theme editor, WooCommerce settings, Elementor/Gutenberg blocks |
| Shopify | Theme editor, Shopify App Store, liquid templates, checkout settings, Klaviyo |
| ERS | /cp/items/, /cp/source_code/, /cp/responsive_editor/, /cp/website_pages/, ERSMail |
| Webflow | Designer, CMS collections, Interactions, Embed code blocks |
| Squarespace | Pages panel, Style editor, Commerce settings, Code injection |

### Dark Slide Text Contrast

Text on dark/blue gradient slides must meet minimum opacity thresholds for readability:
- Stat labels, subtitles, secondary copy: minimum `rgba(255,255,255,0.85)`
- Body/explanatory paragraphs: minimum `rgba(255,255,255,0.78)`
- Footer / meta text: minimum `rgba(255,255,255,0.70)`
- Never go below `0.62` for any readable text element — it fails on blue backgrounds

### Education Slide Copy Style

Pillar intro slides (dark) follow this pattern:
1. Pillar name as large headline
2. One-sentence plain-English explanation of what this pillar covers
3. One compelling industry benchmark stat (use the stats from Phase 2 pillar descriptions)
4. 2-3 bullet "signals we look for" — primes the client to understand what the findings mean

Keep education slides short — they are context-setters, not lectures. The findings slide is where the value is.

### Stat Cards (Cover Slide)

Pull from real data only:
- **Overall CVR**: from GA4 if connected (e.g. "2.1% conversion rate")
- **Mobile Score**: from PageSpeed (e.g. "34 / 100")
- **Issues Found**: total count of all findings across pillars
- **Top Priority Pillar**: the pillar with the most Critical + High items

If GA4 not connected, replace CVR card with "Platform: {platform name}".

---

## Phase 3b: QA Verification

After the deck is assembled, spawn a background QA agent to verify the accuracy of findings against the live site before delivery. Do not skip this step.

```
Spawn a general-purpose agent with this prompt:

"QA the CRO audit deck for [client name] ([url]).
Read the deck at [path to cro-audit.html].
Browse the actual website and verify each finding is accurate.
For each claim, report: VERIFIED / WRONG / PARTIAL / CANT VERIFY.
Flag any factual errors — wrong step counts, incorrect headlines, misquoted copy,
offers that don't exist, or features described incorrectly.
Do not edit any files — research only."
```

**Common errors to specifically check:**
- Form step count — walk through the actual checkout/booking form and count steps. Never estimate.
- Hero headline — quote the exact live text, not brand taglines from image filenames or metadata
- Pricing claims — verify which specific pages show or hide pricing (don't generalize across all pages)
- Review placement — check each service page individually; "no reviews on service pages" is often wrong
- Offer count and descriptions — verify each offer exists and note where it actually appears
- Competitor comparisons — confirm any specific claims made about competitor sites

Apply all corrections from the QA report before pushing.

---

## Phase 4: Save and Deliver

1. Save to `embertribe-clients/{client-slug}/cro-audit.html`
2. Save working data to `EmberTribe/site/clients/{slug}/cro-audit/`
3. Commit + push `embertribe-clients` repo
4. Report:
   - **Public URL:** `https://client.embertribe.com/{client-slug}/cro-audit.html`
   - Issue count by tier (e.g. "4 Critical, 7 High, 9 Medium, 5 Low — 25 total")
   - Top 3 findings summary (the headline items to lead with on the client call)

---

## Quality Checklist

Before pushing:

- [ ] All stat values sourced from actual data — no estimated numbers on slides
- [ ] PageSpeed scores shown for all 3 pages (mobile + desktop)
- [ ] GA4 funnel numbers match what was pulled (if connected); if not connected, slide 3 uses fallback layout and notes the gap
- [ ] Every finding has a priority tag (Critical / High / Medium / Low)
- [ ] Platform-specific implementation steps (not generic advice)
- [ ] Priority roadmap (slide 16) lists ALL findings from all 6 pillars
- [ ] Phase breakdown (slide 17) assigns every finding to a phase — no week estimates, phases only
- [ ] Education slides are short — stat + context + "what we look for" only
- [ ] Brand colors match client website — verified by viewing the site
- [ ] Dark slide text opacity minimum 0.78 for body copy, 0.85 for labels/subtitles
- [ ] No em dashes in prose copy
- [ ] No broken HTML — single file, fully self-contained
- [ ] Slide counter shows correct total (16-18)
- [ ] QA agent run and all corrections applied
- [ ] Hero headline quoted from live site copy — not from image filenames, alt text, or brand docs
- [ ] Form step count verified by walking through the actual form
- [ ] Competitor comparisons backed by data from actually fetching their sites
- [ ] CTA email set to sales@embertribe.com (or client-specified address)
- [ ] Deck saved to `embertribe-clients/{client-slug}/cro-audit.html`
- [ ] Both repos pushed before reporting delivery

---

## Example Usage

```
User: Run a CRO audit for Dogizone (dogizone.com). Platform: WordPress.
      GA4: yes, connected. Competitors: Rover, Wag, local doggy daycare.

Skill:
  Phase 0: Intake saved to EmberTribe/site/clients/dogizone/cro-audit/intake.json
  Phase 1: PageSpeed running on homepage + services page + contact page.
           GA4 pull: 6-month funnel, device split, top landing pages.
           Site browse: noting hero, CTAs, nav, checkout/booking flow, trust signals.
  Phase 2: 22 findings across 6 pillars. 3 Critical, 6 High, 9 Medium, 4 Low.
           Top pillar: De-risking & Social Proof (no reviews surfaced on service pages).
  Phase 3: 17-slide deck assembled. Brand colors: deep teal + warm orange.
  Phase 4: Saved to embertribe-clients/dogizone/cro-audit.html
           Live at https://client.embertribe.com/dogizone/cro-audit.html
```
