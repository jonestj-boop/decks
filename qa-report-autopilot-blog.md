# QA Report (round 3) — Go-to-market plan deck — autopilot-blog — 2026-10-14
Content verdict: FIX
P1: 0  P2: 1  P3: 5
Process gap (separate from the content verdict): there is still no `clients/autopilot-blog/brand-facts.md`. Every client claim traces to the verbatim transcript addendum in `call-notes-2026-10-12.md`. Build brand-facts.md from that addendum.

**Reviewed:** local `decks/autopilot-blog.html` at commit f47c1d6, working tree clean, no diff against `upstream/main`. The live https://decks.embertribe.com/autopilot-blog serves the same version: it shows "$4,250", and render metrics were taken on the live page.

**Ground truth:**
- `call-notes-2026-10-12.md` with its transcript addendum.
- `call-notes-2026-10-14-tj-instructions.md`, authoritative for pricing and scope: $1,500 covers Google + Meta, $1,250 when bundled, no separate Meta fee, remove the fee-breakdown note, paid media + creative only.
- `partner-rate-cards.html`.

## P1 — must fix before this reaches the client
None. Each of the following was tested and could not be refuted:
- **Fee figures:** the only fee figures left are $1,500 and $1,250 (slide 12) and the $1,500 fee (slide 9). Searched for leftovers: no $2,500 fee, no $1,000 Meta line, no $5,500, no $1,830/$1,850, no "Our fee is … of that" note, no rate-card attribution, no "$20K" ceiling. The $1,000 figures that remain are the client's $1,000 price tier, the slide 3 6-month max CAC, and the slide 9 Meta *ad spend*. All are correct.
- **Slide 12 math:** $1,500 + $3,000 = $4,500, and $1,250 + $3,000 = $4,250 ✓.
- **Slide 9 math:** ($3,000 + $1,500) ÷ 3 = $1,500 and ÷ 2 = $2,250 ✓. Payback: $1,500 ÷ $500 = 3.0 months and $2,250 ÷ $500 = 4.5 months, so "three to five months" ✓. The other rows are unchanged and still recompute: $250 per demo, 6 pilots, 40% → 2–3 customers, $1,000–$1,500 ad spend per customer, $9,000–$13,500 LTV.
- **Slide 3:** LTV $3,000 / $4,500 / $6,000 with 3:1 maxima $1,000 / $1,500 / $2,000 ✓. 30–60× of $100 ✓.
- **Slide 3 vs slide 9:** consistent. Slide 3's target is explicitly ad spend per customer ($1,000–$1,500), with "Our management fee comes on top of that … (see slide 9)". Slide 9's ad-spend row is the same $1,000–$1,500, and the fee-inclusive cost is shown separately.
- **Bundle wording:** matches TJ's instruction, and the FFmpeg Micro deck states the same $1,500 → $1,250 bundle (`decks/ffmpeg-micro.html` lines 581 and 597).
- **Scope:** paid media + creative only.
  - Slide 12 includes campaign strategy and builds, creative, ad tracking (UTMs and platform conversion tracking), targeting and optimization, and reporting.
  - Slide 14 now says "We build campaigns and draft ad creative while the site is built."
  - Slide 6 and slide 11 split the work cleanly: Javid owns the site, GA4 and CRM, and EmberTribe owns the ad-side tracking.
  - Reseller outreach is "Your track".
  - Slide 13 is "to discuss", with no terms and no CRO.
  - No site build, launch support, CRO, outbound, AI Visibility or Reddit appears.
- **Client facts:** checked against the notes and addendum. Roofer/impressions quote, med spas and roofing, packaging, reassurance/guarantee, customer-roadmap ideas, ~20 customers, $300–$1,000, ~90% SMB, two resellers, close process, 3–4 week site, call time and split. No Napkin, sale or IPO.

## P2 — should fix
- **[G] Slide 6 headline: "Seven pages, one goal: a booked demo."** Slide 6 now shows only two vertical pages ("/roofing and /med-spas"). The page cards are Home, /roofing, /med-spas, How it works, Lead magnet and Partners, which is **six**. The sixth card, Tracking, is not a page. The headline only reaches seven if a demo-booking page is counted, and the slide never names one; slide 11 lists "demo booking" separately. This mismatch was introduced when the third vertical was dropped. Fix: "Six pages, one goal: a booked demo." Or add the demo-booking page to the slide.

## P3 — notes and questions
- [B] Slide 5: "Your rep already talks to roofers and med spas **every week**." The transcript supports that she talks to them ("talks to a med spa or roofing company or whatever") but not how often. Drop "every week".
- [C] Slide 3: "Our management fee comes on top of that, so **early months** cost more per customer." The fee is flat, so fee per customer only falls if customer volume rises. Nothing in the deck says it is front-loaded. Consider "so the all-in cost per customer is higher (see slide 9)."
- [B] Slide 12 bundle condition: "$1,250 when you also sign up for the FFmpeg Micro plan." Under TJ's FFmpeg instructions, Foundation is a one-time $500 in month 1 and brand mentions start in month 2. Confirm with TJ whether $1,250 holds only while an FFmpeg retainer is active, or for the whole Autopilot term if Javid buys Foundation only. Javid may ask.
- [A] Slide 11: four weeks of "Us: campaign builds … first ad creative" happen before "The 90-day term starts the day ads go live", so the prep is unbilled. Carried from round 2. Fine if TJ agrees.
- [E] "FFmpeg Micro blog's growth" appears 4× (slides 5, 6, 8, 12), just over the ~3 recurrence guideline. "demo(s), pilot(s), paid" is down to 3×. The validator WARN (rule-of-three ×10) is benign on read-through.

## Verified clean
- **Validators:** with PYTHONUTF8=1, `validate-deck.py --render` PASS (divs balanced; render skipped because Chrome wasn't found) and `validate-prose-tells.py` PASS with one WARN, triaged above.
- **Layout at 1440×900** on the live page, Quatro 400/600/700 loaded: content slides 2, 3, 5, 6 and 8–14 are all 844/844 with no overflow. Slides 1, 4 and 7 report 1065 only because of the decorative "e" glyph, which `overflow:hidden` clips. That is a false positive.
- **Round-2 fixes confirmed:**
  - slide 14 page copy removed;
  - rate-card source line removed;
  - $20K fee-ceiling line replaced with "doesn't change with spend during the test";
  - "closes" changed to "talks to";
  - slide 7 now reads "two vertical pages";
  - vertical pages consistent (two at launch, third after 90 days);
  - reseller outreach timing consistent ("after the 90-day test" on slides 10 and 11);
  - "curve" leftover fixed.
- **Term wording:** "Three-month term from launch day, our standard for ongoing work" matches the rate card's "3-month commitment (default)".
- **No performance guarantees:** targets and assumptions are labeled "not forecasts".
- **Brand and mechanics:** red cover and dividers, black and white body, a single slate accent, ALL CAPS labels, sentence-case headings, title and nav. No inline em dashes. Second person throughout. No spelling or grammar errors.
