# SEO Foundation Data Skill

Pull and verify client baseline data before building or updating an SEO Foundation deck.
Full skill lives in the EmberTribe repo — this is the deck-side reference.

**Scripts location:** `EmberTribe/scripts/ga4-baseline.py` and `gsc-baseline.py`
**Full instructions:** `EmberTribe/.claude/skills/seo-foundation-data/SKILL.md`

---

## Quick Reference

### Pull GA4 organic sessions (6 months)
```bash
# Run from EmberTribe/ directory
python3 scripts/ga4-baseline.py \
  --key-file embertribe-content-tools-e6776250739e.json \
  --property {ga4_property_id} \
  --months 6
```

### Pull GSC metrics (90 days)
```bash
python3 scripts/gsc-baseline.py \
  --key-file embertribe-content-tools-e6776250739e.json \
  --site "{gsc_site_url}" \
  --brand "{brand}" --brand "{brand-variant}" \
  --days 90
```

---

## Known Bugs — Fixed in These Scripts

| Bug | Symptom | Fix |
|-----|---------|-----|
| GA4 filter wrong field name | Returns total sessions (all channels), ~3–4x too high | Use `sessionDefaultChannelGrouping` (with 'ing') not `sessionDefaultChannelGroup` |
| GSC branded text-match | Over- or under-counts branded clicks vs UI | Always verify branded % in GSC UI before using in deck |

---

## Verify Before Putting in the Deck

| Metric | Where to verify |
|--------|----------------|
| Monthly organic sessions | GA4 → Traffic Acquisition → filter Organic Search → Monthly view |
| Monthly impressions | GSC → Performance → set date range → Total impressions |
| Branded % | GSC → Performance → filter Branded queries → clicks ÷ total |
| Top query clicks | GSC → Queries tab → match top 5 |
| Ranking keywords | GSC → Queries tab → row count shown at bottom |

**Rule:** If script output and UI differ by more than 2% (sessions/impressions)
or 5 points (branded %), use the UI number.

---

## Deck Sections That Use This Data

| Deck slide | Data source |
|-----------|-------------|
| Cover stat cards | GA4 most recent month organic sessions |
| Baseline stat cards | GA4 sessions, GSC impressions + branded % |
| 6-month area chart | GA4 monthly sessions × 6 |
| Donut chart | GSC branded % (UI-verified) |
| Click legend | GSC monthly branded + non-branded avg |
| Top queries table | GSC top queries (monthly avg = total ÷ 3) |
| Traffic trajectory | GA4 baseline + directional projections |

---

## Projection Targets (conservative model, 4-month Foundation)

| Milestone | Multiplier from baseline |
|-----------|------------------------|
| Month 3 | ×1.07–1.15 |
| Month 6 | ×1.25–1.40 |
| Month 12 | ×1.60–1.80 |

Chart max = 120% of M12 target. Scale must be 0-based (no truncated y-axis).
