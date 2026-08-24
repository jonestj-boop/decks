# EmberTribe Design System

Brand + UI design system for **EmberTribe**, a growth-marketing agency ("A NAPKIN Company"). Built from the official brand guidelines package.

> **Breakthrough needs method and madness.** — the brand's headline voice

## Company / product context

EmberTribe is a performance-marketing and growth agency. Their public surface is a marketing website and client-facing decks/collateral; there is no product app in the provided materials. This design system therefore centers on **brand foundations** (logo, color, Quatro type), a **reusable web-UI component set**, a **marketing-site UI kit**, and a **client-deck slide kit** — all in the EmberTribe visual voice.

Co-founder listed in guidelines: Josh Sturgeon (josh@embertribe.com). Domain: embertribe.com.

### Sources provided
- `EMBERTRIBE_BRAND_GUIDELINES_V2.pdf` — logo system, color palettes (primary/secondary/tertiary), typography, tone examples, application mockups. (April 2021, v2.0)
- Logo lockups: primary 2-colour (`EmberTribe_PRIMARY_2_COLOUR.{svg,png,ai,eps,pdf,jpg}`) + three "A NAPKIN Company" special-use lockups (horizontal, small stacked, vertical).
- Fonts: `Quatro_Reg.otf`, `Quatro_SemiBold.otf`, `Quatro_Bold.otf` (the real identity typeface — no substitution needed).

No codebase, Figma file, or live product screens were provided. UI-kit screens are **brand-consistent constructions** grounded in the guidelines' tone and application mockups, not recreations of an existing production UI.

---

## CONTENT FUNDAMENTALS

**Voice:** confident, punchy, a little irreverent. The hero example — "Breakthrough needs method and madness." — is short, declarative, and rhythmic. Copy leads with a bold claim, then backs it with specifics.

