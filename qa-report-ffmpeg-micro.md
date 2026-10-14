# QA Report (round 3): ffmpeg-micro.html, 14-slide strategy deck, FFmpeg Micro, 2026-10-14
Content verdict: BLOCK
P1: 1  P2: 1  P3: 10
Process gap (separate from the content verdict): there is still no `clients/ffmpeg-micro/brand-facts.md`.

Reviewed: local `decks/ffmpeg-micro.html`. The live decks.embertribe.com/ffmpeg-micro is identical apart from line endings (diffed after CR strip).
Ground truth: call notes Oct 12 plus addendum, **TJ instructions Oct 14 (authoritative for pricing and scope)**, `gsc_ffm.json`, the Semrush Backlink Gap CSV, brand-mentions pricing memory, the XKGLOW memory (brand-mention term precedent), and `decks/autopilot-blog.html` (bundle cross-check).

## Step 0: validators
- `validate-deck.py`: PASS (with `PYTHONUTF8=1`; render check unavailable, so I checked rendering by hand, see G).
- `validate-prose-tells.py --client ffmpeg-micro`: clean, PASS.
- Em dashes appear only as the CSS bullet glyph.

## Round-2 findings: disposition
- **P2 slide 13 unsourced terms.**
  - Foundation: resolved. It's now "one time, Month 1", which matches TJ's instruction.
  - Brand mentions "3-month term": downgraded to P3. TJ's instructions are silent on it, but house precedent (XKGLOW, Oct 6) sells brand mentions as a quarter-long commitment, so it's plausible. Confirm it with TJ.
- **P2 TechCrunch/ZDNet in column 3:** fixed. Both moved to an "earned press, not placements" note. Column 3 now has 7 rows, all matching the CSV (logrocket 57 / Mux 6; sitepoint 54 / Mux 8, api.video; towardsdatascience 54 / Mux; smashingmagazine 53 / Mux, api.video; stackoverflow.blog 51 / Mux, api.video; videohelp 51 / Mux 10, Creatomate; thenewstack 50 / Mux). Total is 9 + 9 + 7 = 25, which matches "The first 25 targets".

## TJ-instruction compliance (Oct 14)
| Instruction | Deck | Status |
|---|---|---|
| Gap links "quoted per link" | Slide 10 lever 2 "Quoted per link"; slide 12 "quoted per link"; slide 13 "competitor gap links quoted per link" | OK |
| Brand mentions is the recommended starting lever | Slide 10 title "We'd start with brand mentions", "Start here" tag on lever 4 | OK |
| Reddit callout removed | None found on slide 10. "reddit" survives only as a search string on slide 8, which is fine | OK |
| Foundation = one-time $500, Month 1 (listings, merge map, AI baseline, tracking) | Slide 13 lists exactly those four items at "$500 one time, Month 1"; slide 12 says "$500 one time"; the cover and slide 14 match | OK |
| Brand mentions start Month 2, Starter $1,498 suggested | Slide 13 "Month 2 on", "Suggested start" on Starter; slide 12 Months 2–4; slide 14 question | OK |
| Editorial links $500 at DR 30+ | Slides 5, 7, 10, 13 all say DR 30+. **No DR 50+ link wording is left.** The "Authority 50+" mentions on slides 6–7 are Semrush AS gap tiers, not a link tier | OK |
| Bundle: Autopilot paid media + creative $1,250 instead of $1,500 | Slide 13 callout and slide 14 question say $1,250 vs $1,500. The price is right; the wording is in P3 | OK (P3 on wording) |
| No recurring-Foundation leftovers | No "/ month", "Every month", or "$500 a month" Foundation wording remains | OK |

## P1: must fix before this reaches the client
- **[A/C] Slide 9 divider still tells the old story.** It reads: "Listings first, then links to the pages already close to page one, then brand mentions once those links are paying back."
  - Every other slide now says the opposite order. Slide 10 says "We'd start with brand mentions… so that's where we'd begin". Slide 12 says Months 2–4 are "Mentions" with links "as needed". Slide 13 says "Brand mentions start in Month 2".
  - It's the section opener for "The plan", so Javid reads the wrong plan first.
  - Fix, for example: "Listings and the merge map in Month 1, then brand mentions from Month 2, with links added where a page is close to page one. Spend scales with the results."

