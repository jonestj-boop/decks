# DogiZone — Cost Per Qualified Lead (CPQL) Analysis

**Owner:** Paid Ads team
**Requested by:** Melissa
**Purpose:** Produce a defensible cost-per-qualified-lead figure for DogiZone's franchise program.
**Status:** Not started

---

## Why this matters

Andrew (DogiZone owner) is finalizing his Franchise Disclosure Document. He intends to write a **pre-opening lead requirement** into it: a new franchisee must generate a set number of qualified leads before they're approved to open. His current draft says **750 leads** against a **$20,000** pre-opening marketing budget.

Our preliminary read from the Ads API says that gate is not achievable at that budget. But the estimate depends on a lead-to-account conversion rate we inferred from figures quoted on a call, which is too soft to put in a legal document. **This analysis replaces the inference with measured data.**

Once it's in an FDD it's very hard to change, and every franchisee who misses the gate becomes a dispute. Getting the number right matters more than getting it fast.

---

## The core problem: "qualified lead" has three possible meanings

These differ by roughly **3x in cost**, so the definition has to be settled before the number means anything. Produce a CPQL for all three.

| # | Definition | Where it's measured |
|---|---|---|
| **L1** | Ad-reported conversion (phone call or form submission) | Google Ads |
| **L2** | Account created in Gingr | Gingr |
| **L3** | First reservation booked (an actual paying customer) | Gingr |

**Recommendation to validate, not assume:** L2 is probably the right gate metric. L1 is too easy to game and includes spam. L3 is the truest measure of a viable location but is too slow to gate an opening on.

---

## Date range

**April 21 to July 19, 2026** for everything. Use this exact window in both systems so the cohorts line up. If you extend it, extend it in both.

---

## Part A — Google Ads pull

**Account:** DogiZone, customer ID `5861051555`

### Which campaigns to include

We want **cold acquisition only**. A brand-new franchise location has no brand recognition, no review history, and no remarketing audience, so campaigns that harvest existing demand tell us nothing about what a new location will pay.

- **Include:** all campaigns with `TOFU` in the name (6 campaigns)
- **Exclude:** `ET | Search | BOFU | Branded | ...` — branded search, 786 conversions at $1 each. A new location has zero branded search volume.
- **Exclude:** `ET | PMax | MOFU_Engaged | Training | ...` — engaged-audience retargeting. A new location has no audience to retarget.

Getting these exclusions right is the single most important step. Including them drops blended CPL from ~$33 to ~$14 and makes the gate look affordable when it isn't.

### What to pull

Per campaign, and **segmented by conversion action name**:
- Cost
- Clicks
- Conversions (the counted metric, not all_conversions)
- All conversions

### GAQL

Config is at `~/google-ads.yaml` and loads via `GoogleAdsClient.load_from_storage()`.

```sql
SELECT
  campaign.name,
  segments.conversion_action_name,
  metrics.cost_micros,
  metrics.clicks,
  metrics.conversions,
  metrics.all_conversions
FROM campaign
WHERE segments.date BETWEEN "2026-04-21" AND "2026-07-19"
  AND campaign.name LIKE "%TOFU%"
```

**Gotcha:** `LAST_90_DAYS` is not a valid GAQL date literal (only 7, 14 and 30 exist). Use explicit `BETWEEN` dates or the query fails with `INVALID_VALUE_WITH_DURING_OPERATOR`.

**Gotcha:** always date-scope and `LIMIT` exploratory queries. An unbounded query will appear to hang; that's a bad query, not an access problem.

### Baseline to check your work against

If your pull is correct you should land close to:

| Metric | Expected |
|---|---|
| Cold (TOFU) spend | ~$22,010 |
| Counted conversions | ~672 |
| Blended cold CPL (L1) | ~$32.75 |
| Phone calls | 480 (71%) |
| Form submissions | 192 (29%) |

If you're materially off, check the campaign filter first.

### Critical: split calls from forms

Report these separately. **A pre-opening franchise has no phone line and no staff to answer it**, so the 71% of leads that arrive as phone calls are unavailable at launch. A pre-opening campaign runs on forms and waitlist signups only.

We need a **form-only CPL**, which will be higher than blended because it loses the cheaper call conversions. This is the number that actually applies to a franchise launch.

Group the actions as:
- **Calls:** `Calls from ads`, `Website Calls`
- **Forms:** `Reservation Form Completion`, `Reservation Link Email Submit`, `Dog Training Evaluation`, `Contact Form Submit`, `Dog Training Class Form`
- **Ignore:** `Local actions - *`, `Store visits`, `GA4 Phone Click` — these record volume but count zero, so they don't affect CPL. Do not include them.