- **Casing:** Headers are **Sentence case**. Navigation and subheads are **ALL CAPS**. Body is Sentence case. (Per the guidelines' typography example.)
- **Person:** Speaks in a confident brand/first-person-plural voice ("Our mission"), addressing the client as "you." Direct and outcome-oriented.
- **Bullets:** Use an **em dash (—)** as the bullet marker, not discs or hyphens. This is an explicit brand rule.
- **Emoji:** None. The brand is bold-typographic, not emoji-driven.
- **Length:** Headlines are terse (3–7 words). Supporting copy is plain and concrete — growth, results, method.
- **Tone words:** method, madness, breakthrough, growth, results, tribe.

**Examples of section labels seen in guidelines:** "RECENT NEWS", "OUR MISSION", "ABOUT", "CONNECT", "CONTACT US" (all caps navigation/subhead style).

---

## VISUAL FOUNDATIONS

**Color.** The identity is built on high-contrast **black + Candy Apple Red (#FF333C)** on white, with **Honey Yellow (#FFB000)** as the warm accent. A deep secondary set (turquoise, oxford/ultramarine blue, coral, lime) and a playful tertiary set (azure, orchid, shamrock, amethyst, bubblegum) give range for illustration, data, and social use. Rule from guidelines: **maximize contrast** between logo/type and background. Red is used decisively — as the logo field, key CTAs, and accent — never as a wash.

**Type.** Quatro throughout — a friendly, rounded geometric sans. Bold for headers/nav, SemiBold for subheads, Regular for body. Display headers run large and tight (`--ls-tight`); caps roles get letter-spacing (`--ls-caps`). Calibri is the guidelines' *internal-only* fallback and is never mixed with Quatro.

**Backgrounds.** Predominantly clean white or rich black — high contrast, generous whitespace. No gradients as a default motif, no busy textures. Red appears as solid blocks/panels rather than gradients. When imagery is used it should be warm and energetic.

**Corners / cards.** The logo symbol is a soft-cornered square; UI mirrors that with moderate radii (`--radius-md` 12px for cards, `--radius-sm` 8px for inputs, pill radius for tags/some CTAs). Cards use subtle neutral shadows (`--shadow-sm/md`), a 1px `--border-subtle` when flat, and never colored left-border accents.

**Shadows.** Neutral and understated — soft black drop shadows only. A single optional branded shadow (`--shadow-brand`) exists for a red CTA lift; use sparingly.

**Borders.** Hairline (1px) neutral borders for structure; 2px for emphasis/focus. Focus ring is brand red.

**Motion.** Restrained and crisp. Standard `200ms` ease for hovers, `340ms` ease-out for larger transitions. No bounces or infinite decorative loops. Respect `prefers-reduced-motion`.

**Hover states.** Primary (red) buttons darken to `--et-red-hover` (#e62831). Ghost/secondary elements shift background to `--surface-subtle`. Links darken. Slight `translateY(-1px)` lift is acceptable on cards/CTAs.

**Press states.** Return to baseline / very slight scale-down (0.98); no color inversion.

**Transparency / blur.** Minimal. Optional dark scrims over imagery for text legibility; no glassmorphism as a system motif.

**Layout.** Max content width ~1200px, narrow reading column ~760px. 4px spacing grid. Left-aligned, editorial rhythm with big type and clear hierarchy.

---

## ICONOGRAPHY

The brand guidelines do **not** define a proprietary icon set. The identity is typographic + logo-driven. For UI needs this system standardizes on **Lucide** (CDN) — a clean, geometric, consistent-stroke open-source set whose rounded-but-precise character pairs well with Quatro. Stroke weight ~2px, `currentColor`, sized 16–24px in UI.

- No built-in icon font, no emoji, no unicode-glyph icons in the brand materials.
- The **primary logo is now the horizontal "EmberTribe, A NAPKIN Company" lockup** (Napkin acquired EmberTribe). The `Logo` component's `primary` variant points at it; `napkin-stacked` / `napkin-vertical` are special-use, and the legacy pre-acquisition lockup is available as `wordmark`.
- The **E-in-square symbol** from the logo is the one true brand mark — use the provided logo assets in `assets/logos/`, never redraw it.
- **No reversed (white-wordmark) lockup** was provided; the wordmark is black. On dark grounds, use a monochrome-white treatment of the logo or keep the mark on a light panel. Ask the client for a reversed lockup if needed.
- **No slide/deck template** was provided in the brand package, so this system ships no sample slides. Decks are a stated brand use case ("designed keynotes") — request the keynote template to add a Slides kit.
- **Substitution flag:** Lucide is an added convention (there was no source icon set). Swap for the client's preferred library if one exists.

---

## Index / manifest

**Root**
- `styles.css` — global entry (import this). `@import`s all token files.
- `tokens/` — `colors.css`, `typography.css`, `spacing.css`, `fonts.css`.
- `assets/logos/` — EmberTribe logo lockups (NAPKIN primary + special-use + legacy wordmark). `assets/fonts/` — Quatro OTFs.
- `SKILL.md` — Agent-Skill wrapper.

**Components** (`components/`) — React primitives, each with `.jsx` + `.d.ts` + `.prompt.md` + a card:
- `Button`, `Tag`, `Badge`, `Card`, `Input`, `Textarea`, `Select`, `Checkbox`, `SectionLabel`, `Logo`.

**UI kit** (`ui_kits/marketing-site/`) — the full EmberTribe.com, seven linked pages: `index.html` (home), `services.html`, `method.html`, `about.html`, `case-studies.html`, `blog.html`, `contact.html`. Shared `Nav`/`Footer`/`shared.jsx` (CtaBand, PageHeader, Partners). Imagery uses `<image-slot>` drop-targets throughout — drag real CMS photos in. Content reflects the current site (Traction/Profit/Scale method; Paid Media, SEO, ClusterMagic, Email, Web Dev, Recapture; 12+ yrs / $120M+ / 550+ brands; Greensboro HQ).

**Foundation cards** — specimen HTML across groups: Brand, Colors, Type, Spacing.

## Intentional additions
- **Lucide icon set** (CDN) — no source icon library existed; added for functional UI needs.
- **Neutral ink ramp** (`--et-ink-*`) — derived from Dark Charcoal / Cloudy Gray so UI has enough greys for text, borders, surfaces.
- Component families (Button, Card, Input, etc.) are a standard from-scratch web set, since no source component inventory was provided.

---

## Keeping the three copies in sync

This skill lives in **three repos** (EmberTribe, embertribe-decks, embertribe-clients)
because users have different repo access, and everyone needs the design system.
**The EmberTribe copy is canonical** — edit there, then mirror outward:

```bash
rsync -a --delete "EmberTribe/.claude/skills/embertribe-design/" "embertribe-decks/.claude/skills/embertribe-design/"
rsync -a --delete "EmberTribe/.claude/skills/embertribe-design/" "embertribe-clients/.claude/skills/embertribe-design/"
```

(paths relative to the folder that holds all three repos; commit and push each repo).
If you must hotfix a non-canonical copy, port the change back to EmberTribe in the
same sitting — that is how the Aug 2026 print-stylesheet fix briefly stranded in
embertribe-decks.
