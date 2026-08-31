# QA Report — Internal Call-Prep Sheet — Stickmadly — 2026-08-31

Verdict: **BLOCK**
P1: 4  P2: 2  P3: 4

File reviewed: `decks/internal/stick-madly/call-prep.html`
Reviewer: fresh-context QA pass, no part in producing the deliverable.

## Step 0 — deterministic validators

- `validate-deck.py` / `validate-content-plan.py`: **not applicable** — this is a one-page internal call-prep reference, not a roadmap deck or content plan. Skipped per manifest.
- `validate-prose-tells.py decks/internal/stick-madly/call-prep.html --client stick-madly`: **ran, FAIL.**
  ```
  ✗ 18 em dash(es) inside prose — house rule: none in client-facing copy
    (leading bullet glyphs are fine)
  ```
  Confirmed by manual grep: 18 em dashes across the title, header, and nearly every finding/agenda/objection line (`grep -n "—" call-prep.html`). See P1-4 below — the manifest directs this dimension to be enforced for internal docs too, per Melissa's standing global rule ("never use em dashes in any writing").

## P1 — must fix before this reaches the call

**[B] Uncorrected claim directly contradicts the doc's own correction, three lines later.**
The "Paid social" finding states: *"This is the whole marketing effort today — no confirmed Google presence."* Immediately below it, the "Google Ads" finding states: *"Correction — Google IS active."* (23 live Display/YouTube ads, verified advertiser). The second finding was clearly added to fix an earlier wrong read of "Google is untouched" — but the first finding was never edited to match. A rep skimming top-to-bottom hits the false claim first. Fix: remove or rewrite "no confirmed Google presence" in the Paid social finding (e.g., "no confirmed Google Search/Shopping presence — see Google Ads finding below").

**[B] "Built on licensed collections" is asserted as fact, then contradicted by the doc's own Discovery Question.**
The Product finding states as fact: *"Premium 3D-textured sticker packs ($8–$80) built on licensed collections — US Army, Navy, Air Force, NASA, FC Barcelona, My Hero Academia, Jujutsu Kaisen..."* But the Discovery Questions column asks: *"Are the military, sports, and anime collections officially licensed, or reproductions?"* — a direct contradiction within the same document. No source in the manifest (site, Meta Ad Library, Semrush, Google Ads Transparency Center) confirms an actual licensing relationship with the U.S. Army, FC Barcelona, or the Japanese IP holders behind My Hero Academia/Jujutsu Kaisen (Shueisha), and none is cited in the doc. Given the SEO section already documents this business buying spammy shortcuts (PBN links), "licensed" is the least likely explanation, not the default one. Fix: change "licensed collections" to "military/sports/anime-themed collections" (or similar neutral phrasing) in the Product finding, and let the Discovery Question stand as the open item — don't assert the fact in one place and question it in another.

**[C] Snapshot revenue and budget figures have no traceable source.**
The header snapshot states "Annual revenue: $0 – $249K" and "Marketing budget / mo: $3K – $4K (incl. fees)." None of the three sources named in the footer ("Meta Ad Library, Semrush Domain Overview, stickmadly.com") produce a revenue band or a budget figure — nothing on the live site publishes revenue or ad spend, Semrush's Domain Overview doesn't estimate company revenue, and Meta Ad Library doesn't show spend. Per the manifest's explicit instruction ("treat any claim you cannot independently verify against a live source... as unverifiable, P1, not something to skip") and given there's no `brand-facts.md` or intake file for this prospect, these two numbers are unverifiable as presented. Fix: either cite where they came from (a prospecting/enrichment tool, a lead form, a call note) in the footer, or mark them as an estimate.

**[E] 18 em dashes in prose — violates a standing personal rule, confirmed by the house scanner.**
`validate-prose-tells.py` fails the file for em-dash usage (house rule: zero in prose). This isn't just house style here — Melissa's global instructions state "never use em dashes in any writing," reinforced in her memory file ("No em dashes — never use em dashes in any writing; use commas, periods, or restructured sentences instead"), and the manifest explicitly says to hold internal docs to this. Every finding, agenda item, and objection-table row in this doc uses an em dash as an internal punctuation mark (e.g., "Come in as '...,' not '...'"; "spend spread across too many creatives at once rather than concentrated behind winners"). Fix: replace with periods, commas, colons, or parentheses throughout — roughly 18 instances.

## P2 — should fix

**[B] Price range overstated at the top end.** The doc claims sticker packs run "$8–$80." Two independent live checks of stickmadly.com (a general product sweep and `?sort_by=price-descending`) found individual stickers from $7.95 and the highest-priced bundle at $69.75 (Barça Femení Stars Pack / FC Barcelona Chibi Players Pack). No $80 item was found in either pass. Fix: "$8–$70" or verify a specific $80 SKU exists before keeping the claim.

