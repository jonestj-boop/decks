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
│   └── {client-slug}/                            # SEO opportunity assessments — one folder per client
│       ├── opportunity-assessment.html           # 13-slide deck (deploys publicly)
│       └── keyword-research.xlsx                 # companion workbook (in repo, NOT linked publicly)
├── .claude/
│   └── skills/
│       ├── pitch-deck/                           # original pitch-deck skill
│       └── seo-opportunity-assessment/           # tripwire opportunity assessment skill
└── CLAUDE.md                                     # This file
```

## Skills

| Skill | Purpose |
|-------|---------|
| `pitch-deck` | Generate branded audit/pitch decks from prospect data — output to `decks/{slug}.html` |
| `seo-opportunity-assessment` | Generate SEO opportunity assessment bundle (deck + xlsx) — output to `decks/{client-slug}/` |

## Rules

1. **Pitch decks → `decks/{slug}.html`** (flat); **SEO opportunity assessments → `decks/{client-slug}/opportunity-assessment.html`** (nested)
2. **xlsx companions live in the client folder** but aren't linked from anywhere public — sales team grabs them from the repo or shares directly with prospects
3. **Single-file HTML** — no external dependencies, everything inline (except shared images in `decks/images/`, referenced as `../images/...` from inside a client folder)
4. **`pitch-deck` skill** — if something needs changing, flag it for Josh
5. **`seo-opportunity-assessment` skill** — canonical copy is mirrored in both `embertribe-decks` and `EmberTribe`; supporting scripts (site crawl, PageSpeed, GA4/GSC pulls, xlsx generators) live in `EmberTribe/scripts/`. Keep both copies in sync when editing.
