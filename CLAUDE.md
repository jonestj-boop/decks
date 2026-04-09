# EmberTribe Decks

This repo powers `decks.embertribe.com` — sales pitch decks and audit presentations for prospects.

## How It Works

1. Run the `pitch-deck` skill to generate a deck from prospect data
2. Save the HTML to `decks/`
3. Push to `main` — auto-deploys to `decks.embertribe.com`

## Folder Structure

```
embertribe-decks/
├── decks/                    # Published HTML decks (auto-deployed)
│   └── {prospect-slug}.html
├── images/                   # Shared images (logos, screenshots)
├── .claude/
│   └── skills/
│       └── pitch-deck/       # Deck generation skill
│           ├── SKILL.md
│           └── template.html
└── CLAUDE.md                 # This file
```

## Skills

| Skill | Purpose |
|-------|---------|
| `pitch-deck` | Generate branded audit/pitch decks from prospect data |

## Rules

1. **All decks go in `decks/`** — this is the deploy root
2. **Single-file HTML** — no external dependencies, everything inline
3. **Don't modify the skill** — if something needs changing, flag it for Josh
4. **Images in `images/`** — reference with relative paths from `decks/`
