# QA Report (round 2) — Go-to-market plan deck — autopilot-blog — 2026-10-14
Content verdict: BLOCK
P1: 1  P2: 2  P3: 7
Process gap (logged separately, per the skill): no `clients/autopilot-blog/brand-facts.md`. Client claims now trace to the verbatim transcript addendum in the call notes. Create brand-facts.md from that addendum so future reviews have a canonical source.

File reviewed: `decks/autopilot-blog.html` (local). Ground truth: `scratchpad/ffm/call-notes-2026-10-12.md`, including the round-2 transcript addendum. Rate card: `decks/partner-rate-cards.html`. Coordinator's round-2 change list.

## Round-1 findings, re-checked
| Round-1 item | Status |
|---|---|
| P1 4,019 labeled as blog clicks | **Resolved.** Slide 2 now shows 3,141, with the source line "pages under /blog/". Taken as given per the coordinator; framing is fine. |
| P1 untraced client claims | **Resolved.** Each claim now traces to the addendum: roofer/impressions ("they don't give a [expletive] about impressions"), med spas and roofing, packaging ("what types of services we're packaging with it"), low tech (reworded to "buyers who need more reassurance"), and customer roadmap ideas ("a lot of direction already from my existing customer base"). The multi-client dashboard is gone. |
| P1 landing-page brief/review | **Resolved on slides 6 and 12.** But see the new P1: page copy reappears on slide 14. |
| P2 3:1 vs fee-inclusive cost | **Resolved.** The slide 3 target is now ad spend only and points to slide 9. |
| P2 timeline | **Resolved.** The term starts when ads go live; slides 9, 11, 12 and 14 agree. |
| P2 scope blur | **Resolved:** cover, tracking split, slide 13 and the slide 8 "Your track" label. |
| P2 rate-card attribution | **Not resolved.** Still on slide 14 (see P2 below). |
| P2 "gets cheaper" | **Reworded.** The new wording raises its own issue (see P2 below). |
| P2 humanization | **Mostly resolved.** "X, not Y" constructions are cut to about two. A recurrence remains (P3). |

## P1 — must fix before this reaches the client
- **[A/G] Slide 14 "Next steps": "We draft ad creative and vertical page copy while the site is built."** Writing the vertical landing-page copy is site and launch work. TJ's instruction was "no launch support (Javid ... builds the site); stick to paid media and creative." The slide 12 scope correctly lists only campaigns, creative, ad tracking, optimization and reporting. This line commits EmberTribe to unpriced site work in the slide the client reads last. It is the same class of defect as the round-1 landing-brief P1, in a new location. Fix: "We build campaigns and draft ad creative while the site is built."

## P2 — should fix
- **[B] Slide 14 sources still say "Pricing from EmberTribe's current rate card."** The coordinator listed this as removed. The addendum confirms TJ said the $1,500 Google fee is "a deal price (not rate card)". The rate card lists $2,500/mo, and `partner-rate-cards.html` is publicly deployed. Fix: delete the sentence.
- **[B] Slide 9: "Our fee stays flat as spend grows, up to $20K a month."** The $20K ceiling comes from the rate card's $2,500 tier ($0–$20,000 spend). Applied to the $1,500 deal price, it commits EmberTribe to that discounted fee at up to roughly 6.7× the planned spend. TJ didn't instruct that. The rate card also says multi-channel accounts under $10K combined spend "may be adjusted — confirm with Melissa and/or TJ", which applies to the $1,000 Meta line at $3K combined. Fix: get TJ to confirm the ceiling, or use "Our fee doesn't change with spend during the test."

## P3 — notes and questions
- [B] Slide 5: "Your rep already **closes** roofers and med spas." The transcript says she "talks to a med spa or roofing company". "Already sells to" or "already talks to" would be exact. Slide 2 similarly lists roofers and med spas as *customers*. The transcript supports them as who Javid and the rep sell to, and only the photography studio as a named customer. That's low risk, but confirm on the call.
- [G] Slide 7 divider: "Two paid channels against **one vertical page each**". Slides 8, 11 and 12 run Google on two verticals and Meta on roofing plus med spas. This was a round-1 P3 and is still present.
- [G] Slide 6 lists three vertical pages (/roofing, /med-spas, /home-services). Slide 11 has "two vertical pages" before launch and "Add a third vertical page" after 90 days. This round-1 P3 is still present.
- [G] Slide 10 says start agency outreach "in month 3". Slide 11 puts "Start agency and software vendor outreach" under "After 90 days".
- [A] Slide 11 weeks 1–4: "Us: campaign builds, UTMs, ad conversion tracking, first ad creative" happens before the term starts on launch day. That is four weeks of unbilled prep. Confirm TJ is fine with it; otherwise state when billing starts.
- [E] "demo(s), pilot(s), (and) paid" appears 4× (lines 302, 368, 437, 486), over the ~3 recurrence guideline. Slide 8 still says "the FFmpeg Micro curve" while the rest of the deck now says "the FFmpeg Micro blog's growth", which reads as an unconverted leftover. The validator WARN of rule-of-three ×11 is mostly benign: list content varies.
- [Tooling] The validators need `PYTHONUTF8=1` on Windows. `--render` skips because Chrome isn't found, so rendering was checked manually.

## Verified clean
- **Validators:** `validate-deck.py --render` PASS, 129/129 divs. `validate-prose-tells.py` PASS with one WARN, triaged above.
- **Rendering at 1440×900 (Quatro loaded):** all content slides fit (844/844). Slides 1, 4 and 7 exceed only because of the clipped decorative "e" glyph, a false positive.
- **Math:** LTV $3,000/$4,500/$6,000 and ÷3 = $1,000/$1,500/$2,000. 30–60× of $100. $3,000 ÷ 12 = $250 per demo. 6 pilots. 40% of 6 = 2.4 → 2–3. $1,000–$1,500 ad spend per customer. $4,500 × 2–3 = $9,000–$13,500. ($3,000 + $2,500) ÷ 3 = $1,833 ≈ "$1,830" and ÷ 2 = $2,750. Payback 3.7–5.5 months → "four to six". $1,500 + $1,000 + $3,000 = $5,500, of which the fee is $2,500.
- **Client facts** against the notes and addendum: ~20 customers, ~3 months, revenue conditional ("if growth holds"), $300 base / up to $1,000, ~90% SMB, two resellers, warm 1-call / cold 2-call close, 1–2 week pilot, Stripe links, guarantee wording, site in 3–4 weeks, working name, the Oct 14 2 PM CT call split.
- **Scope:** the only priced offer is paid media and creative. There is no site build, CRO, outbound email, AI Visibility or Reddit offer, and no $3,500, $6,500 or $125/hr figure. Slide 13 is framed "to discuss", with no terms. Napkin, the sale and IPO don't appear.
- **No performance guarantees:** funnel figures are labeled as targets and planning assumptions, "not forecasts".
- **Brand:** red cover and dividers, black and white body, a single slate accent, ALL CAPS labels, sentence-case headings, title and nav fixed. Em dashes appear only as bullet glyphs. Second person throughout. No spelling or grammar errors found.
