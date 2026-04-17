#!/usr/bin/env python3
"""
Full SEO audit crawl for ceumatrix.com.
Collects all data needed to populate the accordion issues in one pass:
  1. Broken internal links (404s)
  2. Low text-to-HTML ratio pages (<15%)
  3. Pages with only 1 inbound internal link
  4. Missing meta descriptions
  5. Multiple H1 tags per page
  6. Duplicate title tags
  7. Schema markup presence / llms.txt
"""

import requests, urllib.parse, json, time, re
from collections import deque, defaultdict
from html.parser import HTMLParser

BASE_DOMAIN = "ceumatrix.com"
BASE_URL    = "https://ceumatrix.com"
MAX_PAGES   = 200
DELAY       = 0.12

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}
session = requests.Session()
session.headers.update(HEADERS)
session.max_redirects = 5

# ── Parsers ────────────────────────────────────────────────────────────────
class PageParser(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base = base_url
        self.links = []
        self.h1_count = 0
        self.in_h1 = False
        self.title = ""
        self.in_title = False
        self.meta_desc = None
        self.has_schema = False
        self.text_chunks = []
        self.in_script = False
        self.in_style = False
        self.in_body = False
        self.raw_html_len = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == 'script':
            self.in_script = True
            src = d.get('src', '') or ''
            typ = d.get('type', '') or ''
            if 'application/ld+json' in typ:
                self.has_schema = True
        elif tag == 'style':
            self.in_style = True
        elif tag == 'body':
            self.in_body = True
        elif tag == 'h1':
            self.h1_count += 1
            self.in_h1 = True
        elif tag == 'title':
            self.in_title = True
        elif tag == 'meta':
            name = (d.get('name') or '').lower()
            if name == 'description':
                self.meta_desc = d.get('content', '').strip()
        elif tag == 'a':
            href = d.get('href', '') or ''
            if href:
                resolved = urllib.parse.urljoin(self.base, href)
                self.links.append(resolved)
        elif tag == 'link':
            rel = (d.get('rel') or '').lower()
            if 'canonical' not in rel:
                pass

    def handle_endtag(self, tag):
        if tag == 'script': self.in_script = False
        elif tag == 'style': self.in_style = False
        elif tag == 'h1': self.in_h1 = False
        elif tag == 'title': self.in_title = False

    def handle_data(self, data):
        if self.in_script or self.in_style:
            return
        if self.in_title:
            self.title += data
        if self.in_body and not self.in_script and not self.in_style:
            stripped = data.strip()
            if stripped:
                self.text_chunks.append(stripped)

def parse_page(url, html):
    p = PageParser(url)
    p.raw_html_len = len(html)
    try:
        p.feed(html)
    except Exception:
        pass
    return p

def is_internal(url):
    parsed = urllib.parse.urlparse(url)
    return parsed.scheme in ('http', 'https') and BASE_DOMAIN in parsed.netloc

def normalise(url):
    p = urllib.parse.urlparse(url)
    # strip fragment, normalise scheme
    clean = urllib.parse.urlunparse(p._replace(fragment='', scheme='https'))
    # strip trailing slash unless it's the root
    if clean.endswith('/') and clean != BASE_URL + '/':
        clean = clean.rstrip('/')
    return clean

def skip_url(url):
    skip_patterns = [
        '/wp-admin', '/wp-login', '/feed/', '?replytocom',
        'cdn-cgi', 'mailto:', 'tel:', '.pdf', '.jpg', '.png',
        '.gif', '.zip', '.css', '.js', '?add-to-cart',
        'action=logout', '/cart/', '/checkout/', '/my-account/',
        '/wp-json/', '?v=', '#',
    ]
    return any(p in url for p in skip_patterns)

def check_status(url):
    try:
        r = session.head(url, timeout=8, allow_redirects=True)
        if r.status_code == 405:
            r = session.get(url, timeout=8, allow_redirects=True, stream=True)
            r.close()
        return r.status_code
    except Exception:
        return None

# ── Seed URLs from sitemaps + known patterns ───────────────────────────────
def get_seed_urls():
    seeds = set([BASE_URL + '/'])
    sitemap_urls_to_try = [
        '/sitemap.xml', '/sitemap_index.xml',
        '/page-sitemap.xml', '/post-sitemap.xml',
        '/product-sitemap.xml', '/product_cat-sitemap.xml',
        '/wp-sitemap.xml', '/wp-sitemap-posts-page-1.xml',
        '/wp-sitemap-posts-post-1.xml', '/wp-sitemap-taxonomies-category-1.xml',
    ]
    for path in sitemap_urls_to_try:
        try:
            r = session.get(BASE_URL + path, timeout=8)
            if r.status_code == 200 and ('xml' in r.headers.get('content-type','') or '<url' in r.text):
                found = re.findall(r'<loc>(https?://[^<]+)</loc>', r.text)
                for u in found:
                    if BASE_DOMAIN in u and not skip_url(u):
                        seeds.add(normalise(u))
                # Also find nested sitemaps
                nested = re.findall(r'<sitemap>.*?<loc>(https?://[^<]+)</loc>', r.text, re.DOTALL)
                for nurl in nested:
                    try:
                        nr = session.get(nurl, timeout=8)
                        nfound = re.findall(r'<loc>(https?://[^<]+)</loc>', nr.text)
                        for u in nfound:
                            if BASE_DOMAIN in u and not skip_url(u):
                                seeds.add(normalise(u))
                    except Exception:
                        pass
        except Exception:
            pass
    print(f"  Seeds from sitemaps: {len(seeds)} URLs")
    return seeds

# ── Main crawl ─────────────────────────────────────────────────────────────
print(f"🕷  Starting full audit crawl of {BASE_URL}\n")

print("Step 1: Collecting seed URLs from sitemaps...")
seeds = get_seed_urls()

queue = deque(seeds)
visited  = set(seeds)   # pages we've queued
crawled  = {}           # url → {title, meta_desc, h1_count, has_schema, text_ratio, outlinks}
link_graph = defaultdict(set)  # target_url → set(source_urls)
url_status = {}  # url → status code

print(f"\nStep 2: BFS crawl (max {MAX_PAGES} pages)...")
page_count = 0

while queue and page_count < MAX_PAGES:
    url = queue.popleft()
    page_count += 1

    try:
        r = session.get(url, timeout=12, allow_redirects=True)
        final_url = normalise(r.url)

        # Track redirect chains
        if final_url != url:
            url_status[url] = r.history[0].status_code if r.history else r.status_code

        content_type = r.headers.get('content-type', '')
        if 'text/html' not in content_type:
            url_status[url] = r.status_code
            continue

        url_status[url] = r.status_code

        p = parse_page(url, r.text)

        # Text-to-HTML ratio
        text_content = ' '.join(p.text_chunks)
        text_len  = len(text_content)
        html_len  = p.raw_html_len if p.raw_html_len > 0 else 1
        text_ratio = round(text_len / html_len * 100, 1)

        crawled[url] = {
            'title':      p.title.strip(),
            'meta_desc':  p.meta_desc,
            'h1_count':   p.h1_count,
            'has_schema': p.has_schema,
            'text_ratio': text_ratio,
            'text_len':   text_len,
            'html_len':   html_len,
        }

        # Process outlinks
        internal_links = []
        for link in p.links:
            if not link or skip_url(link): continue
            if is_internal(link):
                clean = normalise(link)
                internal_links.append(clean)
                link_graph[clean].add(url)  # build inbound link graph
                if clean not in visited and not skip_url(clean):
                    visited.add(clean)
                    queue.append(clean)

        crawled[url]['outlinks'] = list(set(internal_links))

        if page_count % 15 == 0:
            print(f"  [{page_count} crawled | {len(queue)} queued | {len(crawled)} pages with data]")

        time.sleep(DELAY)

    except requests.exceptions.Timeout:
        url_status[url] = 'timeout'
    except requests.exceptions.TooManyRedirects:
        url_status[url] = 'redirect_loop'
    except Exception as e:
        url_status[url] = f'error'

print(f"\n  Crawl complete: {page_count} pages visited, {len(crawled)} pages parsed\n")

# ── Step 3: Check outbound link status for broken links ───────────────────
print("Step 3: Checking for broken internal links...")

# Collect all unique internal URLs that were linked to
all_linked_urls = set()
for data in crawled.values():
    all_linked_urls.update(data.get('outlinks', []))

# Check status of any linked URL we haven't crawled
broken_links = []  # {source, target, status}
for target in sorted(all_linked_urls):
    if target not in url_status:
        status = check_status(target)
        url_status[target] = status
        time.sleep(0.05)
    status = url_status.get(target)
    if isinstance(status, int) and status >= 400:
        sources = [p for p, d in crawled.items() if target in d.get('outlinks', [])]
        for src in sources:
            broken_links.append({
                'source_page': src.replace(BASE_URL, '') or '/',
                'broken_url':  target.replace(BASE_URL, '') or '/',
                'status_code': status,
            })

broken_links.sort(key=lambda x: (x['broken_url'], x['source_page']))
print(f"  Found {len(broken_links)} broken link instances ({len(set(b['broken_url'] for b in broken_links))} unique broken URLs)")

# ── Step 4: Compile all audit findings ───────────────────────────────────
print("\nStep 4: Compiling audit findings...")

# 1. Low text-to-HTML (<15%)
thin_pages = [
    {'url': u.replace(BASE_URL,'') or '/', 'ratio': d['text_ratio'],
     'title': d['title'][:60] if d['title'] else '(no title)'}
    for u, d in crawled.items()
    if d['text_ratio'] < 15
]
thin_pages.sort(key=lambda x: x['ratio'])

# 2. Pages with only 1 inbound internal link
inbound_counts = {u: len(link_graph.get(u, set())) for u in crawled}
single_link_pages = [
    {'url': u.replace(BASE_URL,'') or '/', 'inbound': cnt,
     'title': crawled[u]['title'][:60] if crawled[u]['title'] else '(no title)'}
    for u, cnt in inbound_counts.items()
    if cnt == 1
]
single_link_pages.sort(key=lambda x: x['url'])

# 3. Missing meta descriptions
no_meta_pages = [
    {'url': u.replace(BASE_URL,'') or '/', 'title': d['title'][:60] if d['title'] else '(no title)'}
    for u, d in crawled.items()
    if not d['meta_desc'] or d['meta_desc'] == ''
]
no_meta_pages.sort(key=lambda x: x['url'])

# 4. Multiple H1s
multi_h1_pages = [
    {'url': u.replace(BASE_URL,'') or '/', 'h1_count': d['h1_count'],
     'title': d['title'][:60] if d['title'] else '(no title)'}
    for u, d in crawled.items()
    if d['h1_count'] > 1
]
multi_h1_pages.sort(key=lambda x: (-x['h1_count'], x['url']))

# 5. Duplicate title tags
from collections import Counter
title_map = defaultdict(list)
for u, d in crawled.items():
    t = d['title'].strip()
    if t:
        title_map[t].append(u.replace(BASE_URL,'') or '/')
dup_titles = [
    {'title': t, 'urls': urls}
    for t, urls in title_map.items()
    if len(urls) > 1
]
dup_titles.sort(key=lambda x: x['title'])

# 6. Schema markup check + llms.txt
has_schema_pages = [u for u, d in crawled.items() if d['has_schema']]
try:
    llms_r = session.get(BASE_URL + '/llms.txt', timeout=5)
    has_llms = llms_r.status_code == 200
except Exception:
    has_llms = False

# ── Step 5: Save everything ────────────────────────────────────────────────
output = {
    'crawl_summary': {
        'pages_crawled': page_count,
        'pages_with_data': len(crawled),
    },
    'broken_links': broken_links,
    'thin_content': thin_pages,
    'single_inbound_link': single_link_pages,
    'missing_meta': no_meta_pages,
    'multiple_h1': multi_h1_pages,
    'duplicate_titles': dup_titles,
    'schema_status': {
        'pages_with_schema': len(has_schema_pages),
        'has_llms_txt': has_llms,
        'schema_pages': [u.replace(BASE_URL,'') for u in has_schema_pages[:10]],
    },
}

out_path = "/Users/deannaspallone/Documents/Claude Projects/embertribe-decks/ceu-matrix-full-audit.json"
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)

print(f"\n{'='*60}")
print(f"AUDIT RESULTS")
print(f"{'='*60}")
print(f"Pages crawled:          {page_count}")
print(f"Broken link instances:  {len(broken_links)}")
print(f"Thin content (<15%):    {len(thin_pages)}")
print(f"Single inbound link:    {len(single_link_pages)}")
print(f"Missing meta desc:      {len(no_meta_pages)}")
print(f"Multiple H1 tags:       {len(multi_h1_pages)}")
print(f"Duplicate title pairs:  {len(dup_titles)}")
print(f"Pages with schema:      {len(has_schema_pages)}")
print(f"llms.txt exists:        {has_llms}")
print(f"\nSaved to: {out_path}")
