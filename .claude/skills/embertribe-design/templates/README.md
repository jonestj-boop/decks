# EmberTribe HTML deliverable templates

Three reference templates for the HTML artifacts EmberTribe ships to clients. Each is a
**self-contained HTML file + a `fonts/` folder** (Quatro). Copy the whole folder into the
client repo, set one accent color, fill in content. This keeps every deliverable on-brand
instead of drifting to default styles.

## The three templates

| Folder | File | For |
|---|---|---|
| `growth-roadmap-deck/` | `growth-roadmap-deck.html` | Full-screen keynote deck (arrow keys / click / dots). Growth roadmaps. |
| `client-report/` | `client-report.html` | Scrolling one-pager with sticky sidebar nav. CRO audits, ecommerce reports, implementation workbooks. |
| `content-plan/` | `content-plan.html` | Keyword-research-driven SEO content plan: summary stats, pillar/funnel charts, month tabs, per-month article table (keyword · volume · difficulty). |

## Shared conventions (the house style)

- **Type:** Quatro only. Headers *Sentence case*; labels & subheads *ALL CAPS*; bullets use an em-dash (—).
- **Palette:** EmberTribe red `#FF333C`, black `#000`, honey `#FFB000`, white. **Do not change these.**
- **Client accent:** each file has one `--client-accent` token (+ `--client-accent-soft`). Set it to the
  client's brand color. It's used only for chart series, secondary highlights and active states — the red/black
  frame stays EmberTribe.
- **Client logo:** each template has an optional `<img class="client-logo" src="">` on the cover/masthead.
  Point it at a client logo (white/transparent works best on the black covers) or delete the tag — it hides
  itself if empty.
- **Placeholder content:** every archetype/module appears once, filled with realistic dummy copy. Duplicate and
  replace — don't invent new component styles.

## Growth-roadmap deck — required slides

The **case-study slide is always included.** It's EmberTribe's fixed flagship-client
proof ("8,500 → 500,000 monthly organic visits" via the ClusterMagic engine). Keep the
story and the ClusterMagic reference verbatim; only swap the example-client name. Drop the
SEMrush chart in as `casestudy-500k.jpg` beside the HTML — the slide falls back to a labelled
placeholder until you do.

## For Claude Code

1. `cp -r templates/<folder> <client-repo>/<slug>/`
2. Open the HTML, set `--client-accent` in `:root`.
3. Add the client logo (optional).
4. Duplicate slides / sections / rows and fill with real content — but keep the flagship
   case-study slide in every growth-roadmap deck.
5. Keep the type + color rules above. That's what stops these from looking generic.

All three print cleanly (Cmd/Ctrl-P → Save as PDF) and work fully offline.
