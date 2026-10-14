# QA Report (round 2): ffmpeg-micro.html, 14-slide strategy deck, FFmpeg Micro, 2026-10-14
Content verdict: FIX
P1: 0  P2: 2  P3: 9
Process gap (logged separately, not counted in the content verdict): no `clients/ffmpeg-micro/brand-facts.md`.

Reviewed: local `decks/ffmpeg-micro.html` (working tree, round-2 edits). The live URL was not re-checked this round. Round-1 report superseded.
Ground truth: call notes incl. the round-2 addendum, `gsc_ffm.json`, Semrush Backlink Gap CSV, brand-mentions pricing memory, partner-rate-cards.html, and the live ffmpeg-micro.com (/about, /pricing, /llms.txt) from round 1.

## Step 0: validators
- `validate-deck.py`: PASS with 146/146 divs balanced. It needs `PYTHONUTF8=1` on Windows. Its render check is unavailable (no Chrome), so I checked rendering by hand, see G.
- `validate-prose-tells.py --client ffmpeg-micro`: clean, PASS. Also needs `PYTHONUTF8=1`.
- Em dashes: the only ones are the CSS `::before` bullet glyphs, which are allowed.

## Round-1 findings: disposition
| Round-1 item | Status |
|---|---|
| P1 Postman claim unverifiable | **Downgraded to P3.** The call-notes addendum now cites Crunchbase ("Head of Engineering - Growth @ Postman") and a 2026 Startups Rising listing. I couldn't independently re-fetch either: Crunchbase returns 403 and two web searches found nothing. A documented source now sits in the ground truth, so per the evidence rule this is a question, not a blocker. See P3. |
| P1 Slide 4 "12 more URLs" row | **Fixed.** I recomputed it: 71 impressions, positions 3.0 to 86.5, shown as "3 to 87". The subtitle "best-of post … at 8.4, and five more pages compete from page two and three" now matches: /docs 17.9, 20.3, 21.0, 23.3, 24.2. |
| P1 Slide 6 "203" spam count | **Fixed.** Replaced by "10 Authority 50+ sites that link to three or four of your competitors". The 10 recomputes exactly, with one composition note in P3. |
| P1 Missing brand-facts.md | Moved to the process gap per the coordinator, see the bottom of this report. |
| P2 DR vs Authority Score | **Fixed.** Slide 3 now reads "AS 12, Semrush Authority Score". "The tier your link plan buys in" is gone. Slide 7 adds "we confirm each site's DR before pitching". The sources line reads "Authority Scores from Semrush". |
| P2 "Pricing from rate card" | **Fixed** ("EmberTribe pricing" on slides 13 and 14). The term lengths remain unsourced, see P2-1. |
| P2 Shotstack on slide 10 | **Fixed** (Creatomate). Shotstack now appears only on slide 5, where it correctly refers to the /vs/shotstack page. |
| P2 TrustRadius/Latka below 50 | **Fixed.** The subtitle now says "plus a few review sites and integration platforms below 50". |
| P2 Medium/Substack/Veed/GetStream as $500 editorial | **Fixed.** Column 3 has been replaced, but the replacement brings a new issue, see P2-2. |
| P2 "Columns 1 and 2 go in Month 1" | **Fixed.** Now "start in Month 1", with * marking zapier, pypi, packagist, pipedream, pabbly, latenode, and socket.dev. |
| P2 "a few dozen … into the top three" | **Fixed.** Now "aims to move the ten buyer pages on slide 5 toward the top three". |
| P3 ~91%/~9% definition | **Fixed.** Now "9 in 10" and "1 in 10"; the source data gives 7.4% to 10.7% depending on definition. |
| P3 WebCatalog omitted api.video | **Fixed** (api.video 33 added, matches the CSV). |
| P3 25% phrasing | **Fixed.** Slide 2 now says "on your post about getting an FFmpeg API key, per your analytics". |
| P3 "keeps adding sign-ups" | **Fixed** ("can keep adding"). |
| P3 "Here's …" point announcements | **Fixed** (0 left). |
| P3 table header "Referring domains" | **Fixed** ("Domains linking to them, not you"). |

## P1: must fix before this reaches the client
None. I tried to refute every recomputed number on slides 3 to 7 and every changed line, and found nothing that rises to P1.

## P2: should fix
1. **[B] Slide 13: two contract terms with no source.**
   - Foundation: "Month to month after the first 90 days".
   - Brand mentions: "3-month term".
   - Neither appears in the call notes, TJ's Oct 14 instructions, the brand-mentions pricing memory, or the rate card. The prices themselves are correct.
   - Fix: TJ confirms both terms, or remove them.
2. **[A] Slide 7, column 3 "Editorial links … This is where the $500 DR 50+ links go."**
   - techcrunch.com (AS 72) and zdnet.com (AS 60) are newsrooms. They don't run vendor-contributed or placed posts, so a link from them is earned press coverage, not a $500 placement.
   - Listing them under the $500 price tells Javid we can buy TechCrunch for $500. The callout "each placement is pitched, written, and placed by our team" reinforces that.
   - The other seven accept contributed or pitched technical articles, so they fit the label: logrocket, sitepoint, towardsdatascience, smashingmagazine, stackoverflow.blog, videohelp, thenewstack.
   - Fix: move TechCrunch/ZDNet to a "press / earned" note, or swap in two contributor-friendly outlets from the 335 list.

