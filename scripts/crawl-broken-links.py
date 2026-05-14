#!/usr/bin/env python3
"""
Crawl ceumatrix.com to find all broken internal links.
Output: JSON list of {source_page, broken_url, status_code}
"""

import requests
import urllib.parse
import json
import time
from html.parser import HTMLParser

BASE_DOMAIN = "ceumatrix.com"
BASE_URL = "https://ceumatrix.com"
SITEMAP_URL = "https://ceumatrix.com/sitemap.xml"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; EmberTribe-SEOAudit/1.0)",
    "Accept": "text/html,application/xhtml+xml",
}

session = requests.Session()
session.headers.update(HEADERS)

# ── Step 1: collect all URLs from sitemap ──────────────────────────────────

def get_sitemap_urls():
    urls = []
    try:
        r = session.get(SITEMAP_URL, timeout=10)
        if r.status_code == 200:
            import re
            found = re.findall(r'<loc>(https?://[^<]+)</loc>', r.text)
            urls = [u for u in found if BASE_DOMAIN in u]
            print(f"  Sitemap: {len(urls)} URLs found")
    except Exception as e:
        print(f"  Sitemap error: {e}")
    return urls

# ── Step 2: parse links from a page ───────────────────────────────────────

class LinkParser(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, val in attrs:
                if attr == 'href' and val:
                    resolved = urllib.parse.urljoin(self.base_url, val)
                    self.links.append(resolved)

def get_internal_links(page_url, html):
    parser = LinkParser(page_url)
    parser.feed(html)
    links = []
    for link in parser.links:
        parsed = urllib.parse.urlparse(link)
        if parsed.scheme in ('http', 'https') and BASE_DOMAIN in parsed.netloc:
            # Strip fragment
            clean = urllib.parse.urlunparse(parsed._replace(fragment=''))
            links.append(clean)
    return list(set(links))

# ── Step 3: check if a URL is broken ─────────────────────────────────────

def check_url(url):
    try:
        r = session.head(url, timeout=8, allow_redirects=True)
        if r.status_code == 405:  # HEAD not allowed
            r = session.get(url, timeout=8, allow_redirects=True)
        return r.status_code
    except Exception as e:
        return f"error: {e}"

# ── Main crawl ────────────────────────────────────────────────────────────

print("Step 1: Getting sitemap URLs...")
sitemap_urls = get_sitemap_urls()

# Also add homepage if not in sitemap
if BASE_URL + "/" not in sitemap_urls and BASE_URL not in sitemap_urls:
    sitemap_urls.insert(0, BASE_URL + "/")

# Limit to 80 pages for speed (covers most of the site)
pages_to_crawl = sitemap_urls[:80]
print(f"  Crawling {len(pages_to_crawl)} pages\n")

broken_links = []
checked_urls = {}  # url → status_code cache
all_page_links = {}

print("Step 2: Crawling pages and collecting internal links...")
for i, page_url in enumerate(pages_to_crawl):
    try:
        r = session.get(page_url, timeout=10)
        if 'text/html' not in r.headers.get('content-type', ''):
            continue
        links = get_internal_links(page_url, r.text)
        all_page_links[page_url] = links
        if (i + 1) % 10 == 0:
            print(f"  [{i+1}/{len(pages_to_crawl)}] crawled...")
        time.sleep(0.15)  # polite delay
    except Exception as e:
        print(f"  Error crawling {page_url}: {e}")

# Collect unique internal URLs to check
all_linked_urls = set()
for links in all_page_links.values():
    all_linked_urls.update(links)
print(f"\nStep 3: Checking {len(all_linked_urls)} unique internal URLs...")

for j, url in enumerate(sorted(all_linked_urls)):
    if url not in checked_urls:
        status = check_url(url)
        checked_urls[url] = status
        time.sleep(0.1)
    if (j + 1) % 50 == 0:
        print(f"  [{j+1}/{len(all_linked_urls)}] checked...")

# Find broken links with their source pages
print("\nStep 4: Mapping broken links to source pages...")
for page_url, links in all_page_links.items():
    for link in links:
        status = checked_urls.get(link)
        if isinstance(status, int) and status >= 400:
            broken_links.append({
                "source_page": page_url,
                "broken_url": link,
                "status_code": status
            })

# Deduplicate (same broken URL found on multiple pages)
seen = set()
unique_broken = []
for item in broken_links:
    key = (item["source_page"], item["broken_url"])
    if key not in seen:
        seen.add(key)
        unique_broken.append(item)

unique_broken.sort(key=lambda x: x["broken_url"])

print(f"\n{'='*60}")
print(f"RESULT: {len(unique_broken)} broken internal link instances")
print(f"{'='*60}")

# Save results
output_path = "/Users/deannaspallone/Documents/Claude Projects/embertribe-decks/ceu-matrix-broken-links.json"
with open(output_path, "w") as f:
    json.dump(unique_broken, f, indent=2)
print(f"\nSaved to {output_path}")

# Print summary
for item in unique_broken[:20]:
    src = item["source_page"].replace(BASE_URL, "")
    lnk = item["broken_url"].replace(BASE_URL, "")
    print(f"  [{item['status_code']}] {src} → {lnk}")
if len(unique_broken) > 20:
    print(f"  ... and {len(unique_broken) - 20} more (see JSON file)")
