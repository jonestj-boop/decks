#!/usr/bin/env python3
"""
Full SEO technical audit crawl for lendforall.ca.
Adapted from full-audit-crawl.py (ceumatrix). Collects:
  1. Broken internal links (404s)
  2. Low text-to-HTML ratio pages (<15%)
  3. Pages with only 1 inbound internal link
  4. Missing meta descriptions
  5. Multiple H1 tags per page
  6. Duplicate title tags
  7. Schema markup presence / llms.txt / robots.txt / sitemap coverage
  8. Canonical + noindex flags, title length issues, redirect chains
"""

import requests, urllib.parse, json, time, re
from collections import deque, defaultdict
from html.parser import HTMLParser

BASE_DOMAIN = "lendforall.ca"
BASE_URL    = "https://lendforall.ca"
MAX_PAGES   = 250
DELAY       = 0.12

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
    "Accept-Language": "en-CA,en;q=0.9",
}
session = requests.Session()
session.headers.update(HEADERS)
session.max_redirects = 5

class PageParser(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base = base_url
        self.links = []
        self.h1_count = 0
        self.title = ""
        self.in_title = False
        self.meta_desc = None
        self.meta_robots = None
        self.canonical = None
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
            if 'application/ld+json' in (d.get('type') or ''):
                self.has_schema = True
        elif tag == 'style':
            self.in_style = True
        elif tag == 'body':
            self.in_body = True
        elif tag == 'h1':
            self.h1_count += 1
        elif tag == 'title':
            self.in_title = True
        elif tag == 'meta':
            name = (d.get('name') or '').lower()
            if name == 'description':
                self.meta_desc = (d.get('content') or '').strip()
            elif name == 'robots':
                self.meta_robots = (d.get('content') or '').strip().lower()
        elif tag == 'a':
            href = d.get('href', '') or ''
            if href:
                self.links.append(urllib.parse.urljoin(self.base, href))
        elif tag == 'link':
            rel = (d.get('rel') or '').lower()
            if 'canonical' in rel:
                self.canonical = (d.get('href') or '').strip()

    def handle_endtag(self, tag):
        if tag == 'script': self.in_script = False
        elif tag == 'style': self.in_style = False
        elif tag == 'title': self.in_title = False

    def handle_data(self, data):
        if self.in_script or self.in_style:
            return
        if self.in_title:
            self.title += data
        if self.in_body:
            s = data.strip()
            if s:
                self.text_chunks.append(s)

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
    clean = urllib.parse.urlunparse(p._replace(fragment='', scheme='https'))
    if clean.endswith('/') and clean != BASE_URL + '/':
        clean = clean.rstrip('/')
    return clean

def skip_url(url):
    skip_patterns = [
        '/wp-admin', '/wp-login', '/feed/', '?replytocom',
        'cdn-cgi', 'mailto:', 'tel:', '.pdf', '.jpg', '.png',
        '.gif', '.zip', '.css', '.js', '?add-to-cart',
        'action=logout', '/cart/', '/checkout/', '/my-account/',
        '/wp-json/', '?v=', '#', '.webp', '.svg', '.mp4',
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

# ── robots.txt / llms.txt / redirect variants ─────────────────────────────
extras = {}
try:
    r = session.get(BASE_URL + '/robots.txt', timeout=8)
    extras['robots_txt'] = {'status': r.status_code, 'content': r.text[:2000] if r.status_code == 200 else None}
except Exception as e:
    extras['robots_txt'] = {'status': 'error'}
try:
    r = session.get(BASE_URL + '/llms.txt', timeout=8)
    extras['llms_txt'] = r.status_code == 200 and 'html' not in r.headers.get('content-type','')
except Exception:
    extras['llms_txt'] = False

redirect_checks = {}
for variant in ["http://lendforall.ca/", "http://www.lendforall.ca/", "https://www.lendforall.ca/"]:
    try:
        r = session.get(variant, timeout=10, allow_redirects=True)
        redirect_checks[variant] = {
            'final': r.url,
            'hops': len(r.history),
            'chain': [h.status_code for h in r.history],
        }
    except Exception:
        redirect_checks[variant] = {'final': 'error', 'hops': None, 'chain': []}
extras['redirect_variants'] = redirect_checks

# ── Seed URLs from sitemaps ────────────────────────────────────────────────
def get_seed_urls():
    seeds = set([BASE_URL + '/'])
    sitemap_info = {'found': [], 'url_count': 0}
    for path in ['/sitemap.xml', '/sitemap_index.xml', '/wp-sitemap.xml', '/page-sitemap.xml', '/post-sitemap.xml']:
        try:
            r = session.get(BASE_URL + path, timeout=8)
            if r.status_code == 200 and ('xml' in r.headers.get('content-type','') or '<url' in r.text or '<sitemap' in r.text):
                sitemap_info['found'].append(path)
                found = re.findall(r'<loc>(https?://[^<]+)</loc>', r.text)
                nested = [u for u in found if 'sitemap' in u and u.endswith('.xml')]
                page_urls = [u for u in found if u not in nested]
                for u in page_urls:
                    if BASE_DOMAIN in u and not skip_url(u):
                        seeds.add(normalise(u))
                for nurl in nested:
                    try:
                        nr = session.get(nurl, timeout=8)
                        for u in re.findall(r'<loc>(https?://[^<]+)</loc>', nr.text):
                            if BASE_DOMAIN in u and not skip_url(u):
                                seeds.add(normalise(u))
                    except Exception:
                        pass
                break
        except Exception:
            pass
    sitemap_info['url_count'] = len(seeds)
    extras['sitemap'] = sitemap_info
    print(f"  Sitemaps found: {sitemap_info['found']} -> {len(seeds)} seed URLs")
    return seeds

print(f"Starting full audit crawl of {BASE_URL}\n")
print("Step 1: Collecting seed URLs from sitemaps...")
seeds = get_seed_urls()
sitemap_urls = set(seeds)

queue = deque(sorted(seeds))
visited  = set(seeds)
crawled  = {}
link_graph = defaultdict(set)
url_status = {}

print(f"\nStep 2: BFS crawl (max {MAX_PAGES} pages)...")
page_count = 0

while queue and page_count < MAX_PAGES:
    url = queue.popleft()
    page_count += 1
    try:
        r = session.get(url, timeout=12, allow_redirects=True)
        final_url = normalise(r.url)
        if final_url != url:
            url_status[url] = r.history[0].status_code if r.history else r.status_code
        content_type = r.headers.get('content-type', '')
        if 'text/html' not in content_type:
            url_status[url] = r.status_code
            continue
        url_status[url] = r.status_code
        p = parse_page(url, r.text)
        text_content = ' '.join(p.text_chunks)
        text_len = len(text_content)
        html_len = p.raw_html_len or 1
        crawled[url] = {
            'title': p.title.strip(),
            'meta_desc': p.meta_desc,
            'meta_robots': p.meta_robots,
            'canonical': p.canonical,
            'h1_count': p.h1_count,
            'has_schema': p.has_schema,
            'text_ratio': round(text_len / html_len * 100, 1),
            'text_len': text_len,
            'html_len': html_len,
            'redirect_hops': len(r.history),
        }
        internal_links = []
        for link in p.links:
            if not link or skip_url(link): continue
            if is_internal(link):
                clean = normalise(link)
                internal_links.append(clean)
                link_graph[clean].add(url)
                if clean not in visited and not skip_url(clean):
                    visited.add(clean)
                    queue.append(clean)
        crawled[url]['outlinks'] = list(set(internal_links))
        if page_count % 25 == 0:
            print(f"  [{page_count} crawled | {len(queue)} queued]")
        time.sleep(DELAY)
    except requests.exceptions.Timeout:
        url_status[url] = 'timeout'
    except requests.exceptions.TooManyRedirects:
        url_status[url] = 'redirect_loop'
    except Exception:
        url_status[url] = 'error'

print(f"\n  Crawl complete: {page_count} visited, {len(crawled)} parsed\n")

print("Step 3: Checking for broken internal links...")
all_linked_urls = set()
for data in crawled.values():
    all_linked_urls.update(data.get('outlinks', []))
broken_links = []
for target in sorted(all_linked_urls):
    if target not in url_status:
        url_status[target] = check_status(target)
        time.sleep(0.05)
    status = url_status.get(target)
    if isinstance(status, int) and status >= 400:
        for src, d in crawled.items():
            if target in d.get('outlinks', []):
                broken_links.append({
                    'source_page': src.replace(BASE_URL, '') or '/',
                    'broken_url': target.replace(BASE_URL, '') or '/',
                    'status_code': status,
                })
broken_links.sort(key=lambda x: (x['broken_url'], x['source_page']))
print(f"  {len(broken_links)} broken link instances ({len(set(b['broken_url'] for b in broken_links))} unique URLs)")

print("\nStep 4: Compiling findings...")
def rel(u): return u.replace(BASE_URL, '') or '/'

thin_pages = sorted([
    {'url': rel(u), 'ratio': d['text_ratio'], 'title': (d['title'] or '(no title)')[:60]}
    for u, d in crawled.items() if d['text_ratio'] < 15
], key=lambda x: x['ratio'])

inbound_counts = {u: len(link_graph.get(u, set())) for u in crawled}
single_link_pages = sorted([
    {'url': rel(u), 'inbound': c, 'title': (crawled[u]['title'] or '(no title)')[:60]}
    for u, c in inbound_counts.items() if c <= 1
], key=lambda x: x['url'])

no_meta_pages = sorted([
    {'url': rel(u), 'title': (d['title'] or '(no title)')[:60]}
    for u, d in crawled.items() if not d['meta_desc']
], key=lambda x: x['url'])

multi_h1_pages = sorted([
    {'url': rel(u), 'h1_count': d['h1_count'], 'title': (d['title'] or '(no title)')[:60]}
    for u, d in crawled.items() if d['h1_count'] > 1
], key=lambda x: (-x['h1_count'], x['url']))

no_h1_pages = sorted([rel(u) for u, d in crawled.items() if d['h1_count'] == 0])

title_map = defaultdict(list)
for u, d in crawled.items():
    t = d['title'].strip()
    if t:
        title_map[t].append(rel(u))
dup_titles = sorted([{'title': t, 'urls': urls} for t, urls in title_map.items() if len(urls) > 1],
                    key=lambda x: -len(x['urls']))

long_titles = sorted([
    {'url': rel(u), 'len': len(d['title']), 'title': d['title'][:80]}
    for u, d in crawled.items() if len(d['title']) > 60
], key=lambda x: -x['len'])

noindex_pages = sorted([
    {'url': rel(u), 'robots': d['meta_robots']}
    for u, d in crawled.items() if d['meta_robots'] and 'noindex' in d['meta_robots']
], key=lambda x: x['url'])

bad_canonical = sorted([
    {'url': rel(u), 'canonical': d['canonical']}
    for u, d in crawled.items()
    if d['canonical'] and normalise(d['canonical']) != u
], key=lambda x: x['url'])

missing_canonical = sorted([rel(u) for u, d in crawled.items() if not d['canonical']])

has_schema_pages = [u for u, d in crawled.items() if d['has_schema']]

# Orphans: in sitemap but zero inbound internal links found in crawl
orphans = sorted([
    rel(u) for u in sitemap_urls
    if u in crawled and len(link_graph.get(u, set())) == 0 and u != BASE_URL + '/'
])

output = {
    'crawl_summary': {'pages_crawled': page_count, 'pages_with_data': len(crawled)},
    'extras': extras,
    'broken_links': broken_links,
    'thin_content': thin_pages,
    'single_inbound_link': single_link_pages,
    'orphan_pages': orphans,
    'missing_meta': no_meta_pages,
    'multiple_h1': multi_h1_pages,
    'no_h1': no_h1_pages,
    'duplicate_titles': dup_titles,
    'long_titles': long_titles,
    'noindex_pages': noindex_pages,
    'canonical_mismatch': bad_canonical,
    'missing_canonical': missing_canonical,
    'schema_status': {
        'pages_with_schema': len(has_schema_pages),
        'total_pages': len(crawled),
        'has_llms_txt': extras.get('llms_txt', False),
        'schema_pages': [rel(u) for u in has_schema_pages[:15]],
    },
}

out_path = r"C:\Users\jones\Claude\lendforall-full-audit.json"
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)

print(f"\n{'='*60}\nAUDIT RESULTS\n{'='*60}")
print(f"Pages crawled:          {page_count}")
print(f"Broken link instances:  {len(broken_links)}")
print(f"Thin content (<15%):    {len(thin_pages)}")
print(f"<=1 inbound link:       {len(single_link_pages)}")
print(f"Orphan sitemap pages:   {len(orphans)}")
print(f"Missing meta desc:      {len(no_meta_pages)}")
print(f"Multiple H1 tags:       {len(multi_h1_pages)}")
print(f"No H1 tag:              {len(no_h1_pages)}")
print(f"Duplicate title groups: {len(dup_titles)}")
print(f"Titles >60 chars:       {len(long_titles)}")
print(f"Noindex pages:          {len(noindex_pages)}")
print(f"Canonical mismatch:     {len(bad_canonical)}")
print(f"Missing canonical:      {len(missing_canonical)}")
print(f"Pages with schema:      {len(has_schema_pages)}/{len(crawled)}")
print(f"llms.txt exists:        {extras.get('llms_txt')}")
print(f"\nSaved to: {out_path}")
