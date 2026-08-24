---
name: qa-review
description: Neutral pre-delivery QA review of any client-facing deliverable (deck, content plan, article, workbook copy, email, report) for strategy fit, factual accuracy, brand voice, humanization, grammar, and format compliance. Use when user says "QA this", "run QA on {deliverable}", "review this before it ships", or when another skill's checklist requires a qa-review pass.
---

# QA Review — the neutral reviewer

A fresh-context reviewer that was not part of building the deliverable and whose only
job is to find the reasons it should not ship. Same-context self-review misses what it
just wrote; a defect caught here costs minutes, the same defect caught by the client
costs the relationship. This skill is deliverable-agnostic: decks, content plans,
articles, workbook copy, emails, reports.

**The reviewer reports; it never edits.** Fixes belong to whoever built the deliverable,
who then re-runs review until the verdict is SHIP.

**Copies:** canonical in the EmberTribe repo; mirrored to embertribe-decks (with
`references/humanize.md`, the `humanize` skill, and `scripts/validate-deck.py` +
`scripts/validate-prose-tells.py`). Edit the EmberTribe copy and re-mirror — same rule
as the embertribe-design skill. Ground-truth client files exist only in EmberTribe;
when reviewing from another repo, skip what you can't reach and say so in the report.

---

## How to dispatch (for the orchestrating session)

Run the review as a **fresh sub-agent** — never review in the context that produced the
work. Model: **at or above the tier that produced the deliverable** (house decision
2026-08-13: QA runs a tier above a smaller-model writer; work produced by the main
session gets reviewed at the session tier — the freshness is the point). Web access on.

Dispatch prompt template (fill the manifest, keep the rest verbatim):

```
You are a neutral QA reviewer. You had no part in producing this work; your job is to
find the reasons it should NOT ship. Read
.claude/skills/qa-review/SKILL.md and follow it exactly, including the humanization
checklist it references.

Manifest:
- Client: {slug}
- Deliverable type: {deck | content-plan | article | workbook-copy | email | report}
- Files under review: {paths}
- Ground truth: {paths — see the bundle table in the skill}
- Standard / checklist for this deliverable type: {path, e.g. the producing skill's checklist}
- Orchestrator focus notes: {anything the builder is unsure about}

Write the full report to {client working dir}/qa-report.md and return only the verdict
line and the P1/P2/P3 counts.
```

## Ground-truth bundle (assemble per client before dispatch)

| Always | When present |
|---|---|
| `clients/{slug}/brand-facts.md` — every client claim traces here or to the live site | `clients/{slug}/icp-profile.md` — audience/intent/positioning authority |
| The deliverable's own standard/checklist (from the producing skill) | `clients/{slug}/config.yaml` + `taxonomy.yaml` — brand voice, structure |
| `clients/{slug}/rejected-topics.yaml` + banned-phrase lists | `clients/{slug}/FEEDBACK.md` — standing client rules |
| Source data files for any number displayed (analysis.json, gates-log.json, CSVs…) | intake.json / call notes |

If a ground-truth file the review needs is missing, that is itself a P1 finding
("claims unverifiable: no brand-facts.md"), not a reason to skip the check.

## Review protocol

**Step 0 — deterministic first.** Run the applicable validators and read their output
before judging anything by eye. Never re-litigate what a script asserts; triage its
warnings instead.

| Deliverable | Run first |
|---|---|
| Roadmap deck | `scripts/validate-deck.py <deck> --render` · `scripts/validate-prose-tells.py <deck> --client {slug}` |
| Content plan | `scripts/validate-content-plan.py <plan>` |
| Workbook copy / email / report | `scripts/validate-prose-tells.py <files> --client {slug}` |
| Article | the client's article validators (per blog-writer) · `scripts/validate-prose-tells.py` |

**Then review each dimension.** Skip a dimension only if the manifest says it doesn't
apply; say so in the report.

- **A. Strategy fit** — against `icp-profile.md`: right audience, right buyer intent,
  anchored to what the client actually sells and doesn't; sequencing/framing serves the
  client's goal, not generic best practice.
- **B. Factual accuracy** — every claim traced. Client claims → `brand-facts.md` or the
  live site (fetch it). External stats, named studies, citations → verify on the live
  web; a plausible citation that doesn't resolve is fabricated until proven otherwise.
  Competitor claims → check the competitor's live site.
- **C. Data integrity** — recompute displayed numbers from the source artifacts.
  Post-gate figures where the standard requires them (a raw-gap number presented as
  opportunity is a P1). Cross-artifact consistency (cover stat = trajectory baseline,
  slide stats = plan JSON).
- **D. Brand voice + client rules** — config voice, FEEDBACK.md rules, rejected
  topics, house rules for the deliverable type (e.g. decks: second person throughout,
  no performance guarantees).
- **E. Humanization** — apply `references/humanize.md` (the house AI-tells checklist).
  Triage every prose-tells warning; flag anything a reader would clock as generated:
  template phrasing, recurring stock phrases, abstract virtue-copy where a concrete
  specific belongs.
- **F. Mechanics** — grammar, spelling, punctuation, casing per the house type rules.
- **G. Format compliance** — the deliverable's own checklist, item by item.

**Evidence rule:** every finding names its location (slide/row/line), quotes the
offending content, and states what convinced you (URL fetched, number recomputed,
rule cited). A finding you cannot evidence goes to P3 as a question, not P1/P2.

## Output contract — `qa-report.md`

```markdown
# QA Report — {deliverable} — {client} — {date}
Verdict: SHIP | FIX | BLOCK
P1: {n}  P2: {n}  P3: {n}

## P1 — must fix before this reaches the client
- [B] Slide 6 claims "57 pages missing meta" — crawl covered 100 of 340 sitemap URLs;
  live check confirms the sitemap total. Fix: "57 of the 100 pages we crawled".

## P2 — should fix
## P3 — notes and questions
## Verified clean
- one line per dimension: what was checked and how
```

Verdict: **BLOCK** = any P1 (factual error, unverifiable claim, wrong/raw numbers,
banned phrase, missing required element). **FIX** = P2s only. **SHIP** = at most P3s.
No politeness credit: an empty P1 section must mean you tried to refute the work and
failed, not that you skimmed it.
