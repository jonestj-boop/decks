#!/usr/bin/env python3
"""
Convert URL text spans inside accordion detail rows into clickable links
that open ceumatrix.com/<path> in a new tab.
"""

import re

DECK   = "/Users/deannaspallone/Documents/Claude Projects/embertribe-decks/decks/ceu-matrix-seo-foundation.html"
BASE   = "https://ceumatrix.com"

with open(DECK, "r", encoding="utf-8") as f:
    html = f.read()

# Pattern 1: two-column URL list spans (thin content, single inbound, missing meta, multiple H1)
# <span style="font-family:monospace;font-size:11px;color:rgba(44,62,80,0.75);
#   display:inline-block;width:48%;...">  /some/path  </span>
p1 = re.compile(
    r'<span (style="font-family:monospace;font-size:11px;color:rgba\(44,62,80,0\.75\);'
    r'display:inline-block;width:48%;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;")>'
    r'(/[^<]*?)'
    r'</span>'
)
def replace_p1(m):
    style, path = m.group(1), m.group(2).strip()
    return f'<a href="{BASE}{path}" target="_blank" {style}>{path}</a>'

count1 = len(p1.findall(html))
html   = p1.sub(replace_p1, html)
print(f"  Converted {count1} two-column URL spans to links")

# Pattern 2: broken links red URL spans
# <span style="font-family:monospace;font-size:11.5px;color:#c0392b;">/path</span>
p2 = re.compile(
    r'<span (style="font-family:monospace;font-size:11\.5px;color:#c0392b;")>'
    r'(/[^<]*?)'
    r'</span>'
)
def replace_p2(m):
    style, path = m.group(1), m.group(2).strip()
    return f'<a href="{BASE}{path}" target="_blank" {style}>{path}</a>'

count2 = len(p2.findall(html))
html   = p2.sub(replace_p2, html)
print(f"  Converted {count2} broken-link URL spans to links")

# Pattern 3: duplicate titles block spans
# <span style="font-family:monospace;font-size:11.5px;display:block;margin-top:4px;">/path</span>
p3 = re.compile(
    r'<span (style="font-family:monospace;font-size:11\.5px;display:block;margin-top:4px;")>'
    r'(/[^<]*?)'
    r'</span>'
)
def replace_p3(m):
    style, path = m.group(1), m.group(2).strip()
    return f'<a href="{BASE}{path}" target="_blank" {style}>{path}</a>'

count3 = len(p3.findall(html))
html   = p3.sub(replace_p3, html)
print(f"  Converted {count3} duplicate-title URL spans to links")

with open(DECK, "w", encoding="utf-8") as f:
    f.write(html)
print(f"\nTotal: {count1+count2+count3} URLs made clickable. Deck saved.")
