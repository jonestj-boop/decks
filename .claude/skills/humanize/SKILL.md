---
name: humanize
description: Remove AI-writing patterns from any text or file — titles, deck copy, emails, articles, docs. Use when user says "humanize this", "this reads as AI", "remove the AI patterns", "make this sound human", or "de-AI this". Rewrites in place using the house AI-tells checklist without changing any fact.
---

# Humanize

Ad-hoc entry point to the house humanization layer. The checklist and method live in
**`.claude/skills/qa-review/references/humanize.md`** — read that file first and follow
it; this skill only defines the standalone workflow around it.

**Copies:** canonical in the EmberTribe repo; mirrored to embertribe-decks. Edit the
EmberTribe copy and re-mirror. The scanner falls back to a sibling EmberTribe checkout
for the banned-phrase lists; without one it still checks dashes, vocabulary, and
constructions.

## Workflow

1. **Scope.** Identify the target (file paths or pasted text) and, if it belongs to a
   client, the client slug — their `banned-title-phrases.yaml`, `rejected-topics.yaml`,
   `config.yaml` voice, and `FEEDBACK.md` apply on top of the global checklist.

2. **Scan before.** For files, run the deterministic layer and keep the output:

   ```bash
   python3 scripts/validate-prose-tells.py <files> [--client {slug}]
   ```

3. **Two-pass rewrite** (per the checklist):
   - *Rewrite pass* — fix flagged and pattern-matching prose by saying the concrete
     thing, not by swapping a flagged phrase for a synonym of itself. Structure is
     movable; sentences that only exist to hold a pattern get merged or cut.
   - *Verify pass* — re-check against the checklist AND confirm no fact changed: every
     name, number, date, claim must still trace to its source. If the text carries
     client claims, check them against `clients/{slug}/brand-facts.md` when it exists.

4. **Scan after.** Re-run the scanner; it must print PASS (or only warnings you can
   defend). Before/after scanner output is the proof of work.

5. **Report.** Show what changed and why, grouped by pattern (banned phrase, recurrence,
   construction, vocabulary), plus anything left deliberately with a one-line defense.

## Rules

- **Never change facts.** A humanization edit that invents, drops, or shades a claim is
  a worse defect than the tell it fixed.
- **House constants survive every rewrite**: second person for decks and client notes ·
  verified claims only · sentence-case headers · no em dashes inside client prose
  (leading bullet glyphs are house style) · no performance guarantees · no emoji in
  client deliverables.
- Edit prose only — leave code, data, frontmatter, URLs, and markup structure alone.
- **Feed the loop.** If the text came back from a client who flagged specific phrasing,
  add those phrases to the client's `banned-title-phrases.yaml` (or topics to
  `rejected-topics.yaml`) in the same session, per the checklist's feedback-loop rule.
- For a full pre-delivery review (facts, strategy, data integrity — not just prose),
  use the `qa-review` skill instead; this skill is the writing pass only.
