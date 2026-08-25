# EmberTribe Decks

This repo powers `decks.embertribe.com` — sales pitch decks and audit presentations for prospects.

## Git workflow — no worktree isolation

**Never** spawn agents, background tasks, scheduled tasks, or subagents with `isolation: "worktree"`. Always work directly in the main checkout on the `main` branch. Changes made inside `.claude/worktrees/` don't appear in the user's local folders and don't land on `main` unless explicitly merged — the user wants every change visible locally and every commit pushed to `origin` before a session ends.

## How It Works

1. Run the `pitch-deck` skill to generate a deck from prospect data
2. Save the HTML to `decks/`
3. Push to `main` — auto-deploys to `decks.embertribe.com`

## Folder Structure

```
embertribe-decks/
├── decks/                                        # Deploy root
│   ├── {prospect-slug}.html                      # legacy flat-file pitch decks
│   ├── images/                                   # shared images (case study screenshots, logos)
│   └── {client-slug}/                            # SEO growth roadmaps — one folder per client
│       ├── growth-roadmap.html           # 13-slide deck (deploys publicly)
│       └── keyword-research.xlsx                 # companion workbook (in repo, NOT linked publicly)
├── .claude/
│   └── skills/
│       ├── pitch-deck/                           # original pitch-deck skill
│       └── seo-growth-roadmap/           # tripwire SEO growth roadmap skill
└── CLAUDE.md                                     # This file
```

## Skills

| Skill | Purpose |
|-------|---------|
| `pitch-deck` | Generate branded audit/pitch decks from prospect data — output to `decks/{slug}.html` |
| `seo-growth-roadmap` | Generate SEO growth roadmap bundle (deck + xlsx) — output to `decks/{client-slug}/` |
| `embertribe-design` | EmberTribe brand design system — tokens, Quatro fonts, logos, components, and page templates (`templates/growth-roadmap-deck`, `templates/client-report`, `templates/content-plan`) |
| `partnership` | Generate a partner's active-account tier dashboard ("setup /partnership for {name}") — qualifying accounts against the $1,500 MRR floor, current tier, path to next tier. Output to `decks/{partner-slug}/dashboard.html`, public |

## Design system

The EmberTribe brand design system lives in `.claude/skills/embertribe-design/`. **Load the `embertribe-design` skill before generating or restyling any deck, report, or other EmberTribe-branded HTML** — colors, type, spacing, and logo rules come from its tokens and guidelines, not from memory. The `pitch-deck` and `seo-growth-roadmap` skills build on it: EmberTribe constants use the canonical tokens (`--ember-red: #FF333C`) and Quatro is served from the shared `decks/fonts/` folder.

## Rules

1. **Pitch decks → `decks/{slug}.html`** (flat); **SEO growth roadmaps → `decks/{client-slug}/growth-roadmap.html`** (nested); **partnership dashboards → `decks/{partner-slug}/dashboard.html`** (public, no password gate)
2. **xlsx companions live in the client folder** but aren't linked from anywhere public — sales team grabs them from the repo or shares directly with prospects
3. **Single-file HTML** — no external dependencies, everything inline (except shared images in `decks/images/` and shared Quatro fonts in `decks/fonts/`, referenced as `../images/...` / `../fonts/...` from inside a client folder, or `fonts/...` from a flat deck)
4. **`pitch-deck` skill** — if something needs changing, flag it for Josh
5. **`seo-growth-roadmap` skill** — canonical copy is mirrored in both `embertribe-decks` and `EmberTribe`; supporting scripts (site crawl, PageSpeed, GA4/GSC pulls, xlsx generators) live in `EmberTribe/scripts/`. Keep both copies in sync when editing.

## Internal docs (password-gated)

- `decks/internal/` — internal team docs (setup plans, training guides), NOT for prospects
- Everything under `decks.embertribe.com/internal/*` is protected by HTTP Basic Auth via `functions/internal/_middleware.js` (Cloudflare Pages Function at repo root)
- Password check only, any username works. Default password lives in the middleware; override with `INTERNAL_DOCS_PASSWORD` env var in the Pages project settings
- Organize by project: `decks/internal/{project-slug}/{doc}.html`
