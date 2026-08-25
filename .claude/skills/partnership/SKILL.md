---
name: partnership
description: Generate a partner's active-account tier dashboard — qualifying accounts against the $1,500 MRR floor, current tier, and path to the next tier. Use when the user says "setup /partnership for {name}", "build a partner dashboard for {name}", or asks to see where a partner stands on tier.
---

# Partnership Dashboard Skill

Generates the same kind of dashboard built for Shevy (`decks/shevy/dashboard.html`) for any partner: their accounts, which ones qualify for tier under the $1,500 MRR floor, their current tier, and what it takes to reach the next one.

---

## When to Use

- User says "setup /partnership for {name}"
- User says "build a partner dashboard for {name}"
- User provides a partner's client list + MRR and wants to see their tier status
- User asks "where does {partner} stand on tier" or "is {partner} close to the next tier"

---

## Inputs

### Required
- **Partner name**
- **Their accounts**: for each, the account/client name and current MRR

**If the user only gives a name** ("setup /partnership for Shevy"), ask for the account list before building anything — there's no CRM integration to pull it from (see `reference_embertribe_ghl_api` memory: the GHL lookup path is unverified/paused). Don't invent accounts or numbers.

---

## Process

### Phase 1: Collect accounts

Get account name + MRR for every account in the partner's book.

### Phase 2: Apply the tier math

This is the same logic live on `decks/partner-program.html` — don't drift from it. Re-read that file if unsure; it's the source of truth, this skill is not.

**The floor:** an account only counts toward the tier total if its MRR is **≥ $1,500**. Sub-floor accounts still appear in the account breakdown table but are marked "Below floor" and excluded from the qualifying count.

**Tier bands (Model A — Partner Agency), by qualifying account count:**

| Tier | Qualifying accounts | Discount |
|---|---|---|
| *(none)* | 0 | Not yet in a tier |
| Affiliate | 1–3 | 10% |
| Silver | 4–7 | 15% |
| Gold | 8–14 | 20% |
| Platinum | 15+ | 25% |

**Compute:**
1. `qualifying_accounts` = count of accounts with MRR ≥ $1,500
2. `total_mrr` = sum of all account MRR (including sub-floor)
3. `qualifying_mrr` = sum of MRR for qualifying accounts only
4. `current_tier` = the band `qualifying_accounts` falls into
5. `next_tier` = the band above current (skip if already Platinum — see Edge Cases)
6. `ring_percent` = `qualifying_accounts / next_tier's lower bound * 100`, capped at 100
7. `gap_to_next` = `next_tier's lower bound − qualifying_accounts`
8. `tier_without_floor` = what tier the *raw* account count (no floor applied) would land in — only surface this if it differs from `current_tier`. This is the gap the floor exists to close: a partner shouldn't unlock a bigger discount off a stack of tiny accounts and have it apply to one large one (see the $1,500-floor rationale on `partner-program.html`).

**Bars section:** one row per tier band from Affiliate through the tier one above current (or through Gold if current is Silver+, matching the 3-row pattern in the template — don't show a bar for a tier already several steps past reach, it's not useful). Each row's label includes that tier's discount (e.g. "Affiliate (1–3) · 10%"). Tiers fully reached: full bar, "Reached". Current-and-above tiers: dim-fill bar at `qualifying_accounts / that tier's lower bound`, label "`{{qualifying}} / {{lower bound}}`".

### Phase 3: Fill the template

Copy `.claude/skills/partnership/template.html` — every instruction for filling it (including the ring/bars math shorthand) is inline as HTML/CSS comments in the file itself. Read those before filling.

**Where to save:** `decks/{partner-slug}/dashboard.html` — public, no password gate. Slug format: lowercase, hyphens, no special characters.

### Phase 4: Save & report

Report the file path and the live URL: `https://decks.embertribe.com/{partner-slug}/dashboard.html`.

---

## Edge Cases

- **0 qualifying accounts:** partner isn't in a tier yet. Masthead/summary should say so plainly ("Not yet in a tier — 1 qualifying account unlocks Affiliate") rather than showing a 0/1 ring that reads like a bug.
- **Already Platinum (15+ qualifying accounts):** there's no "next tier" to ring toward. Swap the ring for a flat "Platinum — max tier reached" state (no fraction, no percent-fill math) and drop the "Path to next tier" section entirely, or repurpose it to note what it'd take to justify a bespoke arrangement (per partner-program.html: "volume above 15 accounts/referrals... is a custom conversation with your EmberTribe partnerships contact, not an auto-applied rate").
- **The floor doesn't change the tier outcome:** if `current_tier` already equals what the raw count would produce, drop the "Why it's X, not Y" callout — it has nothing to explain and reads as filler.
- **Tier data goes stale:** if the user corrects an account's MRR later (like Ayoub's $2,300 → $3,800 correction), recompute *everything downstream* — total/qualifying MRR and the account table. Don't patch just the one number; check the whole page for consistency before reporting done.

---

## Example Usage

```
User: setup /partnership for Marisol Vega. Accounts: Northwind $2,100,
      Delacroix $900, Fennwick Group $4,200.

Skill:
1. 3 accounts, MRR $2,100 / $900 / $4,200. Floor is $1,500 → Delacroix
   doesn't qualify. Qualifying = 2 (Northwind, Fennwick Group).
2. 2 qualifying accounts → Affiliate tier (1–3 band), 10% off.
   Next tier: Silver at 4. Gap: 2 more qualifying accounts.
3. Raw count (3) would also land in Affiliate (1–3) — floor doesn't
   change the outcome here, so the "why" callout gets dropped.
4. Saves to decks/marisol-vega/dashboard.html.
5. Reports the file path and the live URL:
   decks.embertribe.com/marisol-vega/dashboard.html
```