## P3: notes and questions
- **[B] Postman.** The source is now on file (call-notes addendum: Crunchbase plus Startups Rising). I couldn't re-verify it independently. Two suggestions:
  - TJ should confirm it verbally in the first minutes of the call, or soften the line to "with your growth-engineering background at Postman…" only if he's confident in it.
  - The sources line "Postman role per Javid's Crunchbase profile" cites the prospect's own bio back to him. It's harmless, but you could drop it from the client-facing footnote.
- **[C] Slide 6 "10" card.** The count is correct, but the 10 sites are:
  - ycombinator.com, alternativeto.net, g2.com, webcatalog.io, producthunt.com
  - veed.io, a vendor
  - medium.com and substack.com, open platforms
  - bing.com, a search engine
  - grokipedia.com
  
  Slide 7 says search engines were left out. Consider "8" without bing and grokipedia, or leave it as a raw count.
- **[C] Slide 7 column 3 recompute.** All 9 rows match the CSV exactly: techcrunch 72 (Mux 8, api.video 2), zdnet 60 (Mux), logrocket 57 (Mux 6), sitepoint 54 (Mux 8, api.video), towardsdatascience 54 (Mux), smashingmagazine 53 (Mux, api.video), stackoverflow.blog 51 (Mux, api.video), videohelp 51 (Mux 10, Creatomate), thenewstack 50 (Mux). Six of the nine link only to Mux, which is fine for the "Mux sets the bar" framing.
- **[D] Complimentary framing vs gated list.** Slide 7 still says "The full 335-domain list comes with the engagement", which sits slightly against "on us". The complimentary framing reads clearly overall on slides 6, 7, 13 and 14. This is TJ's call.
- **[A] Foundation economics.** $500 covers one $500 link plus the Month-1 listings, the merge map, the 30-prompt baseline and reporting. That's consistent with TJ's instruction, but confirm the labor is intentionally included.
- **[B] Slide 8 off-Google spot check.** The framing is honest: dated, "a snapshot, not a ranking report", first page only. It can't be re-run exactly. The AlternativeTo Rendi page was spot-checked in round 1 and confirms the claim.
- **[E] Light recurrence.**
  - "Not X" constructions: "a snapshot, not a ranking report" appears twice, plus "paying users, not impressions".
  - The "scale" motif appears four times.
  - Neither is a rule breach.
- **[Tooling] Validators.** Both crash under cp1252 unless `PYTHONUTF8=1` is set. Note also that `python -I` ignores PYTHON* env vars, so use `-X utf8`. validate-deck's `--render` can't find Chrome.
- **[G] Slides 1 and 9.** scrollHeight is larger than the viewport only because of the decorative "e" pseudo-element inside overflow:hidden. Nothing is visible, so there's no defect.

## Verified clean
- **A. Strategy:** organic-first, under-$1K Foundation, then links, then brand mentions. This matches Javid's stated budget and sequence. No AI Visibility packages or Reddit are sold.
- **B. Facts:**
  - Slide 2 call figures match the notes.
  - Slide 11 facts match the live /pricing and /llms.txt (round 1).
  - TipsyTech is on the homepage, and "Founder & CEO" is on /about.
- **C. Data:**
  - Totals: 9,408 clicks, 1.42M impressions, 4,019 in September, 971 for the GIF tool.
  - Slide 4: 19 URLs, 1,271 impressions, rows 1 to 7, and the 12-URL row (71 impressions, positions 3 to 87).
  - Slide 5: every row recomputes.
  - Slide 6: gap counts 14,747 / 335 / 47 / 10, plus the per-competitor domains and AS 50+ counts.
  - Slide 7: all 27 rows recompute.
  - Slide 13: brand-mention prices and per-mention math; break-even 5 × $100 = $500.
  - Cross-references: slides 4, 5, 6 and 7 are referenced correctly.
  - No leftover Build/Scale plans, "$250", "DR 12", "rate card", "203", or "few dozen". "DR 30 to 60" appears only for brand mentions.
- **D. Voice:** second person throughout. Every outcome claim is now hedged ("aims to", "can keep adding").
- **E. Humanization:** the scanner is clean and the point announcements are removed.
- **F. Mechanics:**
  - No spelling or grammar errors found.
  - Headers are sentence case and labels are caps.
  - Em dashes appear only as bullet glyphs.
- **G. Format and render:**
  - Red cover and divider, a black/white body, and client blue #2563EB as the only accent. Quatro loads.
  - At 1440×900, local build: all 14 slides fit with no vertical or horizontal overflow. Minimum clearance below the last content element is 72px (slide 7).

## Process gap (separate from the content verdict)
- `clients/ffmpeg-micro/brand-facts.md` does not exist. The skill rates this as P1-level for verifiability. This round, every client claim was traced to the call notes (now with the addendum) or the live site instead.
- Fix before the next FFmpeg Micro or Autopilot Blog deliverable: create brand-facts.md in the EmberTribe repo from the call notes, the addendum and the /about + /llms.txt facts.
