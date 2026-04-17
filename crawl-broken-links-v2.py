#!/usr/bin/env python3
"""
BFS recursive crawler for ceumatrix.com.
Starts from homepage, follows all internal links, checks for 404s.
"""
import requests, urllib.parse, json, time, re
from collections import deque
from html.parser import HTMLParser

BASE_DOMAIN = "ceumatrix.com"
BASE_URL    = "https://ceumatrix.com"
MAX_PAGES   = 120
DELAY       = 0.15

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

session = requests.Session()
session.headers.update(HEADERS)

# ── Link parser ────────────────────────────────────────────────────────────
class LinkParser(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.links = []
    def handle_starttag(self, tag, attrs):
        attr_map = dict(attrs)
        href = None
        if tag == 'a':     href = attr_map.get('href')
        if href:
            resolved = urllib.parse.urljoin(self.base_url, href)
            self.links.append(resolved)

def extract_links(page_url, html):
    parser = LinkParser(page_url)
    try:
        parser.feed(html)
    except Exception:
        pass
    out = []
    for link in parser.links:
        if not link: continue
        parsed = urllib.parse.urlparse(link)
        if parsed.scheme not in ('http', 'https'): continue
        if BASE_DOMAIN not in parsed.netloc: continue
        # drop anchors, query strings with sessionid, wp-admin, feed, etc.
        clean = urllib.parse.urlunparse(parsed._replace(fragment=''))
        if '/wp-admin' in clean or '/wp-login' in clean: continue
        if '/feed/' in clean or '?replytocom' in clean: continue
        if 'cdn-cgi' in clean: continue
        out.append(clean)
    return list(set(out))

# ── Status checker ─────────────────────────────────────────────────────────
def check_status(url):
    try:
        r = session.head(url, timeout=8, allow_redirects=True)
        if r.status_code == 405:
            r = session.get(url, timeout=8, allow_redirects=True, stream=True)
            r.close()
        return r.status_code
    except requests.exceptions.ConnectionError:
        return "conn_error"
    except requests.exceptions.Timeout:
        return "timeout"
    except Exception as e:
        return f"error"

# ── BFS crawl ──────────────────────────────────────────────────────────────
visited_pages  = set()   # pages we've fetched HTML from
checked_urls   = {}      # url → status code
link_sources   = {}      # broken_url → [source_pages]

queue = deque([BASE_URL + "/"])
visited_pages.add(BASE_URL + "/")

print(f"Starting BFS crawl of {BASE_URL} (max {MAX_PAGES} pages)...\n")

page_count = 0
while queue and page_count < MAX_PAGES:
    page_url = queue.popleft()
    page_count += 1

    try:
        r = session.get(page_url, timeout=12, allow_redirects=True)
        content_type = r.headers.get('content-type', '')
        if 'text/html' not in content_type:
            continue

        links = extract_links(page_url, r.text)

        # Queue unvisited internal pages for crawling
        for link in links:
            if link not in visited_pages:
                visited_pages.add(link)
                queue.append(link)

            # Check status of every linked URL
            if link not in checked_urls:
                status = check_status(link)
                checked_urls[link] = status
                time.sleep(0.05)

            # Record source → broken mapping
            status = checked_urls.get(link)
            if isinstance(status, int) and status >= 400:
                if link not in link_sources:
                    link_sources[link] = []
                if page_url not in link_sources[link]:
                    link_sources[link].append(page_url)

        if page_count % 10 == 0:
            broken_so_far = len(link_sources)
            print(f"  [{page_count} pages crawled | {len(queue)} in queue | {broken_so_far} broken URLs so far]")

        time.sleep(DELAY)

    except requests.exceptions.ConnectionError:
        print(f"  Connection error: {page_url}")
    except requests.exceptions.Timeout:
        print(f"  Timeout: {page_url}")
    except Exception as e:
        print(f"  Error on {page_url}: {e}")

print(f"\n{'='*60}")
print(f"Crawled {page_count} pages, checked {len(checked_urls)} unique URLs")
print(f"Broken links found: {len(link_sources)} unique broken URLs")
print(f"{'='*60}\n")

# Build output: flat list of {source_page, broken_url, status_code}
results = []
for broken_url, sources in sorted(link_sources.items()):
    status = checked_urls.get(broken_url, '?')
    for src in sources:
        results.append({
            "source_page": src.replace(BASE_URL, "") or "/",
            "broken_url":  broken_url.replace(BASE_URL, "") or "/",
            "status_code": status
        })

results.sort(key=lambda x: (x["broken_url"], x["source_page"]))

# Print all
for item in results:
    print(f"  [{item['status_code']}] {item['source_page']}  →  {item['broken_url']}")

# Save
out_path = "/Users/deannaspallone/Documents/Claude Projects/embertribe-decks/ceu-matrix-broken-links.json"
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved {len(results)} rows to {out_path}")
