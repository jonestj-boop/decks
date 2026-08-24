#!/usr/bin/env python3
"""
Scan client-facing deliverables for AI-writing tells before they ship.

Deterministic layer of the humanization pass (see
.claude/skills/qa-review/references/humanize.md for the full checklist and the judgment
layer). Works on .html (visible text), .md/.txt, and .json (string values — e.g.
readme-sections.json, content-plan.json).

  FAIL: em dashes in client prose (house rule) · banned phrases from
        .claude/skills/seo-growth-roadmap/banned-title-phrases.yaml + the client's own
        banned-title-phrases.yaml · chatbot leakage ("I hope this helps", "as an AI")
  WARN: high-signal AI vocabulary and constructions, with counts and context ·
        rule-of-three density · "not X but Y" density

Warnings are triage input for qa-review, not auto-blockers. Exit 1 only on FAILs.

Usage:
  python3 scripts/validate-prose-tells.py <file> [<file> ...] [--client slug] [--allow-emdash]
"""
import argparse
import json
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# This script is mirrored into sibling repos (e.g. embertribe-decks). The banned-phrase
# lists live ONLY in the EmberTribe repo (single source, no drift) — when run from a
# mirror, fall back to a sibling EmberTribe checkout; degrade gracefully if absent.
_ROOTS = [ROOT] + ([ROOT.parent / "EmberTribe"] if ROOT.name != "EmberTribe" else [])
SKILL_BANNED = next((r / ".claude/skills/seo-growth-roadmap/banned-title-phrases.yaml"
                     for r in _ROOTS if (r / ".claude/skills/seo-growth-roadmap/banned-title-phrases.yaml").exists()),
                    ROOT / ".claude/skills/seo-growth-roadmap/banned-title-phrases.yaml")

CHATBOT = ["i hope this helps", "let me know if", "as an ai", "great question", "you're absolutely right",
           "certainly!", "happy to help"]

# High-signal tells only — every hit is worth a human look; noisy generics are left to qa-review judgment.
VOCAB = ["delve", "tapestry", "testament to", "ever-evolving", "fast-paced", "game-chang",
         "revolutioniz", "cutting-edge", "seamless", "holistic", "unleash", "supercharge",
         "elevate your", "in today's", "in the world of", "when it comes to", "look no further",
         "we've got you covered", "let's dive", "dive into", "deep dive", "it's important to note",
         "it's worth noting", "at its core", "at the end of the day", "the bottom line",
         "the future looks bright", "navigating the", "unlocking the", "a treasure trove",
         "whether you're", "look, ", "honestly?"]

NOT_X_BUT_Y = re.compile(r"\b(isn'?t just|not just|not only|it'?s not about|more than just)\b", re.I)
TRIPLET = re.compile(r"\b\w+, \w+, and \w+\b")


class TextExtract(HTMLParser):
    SKIP = {"script", "style"}

    def __init__(self):
        super().__init__()
        self.parts, self._skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in self.SKIP and self._skip:
            self._skip -= 1

    def handle_data(self, d):
        if not self._skip and d.strip():
            self.parts.append(d.strip())


def extract_text(path):
    raw = path.read_text(errors="replace")
    if path.suffix == ".html":
        p = TextExtract()
        p.feed(raw)
        return "\n".join(p.parts)
    if path.suffix == ".json":
        out = []

        def walk(v):
            if isinstance(v, str):
                out.append(v)
            elif isinstance(v, list):
                for x in v:
                    walk(x)
            elif isinstance(v, dict):
                for x in v.values():
                    walk(x)
        try:
            walk(json.loads(raw))
        except json.JSONDecodeError:
            return raw
        return "\n".join(out)
    return raw


def load_banned(client):
    phrases = []
    client_lists = [r / "clients" / client / "banned-title-phrases.yaml" for r in _ROOTS] if client else []
    for p in [SKILL_BANNED] + client_lists:
        if not p.exists():
            continue
        text = p.read_text()
        try:
            import yaml
            phrases += [str(x).lower() for x in (yaml.safe_load(text) or {}).get("phrases", [])]
        except ImportError:
            in_list = False
            for line in text.splitlines():
                if re.match(r"^phrases:\s*$", line):
                    in_list = True
                    continue
                m = re.match(r"^\s*-\s*(.+?)\s*$", line)
                if in_list and m:
                    phrases.append(m.group(1).strip("'\"").lower())
                elif in_list and line and not line.startswith((" ", "#", "-")):
                    in_list = False
    return phrases


def context(text_low, text, needle, limit=2):
    outs = []
    for m in list(re.finditer(re.escape(needle), text_low))[:limit]:
        s, e = max(0, m.start() - 30), min(len(text), m.end() + 30)
        outs.append("…" + re.sub(r"\s+", " ", text[s:e]).strip() + "…")
    return outs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--client", help="slug, to load the per-client banned list")
    ap.add_argument("--allow-emdash", action="store_true", help="downgrade em dashes to a warning")
    args = ap.parse_args()

    banned = load_banned(args.client)
    any_fail = False

    for f in args.files:
        path = Path(f)
        if not path.exists():
            print(f"{f}: not found")
            any_fail = True
            continue
        text = extract_text(path)
        low = text.lower()
        words = max(len(low.split()), 1)
        fails, warns = [], []

        # House rule: no em dashes inside client-facing prose sentences. The
        # embertribe-design system DOES use an em dash as the bullet glyph, so a
        # dash that opens a line (only dashes/spaces before it) is allowed.
        prose_em, em_ctx = 0, []
        for line in text.splitlines():
            s = line.strip()
            for i, ch in enumerate(s):
                if ch == "—" and s[:i].strip("— ") != "":
                    prose_em += 1
                    if len(em_ctx) < 2:
                        em_ctx.append("…" + re.sub(r"\s+", " ", s[max(0, i - 30):i + 30]).strip() + "…")
        if prose_em:
            msg = (f"{prose_em} em dash(es) inside prose — house rule: none in client-facing "
                   f"copy (leading bullet glyphs are fine)  {' | '.join(em_ctx)}")
            (warns if args.allow_emdash else fails).append(msg)

        for p in banned:
            if p in low:
                fails.append(f'banned phrase "{p}"  {" | ".join(context(low, text, p))}')
        for p in CHATBOT:
            if p in low:
                fails.append(f'chatbot leakage "{p}"  {" | ".join(context(low, text, p))}')

        vhits = Counter()
        for v in VOCAB:
            n = low.count(v)
            if n:
                vhits[v] = n
        for v, n in vhits.most_common():
            warns.append(f'AI-vocab "{v}" ×{n}  {" | ".join(context(low, text, v, 1))}')

        nxy = len(NOT_X_BUT_Y.findall(text))
        if nxy > 2:
            warns.append(f'"not X but Y" construction ×{nxy} — more than ~2 per document reads as generated')
        trip = len(TRIPLET.findall(text))
        if trip / words * 1000 > 3 and trip > 3:
            warns.append(f"rule-of-three lists ×{trip} in {words} words — vary list lengths")

        print(path.name)
        for w in warns:
            print(f"  ⚠ {w}")
        for x in fails:
            print(f"  ✗ {x}")
        if not fails and not warns:
            print("  clean")
        if fails:
            any_fail = True

    print("FAIL" if any_fail else "PASS")
    sys.exit(1 if any_fail else 0)


if __name__ == "__main__":
    main()
