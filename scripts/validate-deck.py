#!/usr/bin/env python3
"""
Validate a growth-roadmap (or foundation) deck HTML before publishing.

Catches the #1 recurring deck bug: an unbalanced <div> in a hand-authored slide
— e.g. a box opened with <div class="annotation"> but closed with </p>. HTML
doesn't error on that; it leaves the <div> open, so the browser re-nests the
nav bar inside the orphaned div and the prev/next arrows + counter + dots never
render. The page looks 99% fine, so it slips past an eyeball check.

Checks:
  1. Overall <div>/</div> balance.
  2. Per-slide balance — pinpoints the offending slide by its label/heading.
  3. (--render) Headless-Chrome render + nav-strip content check (best-effort;
     skipped if Chrome or PIL is unavailable).

Usage:
  python3 scripts/validate-deck.py path/to/growth-roadmap.html
  python3 scripts/validate-deck.py path/to/growth-roadmap.html --render

Exit 0 = pass, 1 = fail. Wire into every deck build/QA step so a broken nav
bar can't ship again.
"""
import re, sys, subprocess, shutil
from pathlib import Path


def slide_title(chunk):
    m = re.search(r'class="slide-label">([^<]+)<', chunk) or re.search(r"<h[12][^>]*>([^<]+)<", chunk)
    return m.group(1).strip()[:50] if m else "(untitled)"


def check_balance(html):
    # split on slide CONTAINERS only — class="slide" / "slide dark" / "slide cover" …,
    # NOT "slide-label" (slide followed by '-'). Decks use <div> (legacy hand-authored)
    # or <section> (generated from the design-system template).
    parts = re.split(r'(?=<(?:div|section) class="slide[ "])', html)
    issues = []
    for i, part in enumerate(parts):
        if i == 0:            # pre-slide head / preamble
            continue
        o, c = part.count("<div"), part.count("</div>")
        if o != c:
            issues.append((i, slide_title(part), o, c))
    return html.count("<div"), html.count("</div>"), issues


def check_nav_render(path):
    chrome = next((p for p in [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        shutil.which("google-chrome"), shutil.which("chromium"),
        shutil.which("chromium-browser")] if p and Path(p).exists()), None)
    if not chrome:
        return None, "Chrome not found — render check skipped"
    try:
        from PIL import Image
    except ImportError:
        return None, "PIL not installed — render check skipped"
    out = "/tmp/_deckval.png"
    try:
        subprocess.run([chrome, "--headless", "--disable-gpu", "--no-sandbox",
            "--hide-scrollbars", "--force-device-scale-factor=1",
            "--virtual-time-budget=3000", f"--screenshot={out}",
            "--window-size=1280,820", f"file://{Path(path).resolve()}"],
            capture_output=True, timeout=90)
    except Exception as e:                       # noqa: BLE001
        return None, f"render failed: {e}"
    if not Path(out).exists():
        return None, "render produced no image"
    im = Image.open(out).convert("L")
    strip = im.crop((0, im.height - 52, im.width, im.height))   # nav-bar band
    lo, hi = strip.getextrema()                  # an empty nav = near-uniform dark band
    spread = hi - lo
    return (spread > 60), f"nav-strip luminance spread {spread} (need >60 for visible controls)"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print("usage: validate-deck.py <deck.html> [--render]"); sys.exit(2)
    path = args[0]
    do_render = "--render" in sys.argv
    html = Path(path).read_text()
    o, c, issues = check_balance(html)
    fails, warns = [], []
    # The swallowed-nav bug ALWAYS shows as a TOTAL imbalance (the orphaned div never closes).
    # A per-slide blip with balanced totals is benign — almost always a document-level
    # wrapper (<div class="deck">…</div>) or nav block whose close lands on the last slide.
    if o != c:
        fails.append(f"<div> imbalance off {o-c:+d} — the swallowed-nav bug; a tag is closed "
                     f"with the wrong element (e.g. </p> where </div> was meant)")
        for idx, title, so, sc in issues:
            fails.append(f"  → look in slide {idx} \"{title}\" (off {so-sc:+d})")
    else:
        for idx, title, so, sc in issues:
            warns.append(f"slide {idx} \"{title}\" off {so-sc:+d} but totals balance — "
                         f"usually a wrapper/nav close on the last slide; only check that slide's layout")
    print(path)
    print(f"  <div> balance: {o} open / {c} close  " + ("✓" if o == c else f"✗ OFF BY {o-c:+d}"))
    if o == c and not warns:
        print("  ✓ all slides div-balanced")
    for w in warns:
        print(f"  ⚠ {w}")
    for fl in fails:
        print(f"  ✗ {fl}")
    ok = not fails
    if do_render:
        res, msg = check_nav_render(path)
        if res is None:
            print(f"  · nav render: {msg}")
        elif res:
            print(f"  ✓ nav bar renders — {msg}")
        else:
            print(f"  ✗ nav bar appears EMPTY — {msg}"); ok = False
    print(("PASS (warnings)" if warns else "PASS") if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