## P2: should fix
- **[A] Slide 2 budget callout and the cover don't match the new spend.**
  - Slide 2 restates Javid's budget: "start under $1,000 a month on the foundational work, then step up into link building and brand mentions as rankings and sign-ups move."
  - The plan now moves to $1,498/mo from Month 2 on a 3-month term ($4,494, plus any links). That's before any ranking or sign-up checkpoint, and above the "less than a thousand a month, like 500" he named (call notes).
  - The cover's "scaling only when the numbers say so" has the same tension.
  - The pricing is TJ's call, but the deck never reconciles it with the budget it quotes back to him, and he'll notice.
  - Fix: on slide 2 or 13, acknowledge it directly. For example: "Month 1 stays under your $1,000 ceiling. Starter mentions at $1,498 are the step up, and we'd only start them if you're comfortable after Month 1." Alternatively, reword the slide 2 budget line so it doesn't promise the step-up waits for results.

## P3: notes and questions
- **[D] Bundle wording.** Slide 13 says "Autopilot Blog Google + Meta management". TJ's instruction and `autopilot-blog.html` (line 470: "Paid media + creative · Google Search + Meta … $1,250 when you also sign up for the FFmpeg Micro plan") call it paid media **+ creative**. Align the two labels.
- **[A] Bundle qualifier is ambiguous.** "Sign up for this plan" could mean the one-time $500 Foundation alone. Does that earn a standing $250/mo Autopilot discount, or does it require Starter mentions? Have TJ confirm and state it.
- **[B] Brand-mention "3-month term, starting Month 2"** has no source in the TJ instructions. It's consistent with house precedent (XKGLOW quarterly). Confirm.
- **[A] Slide 12 checkpoint vs the term.** The subtitle says "If rankings and sign-ups don't move, we change course before spending more". But the 3-month mention term commits all of Months 2–4 before the phase checkpoint, so state that the checkpoint falls at the end of the first term.
- **[E] Slide 10 has two "fastest" claims.** Lever 2 is "The fastest wins" and brand mentions is "the quickest way into those answers". They're about different targets (Google vs AI answers), but read together they compete. Consider "Short pitches" for lever 2.
- **[C] Break-even (slide 13) is verified.** $500 / $100 LTV = 5 users. $1,498 / $100 = 14.98, so "about 15 a month" is right. The framing is honest; 15 new paying users a month is ambitious against ~200 active users, and the deck doesn't hide that.
- **[B] Postman.** The source is on file (addendum: Crunchbase and Startups Rising), but I still couldn't re-fetch it independently (Crunchbase returns 403). Have TJ confirm it on the call. The sources-line citation of his own Crunchbase is optional.
- **[C] Slide 6 "10" card.** It's correct, but the 10 include bing.com and grokipedia.com, while slide 7 says search engines were excluded. It could be 8 without those two.
- **[D] Slide 7.** "The full 335-domain list comes with the engagement" sits mildly against "on us". The complimentary framing still reads clearly on slides 6, 7, 13 and 14.
- **[Tooling]** Both validators need `PYTHONUTF8=1` on Windows (or `-X utf8`, because `-I` ignores env vars). `--render` can't find Chrome.

## Verified clean
- **A. Strategy:** apart from the slide 9 and slide 2 items above, the order is consistent across slides 1, 7, 10, 12, 13 and 14: Month 1 Foundation $500 one time, mentions from Month 2, links as needed.
- **B. Facts:**
  - Call figures on slide 2 match the notes.
  - Slide 11 product facts match the live /pricing and /llms.txt (round 1).
  - TipsyTech and "Founder & CEO" are on the live site.
- **C. Data:**
  - The GSC numbers on slides 3–5 recompute unchanged from round 2.
  - Gap counts recompute: 14,747 / 335 / 47 / 10, plus the per-competitor domains and AS 50+ counts.
  - All 25 prospect rows match the CSV, and TechCrunch 72 / ZDNet 60 are correct.
  - Brand-mention prices and per-mention math are correct.
  - Both break-even figures are correct.
  - Slide cross-references (4, 5, 6 and 7) are correct.
- **D. Voice:** second person throughout, no guarantees, every outcome hedged. The complimentary gap is stated on 4 slides.
- **E. Humanization:** the scanner is clean, there are no point announcements, and nothing new reads as template.
- **F. Mechanics:** no spelling or grammar errors found. Headers are sentence case and labels are in caps.
- **G. Format and render:**
  - Red cover and divider, a black/white body, and #2563EB as the only accent. Quatro loads.
  - At 1440×900 on the live URL, all 14 slides fit with no vertical or horizontal overflow. Minimum clearance below the last content element is 61px (slide 7); slide 13 is 96px, and its bundle callout ends at y=748 of 844.

## Process gap (separate from the content verdict)
- `clients/ffmpeg-micro/brand-facts.md` is still missing. This round, every client claim was traced to the call notes, the addendum, TJ's Oct 14 instructions, or the live site instead.
- Create it in the EmberTribe repo before the next FFmpeg Micro or Autopilot Blog deliverable.