**[C] Cross-document number mismatch: "15 spammy PBN links" vs. "18 links / 15 domains."** The Account Finding correctly reports the Semrush anchor-text cluster as 18 backlinks from 15 referring domains. The Objections table, addressing the same spam-link finding, says: *"What they got was 15 spammy PBN links"* — conflating the domain count (15) with the link count (18). Fix: "15 spammy PBN domains" or "18 spammy PBN links" — pick the number that matches the point being made.

## P3 — notes and questions

- **[B]** "Mostly UGC-style video + testimonial creative" — live Meta Ad Library review (confirmed ~74 results, matching the doc's "~70+") shows mostly produced, voiceover-driven product-comparison videos ("The difference between a vinyl sticker and a Stickmadly 3D emblem") plus at least one customer-review-quote ad. Whether this reads as "UGC-style" versus "produced branded video" is a judgment call worth a second look before the call, not a hard error.
- **[C]** "One earned, relevant backlink from navysealmuseum.org" — Semrush's top-backlinks table shows two indexed backlinks from that root domain (the Muster page and the Muster 5K page), both anchored "Stick Madly." Doesn't change the recommendation, but "one backlink" undercounts by one.
- **[B]** The 23-ad, "Miguel Angel Cubias Samper" (verified), Display/YouTube-format claim for the Google Ads Transparency Center is confirmed at the aggregate level (23 ads shown for stickmadly.com under that verified advertiser, with a mix of static and video-icon-tagged entries). The specific claim that individual creatives cover "America 250, NASA, Air Force" content was not independently confirmed at the per-ad level in this pass — worth a quick visual scan before the call if that specificity matters to the pitch.
- **[F]** Minor style inconsistency: media budget is written "$3–4K/mo" in the Google Ads finding prose vs. "$3K – $4K (incl. fees)" in the snapshot strip. Not wrong, just inconsistent formatting.

## Verified clean

- **A. Strategy fit** — no `icp-profile.md` exists for this prospect (expected; it's pre-onboarding). The doc's pitch angle ("consolidate before you expand") is internally consistent with the corrected Google Ads finding and doesn't propose channels/spend the account findings argue against, aside from the P1 contradiction noted above.
- **B. Factual accuracy (site facts)** — founded July 2013, ops in US/El Salvador/Honduras, and all eight named collections (US Army, Navy, Air Force, NASA, FC Barcelona, My Hero Academia, Jujutsu Kaisen, America 250) confirmed live against stickmadly.com and /pages/about-us.
- **B. Factual accuracy (SEO/Semrush)** — Semrush Rank 12.4M, 53 keywords, 0% branded traffic, both cited example keywords ("pencil back," "2d rocket"), 128 total backlinks, and the PBN-spam referring domains (ecomscout.com, shopiscout.com, pointblog.net) all confirmed against the user's Semrush Domain Overview PDF (`~/Downloads/Semrush-Domain_Overview_(Desktop)-stickmadly_com-31st_Aug_2026.pdf`). $0 all-time paid search (Search/Shopping) confirmed — and the doc's own hedge that this only covers Search/Shopping, not Display/YouTube, is accurate.
- **B. Factual accuracy (Meta Ad Library)** — ~74 results (matches "~70+"), multiple "Low impression count" labels present (matches the Flag), heavy recent activity (multiple ads started within the last 1-4 weeks of the prep date) confirmed live.
- **B. Factual accuracy (Google Ads Transparency Center)** — 23 ads for stickmadly.com under verified advertiser "Miguel Angel Cubias Samper" confirmed live (this was flagged in the manifest as needing fresh verification since it came from a pasted screenshot — now independently confirmed).
- **(b) Mario vs. Miguel Angel Cubias Samper** — correctly handled as an open question in Discovery Questions ("is that you, or someone else on the team?") rather than asserted as fact. A public LinkedIn profile for "Mario Cubías" tied to Stickmadly exists, supporting that Mario is a real contact; his role and his relationship (if any) to Miguel Angel Cubias Samper remain appropriately unresolved in the doc.
- **D. Brand voice / client rules** — not applicable (internal-only, correctly noted by the manifest).
- **G. Format compliance** — rendered the file in-browser: the `.page` div measures exactly 816×1056px (8.5in×11in at 96dpi) with `scrollHeight` equal to `.page` height — content fits the one-page print target with no overflow, despite the noted multiple rounds of font-size shrinking.
