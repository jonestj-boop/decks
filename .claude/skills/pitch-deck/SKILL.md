# Pitch Deck Skill

Generate branded audit and pitch decks for EmberTribe prospects. Produces a single-file HTML presentation with slide navigation, data visualizations, and client-specific branding.

---

## When to Use

- User says "build a deck for {prospect}"
- User says "create a pitch for {prospect}"
- User says "audit deck for {prospect}"
- User provides call transcripts, SEMrush data, or GSC exports and wants a presentation

---

## Inputs

The skill works with whatever data is available. More data = richer deck.

### Required
- **Prospect name** and **website URL**
- **At least one data source** (see below)

### Data Sources (any combination)

| Source | What It Provides |
|--------|-----------------|
| **Call transcript** | Pain points, goals, current strategy, budget signals |
| **SEMrush exports** | Organic traffic, keyword rankings, competitors, backlinks, ad spend |
| **Google Search Console** | Impressions, clicks, CTR, top queries, top pages |
| **Manual research** | Site audit findings, content gaps, technical issues |

### How to Provide Data

The user can:
1. **Paste directly** into the conversation (transcripts, data summaries)
2. **Provide file paths** to CSVs, JSONs, or text files
3. **Describe findings** verbally for the skill to structure

---

## Process

### Phase 1: Data Ingestion & Analysis

1. **Collect all inputs** — read files, parse transcripts, review data
2. **Extract key findings:**
   - Current traffic and trend (growing, declining, flat)
   - Top keywords and ranking positions
   - Competitor landscape (who's outranking them, by how much)
   - Content gaps and opportunities
   - Technical issues (site speed, mobile, indexation)
   - Paid media performance if applicable
   - Pain points from call transcript
3. **Identify the narrative** — what's the core story?
   - "You're leaving money on the table because..."
   - "Your competitors are outspending you in..."
   - "Your content strategy has gaps in..."

### Phase 2: Deck Assembly

Build the deck using the template in `.claude/skills/pitch-deck/template.html`.

**Slide structure (adapt based on available data — not all slides are required):**

| # | Slide | Background | Purpose |
|---|-------|-----------|---------|
| 1 | Title | Dark | Prospect name, headline finding, 3-4 stat cards |
| 2 | Current State | Light | Where they are today — traffic, rankings, key metrics |
| 3 | Traffic Trends | Light | 12-month bar chart showing trajectory |
| 4 | Content Audit | Light | Sample pages audited with grades, issues found |
| 5 | Competitor Landscape | Light | Comparison table — prospect vs 2-3 competitors |
| 6 | Keyword Opportunities | Light | Gap analysis — what competitors rank for that they don't |
| 7 | Strategy Overview | Light | 3-column cards — the channels/approaches we'd use |
| 8 | Roadmap | Light | Timeline — Month 1-3 phases with deliverables |
| 9 | Investment | Light | Pricing table with monthly breakdown |
| 10 | Projected Outcomes | Light | Expected results at 3/6/12 months |
| 11 | Next Steps | Dark | CTA — book a call, start onboarding |

**Slide selection rules:**
- Skip slides where we don't have data (e.g., no SEMrush = skip competitor landscape)
- Combine thin slides (e.g., if content audit is light, merge into Current State)
- Minimum 7 slides, maximum 14
- Always include: Title, Current State, Strategy, Investment, Next Steps

### Phase 3: Branding & Theming

1. **Visit the prospect's website** to identify their brand colors
2. **Set CSS variables:**
   - `--primary-dark`: Prospect's darkest brand color (for dark slides)
   - `--primary-mid`: Mid-tone for gradients
   - `--accent`: Prospect's accent/CTA color
   - EmberTribe red (`--ember-red: #ff333d`) stays constant
3. **Dark slide gradient:** `linear-gradient(135deg, var(--primary-dark) 0%, var(--primary-mid) 50%, [third-tone] 100%)`

### Phase 4: Save & Preview

1. **Save to:** `decks/{prospect-slug}.html`
   - Slug format: lowercase, hyphens, no special chars (e.g., `acme-corp.html`)
2. **Report the URL:** `https://decks.embertribe.com/{prospect-slug}.html`
3. **Offer to preview locally** if a dev server is available

---

## Template Reference

The template file (`template.html`) contains the full CSS component library and JS navigation. When building a deck:

1. **Start from the template** — copy its structure
2. **Customize the `:root` variables** for the prospect's brand
3. **Assemble slides** using the component patterns below
4. **Update the slide count** in the nav counter

### Component Library (available in template)

**Layout:**
- `.slide` / `.slide.dark` — light or dark background slides
- `.two-col` — 2-column grid (collapses to 1 on mobile)
- `.three-col` — 3-column grid (collapses to 1 on mobile)

**Data Display:**
- `.stats-row` > `.stat-card` — headline metrics (value + label)
- `.bar-chart` > `.bar-row` — horizontal bar charts
- `table` — data tables with header styling
- `.annotation` / `.annotation.danger` / `.annotation.success` / `.annotation.info` — callout boxes

**Content:**
- `.channel-card` — strategy/service cards with icon + bullets
- `.timeline` > `.timeline-phase` — horizontal roadmap
- `.pill` / `.pill.seo` / `.pill.paid` / `.pill.content` — category badges
- `.sample-card` — page audit cards with URL + grade

**Navigation (built into template):**
- Arrow keys + space for slide advance
- Bottom-right nav buttons
- Top progress bar

---

## Quality Checklist

Before saving the deck, verify:

- [ ] Title slide has prospect name, not a generic heading
- [ ] All stat values are sourced from actual data (no made-up numbers)
- [ ] Bar chart percentages/widths make visual sense
- [ ] Competitor names are real companies, not placeholders
- [ ] Investment slide has realistic EmberTribe pricing
- [ ] CTA slide has a clear next step
- [ ] Colors match the prospect's brand (check their website)
- [ ] No broken HTML — single-file, self-contained
- [ ] File saved to `decks/{prospect-slug}.html`
- [ ] Total slide count matches counter in nav

---

## Pricing Defaults

Unless the user specifies otherwise, use these EmberTribe service tiers:

| Service | Monthly Range |
|---------|-------------|
| SEO Content | $2,000 - $4,000 |
| Paid Media Management | $1,500 - $3,000 |
| Technical SEO | $1,000 - $2,000 |
| Content Strategy | $1,500 - $2,500 |
| Full-Service Package | $5,000 - $10,000 |

Always present as ranges or "starting at" — never as fixed quotes unless the user provides exact numbers.

---

## Example Usage

```
User: Build a pitch deck for Acme Corp (acmecorp.com). Here's the call transcript: [paste]
       And here's the SEMrush organic overview CSV: [file path]

Skill: 
1. Reads transcript → extracts pain points, goals, budget
2. Parses SEMrush CSV → traffic trends, top keywords, competitors
3. Visits acmecorp.com → pulls brand colors
4. Assembles 10-slide deck with findings
5. Saves to decks/acme-corp.html
6. Reports: "Deck ready at decks/acme-corp.html — will be live at https://decks.embertribe.com/acme-corp.html after push"
```
