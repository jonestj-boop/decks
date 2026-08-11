---
name: embertribe-design
description: Use this skill to generate well-branded interfaces and assets for EmberTribe, either for production or throwaway prototypes/mocks/etc. Contains essential design guidelines, colors, type, fonts, assets, and UI kit components for prototyping.
user-invocable: true
---

Read the README.md file within this skill, and explore the other available files.
If creating visual artifacts (slides, mocks, throwaway prototypes, etc), copy assets out and create static HTML files for the user to view. If working on production code, you can copy assets and read the rules here to become an expert in designing with this brand.
If the user invokes this skill without any other guidance, ask them what they want to build or design, ask some questions, and act as an expert designer who outputs HTML artifacts _or_ production code, depending on the need.

## Quick reference
- **Brand:** EmberTribe — growth-marketing agency ("A NAPKIN Company"). Voice: bold, punchy. Hero line: "Breakthrough needs method and madness."
- **Type:** Quatro (Bold/SemiBold/Regular) in `assets/fonts/`. Headers = Bold sentence case; nav/subheads = ALL CAPS; body = Regular. Bullets use an em dash (—).
- **Color:** Black + Candy Apple Red (#FF333C) on white; Honey Yellow (#FFB000) accent. Full secondary/tertiary palettes in `tokens/colors.css`.
- **Tokens:** link `styles.css` (root) — it `@import`s all token files.
- **Components:** `components/` (Button, Tag, Badge, Card, SectionLabel, Logo, Input, Textarea, Select, Checkbox).
- **Logos:** `assets/logos/` — never redraw the mark.
- **Icons:** Lucide (CDN) — no proprietary icon set exists.
