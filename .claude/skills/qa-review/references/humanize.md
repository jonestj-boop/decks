# Humanize — the house AI-tells checklist

Why this exists: a Bomme Studio reviewer read our roadmap recommendations and named the
problem precisely — "several obvious AI patterns throughout, including repetitive
phrasing, and language that immediately reads as generated content." The five phrases
they quoted are now permanently banned. This file is the general rule behind that
feedback, adapted from github.com/blader/humanizer (itself built on Wikipedia's "Signs
of AI writing"), tuned to EmberTribe deliverables.

Layers:
1. **Deterministic** — `scripts/validate-prose-tells.py` (banned phrases, em dashes,
   chatbot leakage = FAIL; high-signal vocab + construction density = WARN) and
   `scripts/validate-content-plan.py` (recurring non-keyword phrases across titles).
2. **Judgment** — this checklist, applied by the writer before handoff and by qa-review
   dimension E with fresh eyes.

---

## The core principle: concrete beats abstract

Template-tell copy describes virtues; human copy names things the reader can picture —
an action, an object, a number, a step. The Bomme fix is the reference example:

| Reads as generated | Shipped instead |
|---|---|
| "How to Vet One for Quality and Scale" | "The Sourcing Questions That Predict Quality" |
| "The Real Numbers Behind the Quote" | "Reading a Quote Line by Line" |
| "Domestic vs Overseas, Weighed Honestly" | "Domestic vs Overseas for Performance Lines" |
| "The Fundamentals, Minus the Jargon" | "What Goes Into a Technical Garment" |

When a phrase promises a virtue (honesty, clarity, no-nonsense, real talk), delete the
promise and demonstrate the virtue: say the concrete thing.

## The recurrence rule

No non-keyword phrase appears in more than ~3 places across one deliverable. Angle and
subtitle pools must be wide and concrete — a short rotation ("A Production-Partner
Checklist" ×9) reads as automation even when each instance is individually fine.
Repetition is the tell clients notice first.

## Tells checklist

**Vocabulary** (any hit gets a second look; the scanner counts these):
delve · tapestry · testament to · ever-evolving · fast-paced · game-changer ·
revolutionize · cutting-edge · seamless · holistic · unleash · supercharge · elevate ·
"in today's …" · "in the world of" · "when it comes to" · "look no further" · "we've
got you covered" · "navigating the …" · "unlocking the …" · "treasure trove" ·
"whether you're X or Y" · "dive into / deep dive / let's dive in" · "it's important to
note / worth noting"

**Constructions:**
- "Not X but Y" / "isn't just X, it's Y" / "more than just" — more than ~2 per document
  is a pattern. (One, placed deliberately, is fine — the house call line "that's the
  plan working, not the plan failing" earns its slot.)
- Forced triplets — "innovation, inspiration, and insights." Vary list lengths; two
  items or four are allowed to exist.
- Shallow -ing chains — "…, symbolizing X, reflecting Y, showcasing Z."
- False ranges — "from A to B" spans that don't measure anything.
- Qualifier stacks — "could potentially", "arguably one of the most".
- Filler — "in order to", "due to the fact that", "it should be noted".
- Avoiding is/are — "serves as", "boasts", "features" as copula-dodges.

**Structure:**
- Point announcements — "Let's break it down", "Here's the thing".
- Fake-candid openers — "Honestly?", "Let's be real".
- Fake deeper truth — "At its core, …", "At the end of the day, …".
- Generic positive endings — "The future looks bright", "…is well worth it".
- Answering objections nobody raised; rejecting alternatives nobody proposed ("This
  isn't about chasing trends").
- Bold-mini-heading bullet lists where prose would carry it; heading restated as the
  first sentence under it.
- Em dashes inside sentences — house rule is zero in client prose. (An em dash as a
  *leading bullet glyph* is embertribe-design house style and allowed; the scanner
  distinguishes the two.)
- Sentence-case headers (house rule); no emoji in client deliverables.

**Content:**
- Inflated importance — "a pivotal step in {client}'s journey".
- Vague authority — "experts agree", "studies show" without a named, checkable source.
- Sales adjectives doing the work of facts — "breathtaking", "world-class".
- Formulaic aphorisms — "Consistency is the language of trust."

## The two-pass fix protocol (for the writer, before handoff)

1. **Rewrite pass** — fix flagged prose by saying the concrete thing, not by swapping
   the flagged phrase for a synonym of itself. Treat structure as movable; merge or cut
   sentences that only existed to hold a pattern.
2. **Verify pass** — re-check against this list AND confirm no fact changed: every
   name, number, date, claim in the rewrite must still trace to its source. A
   humanization pass that invents or drops a fact is a worse defect than the tell was.

House constants that survive every rewrite: second person for decks and client notes ·
verified claims only · sentence-case headers · no em dashes in client prose · no
performance guarantees.

## Feedback loop

When a client (or anyone) flags a phrase as template-tell: add it to the producing
client's `banned-title-phrases.yaml` the same session; if a second client flags the
same phrase, promote it to the skill-global list. The scanner enforces from then on —
feedback becomes a permanent gate, not a memory.