---

## Part B — Gingr pull

**Check this first, before pulling anything else:** does Gingr capture a source, referrer, UTM, or "how did you hear about us" value on the account record?

- **If yes** — we can attribute properly and this analysis becomes rigorous. Pull that field and flag it to Melissa immediately, it changes the whole approach.
- **If no** — we're limited to date-cohort correlation. Still useful, but note the limitation in the output.

### Report needed

**One row per account**, accounts created April 21 to July 19, 2026:

| Field | Why |
|---|---|
| Account created date | Cohort matching against ad spend |
| Source / referral / how-heard | Attribution, if it exists |
| New vs existing customer flag | Isolating genuine new acquisition |
| First reservation date | L3 measurement and lag analysis |
| First reservation service type | Which service actually converts |
| First reservation value | Revenue per acquired account |

### Second report

**First reservations by date** over the same window. The June call referenced 193 accounts created against 108 first reservations in May, which would be roughly 56%. Confirm or correct that.

---

## Part C — The calculations

### 1. The leak rates

```
Rate A (ad → account)      = Gingr accounts created ÷ cold ad conversions
Rate B (account → booking) = first reservations ÷ accounts created
```

Our working assumption is **Rate A ≈ 34%**, inferred from call figures (roughly 400 calls + 167 forms against 193 accounts). **Confirm or replace it.** This single number drives everything downstream.

Do this weekly, not just as a total, so we can see whether the rate is stable or noisy.

### 2. The three CPQLs

```
CPQL (L1) = cold spend ÷ cold ad conversions
CPQL (L2) = cold spend ÷ Gingr accounts created
CPQL (L3) = cold spend ÷ first reservations
```

Produce each on both a **blended** and a **form-only** basis. Form-only L2 is the number that goes to Andrew.

### 3. Lead-to-revenue lag — the one nobody has computed

From the account-level export, calculate days from **account created** to **first reservation**: median, 25th and 75th percentile.

This is arguably the most valuable output of the whole exercise. If the median lag is five weeks, a franchisee's pre-opening campaign has to start over a month before opening day to have paying customers on day one. **That changes the FDD timeline, not just the budget**, and it's a genuine planning input Andrew currently doesn't have.

### 4. Diagnose the leak

Compare form submissions to accounts created, weekly. We're trying to separate three causes that were raised on the June call but never resolved:
- Spam submissions
- Existing customers coming through new-customer funnels
- Genuine drop-off on the long reservation form

If Gingr has a source field, this gets much easier.

---

## Deliverables

1. **CPQL table** — L1, L2, L3, each blended and form-only
2. **Rate A and Rate B**, with the weekly series behind them
3. **Lag distribution** — median, P25, P75, days from account to first reservation
4. **Budget model** — at the measured form-only L2 CPQL, what does 400, 500, 600 and 750 leads actually cost in media?
5. **A recommendation** on which of L1/L2/L3 should be the FDD gate metric, and why
6. **Confidence note** — how much of this is measured versus inferred, and what would firm it up

Send the raw exports along with the summary so the analysis can be re-run.

---

## Known caveats to state in the output

- **No shared identifier** between Google Ads and Gingr, so unless a source field exists this is cohort correlation, not true per-lead attribution. Present it as a reliable ratio, not a per-lead trace.
- **Calls are the weak spot.** 71% of cold conversions are phone calls and they're the hardest to trace into Gingr. Nimbata call tracking is mid-install and will improve this materially once live. Note where call attribution is assumption rather than measurement.
- **Corporate is a best case.** These figures come from a mature location with years of reviews, established Google history, and brand recognition in its metro. A new franchise in an unproven market should be modeled **worse**, not equal. Recommend a premium and say what it's based on.
- **Attribution windows differ** between Google Ads and Gingr, so weekly cohorts will be imperfect at the boundaries. Monthly rollups are more stable.

---

## Also worth checking while you're in the account

**`Reservation Form Completion` recorded 160 conversions but only 48 counted** over the 90-day window. That's the main reservation form, and roughly 70% of its volume isn't feeding the bidding algorithm.

Check whether it's set to "one per click" while comparable actions are set to "every." If Google is optimizing against an undercounted version of the most important form on the site, that's a live performance issue on the account today, independent of anything franchise-related. Flag what you find.
