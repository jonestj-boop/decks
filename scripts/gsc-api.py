#!/usr/bin/env python3
"""
Pull Google Search Console data via the API using a service account.

Paginates automatically (25K rows per request) to get the full dataset.
Outputs the same JSON format as gsc-import.py for downstream compatibility.

Usage:
  python3 gsc-api.py --key-file <service-account.json> \
    --site <site_url> \
    --days 180 \
    --post-index <post-index.json> \
    --domain embertribe.com \
    --output <output.json>

  # Pull from multiple GSC properties and merge:
  python3 gsc-api.py --key-file <sa.json> \
    --site sc-domain:embertribe.com \
    --site https://blog.embertribe.com/ \
    --days 180 \
    --domain embertribe.com --domain blog.embertribe.com \
    --rewrite /=/blog/ \
    --post-index clients/embertribe/post-index.json \
    --output clients/embertribe/gsc-data.json

Options:
  --key-file    Path to service account JSON key file. Required.
  --site        GSC property URL. Can be repeated for multiple properties.
                Use "sc-domain:example.com" for domain properties, or
                "https://example.com/" for URL-prefix properties.
  --days        Number of days to pull (default: 180 = ~6 months).
  --domain      Domain(s) to strip during URL normalization. Can be repeated.
  --rewrite     URL path rewrite: old_prefix=new_prefix. Can be repeated.
  --post-index  Path to post-index.json for URL matching.
  --output      Output file path. Required.
"""

import json
import sys
import argparse
from datetime import datetime, timedelta
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build

# Import normalization/matching functions from gsc-import.py
SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))
from importlib import import_module


def normalize_url(url, domains=None, rewrites=None):
    """Normalize a GSC URL to a path-only format.

    Args:
        domains: List of domains to strip
        rewrites: List of (domain, old_prefix, new_prefix) tuples.
                  Rewrites are only applied when the URL matched that specific domain.
                  If domain is None, the rewrite applies to all URLs.
    """
    import re
    # Strip protocol
    url = re.sub(r'^https?://', '', url)
    # Strip www.
    url = re.sub(r'^www\.', '', url)
    # Strip known domains and track which one matched
    matched_domain = None
    if domains:
        for domain in domains:
            domain_clean = domain.replace('www.', '')
            if url.startswith(domain_clean):
                matched_domain = domain_clean
                url = url[len(domain_clean):]
                break
    # Ensure starts with /
    if not url.startswith('/'):
        url = '/' + url
    # Apply rewrite rules (domain-scoped)
    if rewrites:
        for rewrite in rewrites:
            if len(rewrite) == 3:
                rw_domain, old_prefix, new_prefix = rewrite
                # Only apply if this URL came from the specified domain
                if rw_domain and matched_domain and rw_domain.replace('www.', '') != matched_domain:
                    continue
            else:
                old_prefix, new_prefix = rewrite
            # Special mode: "slug-only" extracts just the last path segment
            if new_prefix.endswith('{slug}'):
                base = new_prefix.replace('{slug}', '')
                # Extract the last path component as the slug
                slug = url.rstrip('/').split('/')[-1]
                if slug:
                    url = base + slug
                break
            elif url.startswith(old_prefix):
                url = new_prefix + url[len(old_prefix):]
                break
    # Strip trailing slash (but keep root /)
    if url != '/' and url.endswith('/'):
        url = url.rstrip('/')
    return url


def build_service(key_file):
    """Build an authenticated GSC API service."""
    SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
    credentials = service_account.Credentials.from_service_account_file(
        key_file, scopes=SCOPES
    )
    return build('searchconsole', 'v1', credentials=credentials)


def pull_data(service, site_url, start_date, end_date, dimensions=None):
    """Pull search analytics data with pagination."""
    if dimensions is None:
        dimensions = ['page', 'query']

    all_rows = []
    start_row = 0
    row_limit = 25000

    while True:
        request_body = {
            'startDate': start_date,
            'endDate': end_date,
            'dimensions': dimensions,
            'rowLimit': row_limit,
            'startRow': start_row,
        }

        response = service.searchanalytics().query(
            siteUrl=site_url,
            body=request_body
        ).execute()

        rows = response.get('rows', [])
        if not rows:
            break

        all_rows.extend(rows)
        print(f"  Pulled {len(all_rows)} rows so far (batch: {len(rows)})...", file=sys.stderr)

        if len(rows) < row_limit:
            break  # Last page

        start_row += row_limit

    return all_rows


def rows_to_entries(rows, dimensions, domains=None, rewrites=None):
    """Convert API rows to normalized entries."""
    entries = []
    for row in rows:
        keys = row.get('keys', [])
        entry = {
            'clicks': row.get('clicks', 0),
            'impressions': row.get('impressions', 0),
            'ctr': round(row.get('ctr', 0) * 100, 2),  # API returns decimal
            'position': round(row.get('position', 0), 1),
        }

        for i, dim in enumerate(dimensions):
            if dim == 'page' and i < len(keys):
                entry['raw_url'] = keys[i]
                entry['page'] = normalize_url(keys[i], domains, rewrites)
            elif dim == 'query' and i < len(keys):
                entry['query'] = keys[i]

        entries.append(entry)

    return entries


def aggregate_by_page(all_entries):
    """Aggregate entries by page URL."""
    from collections import defaultdict

    page_data = defaultdict(lambda: {
        'clicks': 0,
        'impressions': 0,
        'position_weighted_sum': 0.0,
        'queries': defaultdict(lambda: {
            'clicks': 0,
            'impressions': 0,
            'position_weighted_sum': 0.0,
        }),
        'raw_urls': set(),
    })

    for entry in all_entries:
        if 'page' not in entry:
            continue

        page = entry['page']
        pd = page_data[page]
        pd['clicks'] += entry['clicks']
        pd['impressions'] += entry['impressions']
        pd['position_weighted_sum'] += entry['position'] * entry['impressions']
        pd['raw_urls'].add(entry.get('raw_url', ''))

        if 'query' in entry:
            qd = pd['queries'][entry['query']]
            qd['clicks'] += entry['clicks']
            qd['impressions'] += entry['impressions']
            qd['position_weighted_sum'] += entry['position'] * entry['impressions']

    results = {}
    for page, pd in page_data.items():
        imp = pd['impressions']
        avg_pos = pd['position_weighted_sum'] / imp if imp > 0 else 0.0
        ctr = (pd['clicks'] / imp * 100) if imp > 0 else 0.0

        queries = []
        for query, qd in sorted(pd['queries'].items(), key=lambda x: -x[1]['impressions']):
            q_imp = qd['impressions']
            q_pos = qd['position_weighted_sum'] / q_imp if q_imp > 0 else 0.0
            q_ctr = (qd['clicks'] / q_imp * 100) if q_imp > 0 else 0.0
            queries.append({
                'query': query,
                'clicks': qd['clicks'],
                'impressions': q_imp,
                'ctr': round(q_ctr, 2),
                'position': round(q_pos, 1),
            })

        striking = []
        for q in queries:
            if 5 <= q['position'] <= 20 and q['impressions'] > 50:
                potential_clicks = int(q['impressions'] * 0.11)
                striking.append({
                    'query': q['query'],
                    'position': q['position'],
                    'impressions': q['impressions'],
                    'current_clicks': q['clicks'],
                    'potential_clicks': potential_clicks,
                })

        results[page] = {
            'url': page,
            'total_clicks': pd['clicks'],
            'total_impressions': imp,
            'ctr': round(ctr, 2),
            'avg_position': round(avg_pos, 1),
            'queries': queries[:50],
            'striking_distance_queries': striking,
            'query_count': len(queries),
            'raw_urls': list(pd['raw_urls'] - {''}),
        }

    return results


def match_to_index(page_data, post_index_path):
    """Match GSC pages to post index entries."""
    with open(post_index_path) as f:
        index = json.load(f)

    url_to_post = {}
    for post in index:
        url = post.get('url', '')
        if url:
            url_to_post[url] = post
        slug = post.get('id', '').split('/')[-1] if post.get('id') else ''
        if slug:
            url_to_post[f'/blog/{slug}'] = post

    matched = {}
    unmatched_blog = []
    unmatched_other = []

    for url, data in page_data.items():
        if url in url_to_post:
            post = url_to_post[url]
            data['post_id'] = post.get('id', '')
            data['post_title'] = post.get('title', '')
            data['webflow_id'] = post.get('webflow_id', '')
            matched[url] = data
        elif '/blog/' in url:
            unmatched_blog.append(data)
        else:
            unmatched_other.append(data)

    return matched, unmatched_blog, unmatched_other


def detect_cannibalization(matched_data):
    """Find posts competing for the same queries."""
    from collections import defaultdict

    query_to_pages = defaultdict(list)
    for url, data in matched_data.items():
        for q in data.get('queries', []):
            if 5 <= q['position'] <= 30 and q['impressions'] > 30:
                query_to_pages[q['query']].append({
                    'url': url,
                    'post_title': data.get('post_title', ''),
                    'position': q['position'],
                    'impressions': q['impressions'],
                    'clicks': q['clicks'],
                })

    groups = []
    for query, pages in query_to_pages.items():
        if len(pages) >= 2:
            groups.append({
                'shared_query': query,
                'pages': sorted(pages, key=lambda x: x['position']),
            })

    groups.sort(key=lambda g: -sum(p['impressions'] for p in g['pages']))
    return groups


def main():
    parser = argparse.ArgumentParser(description='Pull GSC data via API')
    parser.add_argument('--key-file', required=True, help='Service account JSON key file')
    parser.add_argument('--site', action='append', required=True, help='GSC property URL(s)')
    parser.add_argument('--days', type=int, default=180, help='Days of data to pull')
    parser.add_argument('--domain', action='append', default=[], help='Domain(s) to strip')
    parser.add_argument('--rewrite', action='append', default=[], help='URL rewrite: old=new')
    parser.add_argument('--post-index', help='Path to post-index.json')
    parser.add_argument('--output', '-o', required=True, help='Output file path')

    args = parser.parse_args()

    # Parse rewrite rules (format: "domain:old=new" or "old=new")
    rewrites = []
    for r in args.rewrite:
        if ':' in r and '=' in r:
            domain_part, rule_part = r.split(':', 1)
            parts = rule_part.split('=', 1)
            if len(parts) == 2:
                rewrites.append((domain_part, parts[0], parts[1]))
        else:
            parts = r.split('=', 1)
            if len(parts) == 2:
                rewrites.append((None, parts[0], parts[1]))

    # Date range
    end_date = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')  # GSC has ~3 day lag
    start_date = (datetime.now() - timedelta(days=args.days)).strftime('%Y-%m-%d')
    date_range = f"{start_date} to {end_date}"
    print(f"Date range: {date_range}", file=sys.stderr)

    # Build authenticated service
    service = build_service(args.key_file)

    # Pull from all sites
    all_entries = []
    sources = []
    for site_url in args.site:
        print(f"\nPulling from: {site_url}", file=sys.stderr)
        try:
            rows = pull_data(service, site_url, start_date, end_date)
            entries = rows_to_entries(rows, ['page', 'query'], args.domain, rewrites)
            all_entries.extend(entries)
            sources.append({
                'site_url': site_url,
                'rows': len(rows),
                'method': 'api',
            })
            print(f"  Total: {len(rows)} rows from {site_url}", file=sys.stderr)
        except Exception as e:
            print(f"  ERROR pulling {site_url}: {e}", file=sys.stderr)
            sources.append({
                'site_url': site_url,
                'rows': 0,
                'method': 'api',
                'error': str(e),
            })

    if not all_entries:
        print("No data retrieved from any property.", file=sys.stderr)
        sys.exit(1)

    # Aggregate
    page_data = aggregate_by_page(all_entries)
    print(f"\nAggregated to {len(page_data)} unique pages", file=sys.stderr)

    # Build output
    output = {
        'sources': sources,
        'date_range': date_range,
        'total_pages': len(page_data),
    }

    # Match to post index if provided
    if args.post_index:
        matched, unmatched_blog, unmatched_other = match_to_index(page_data, args.post_index)
        cannibalization = detect_cannibalization(matched) if matched else []

        output['matched_posts'] = len(matched)
        output['unmatched_blog_urls'] = len(unmatched_blog)
        output['non_blog_urls'] = len(unmatched_other)
        output['cannibalization_groups'] = cannibalization[:20]
        output['pages'] = matched
        output['unmatched_blog'] = unmatched_blog[:50]
        output['unmatched_other'] = unmatched_other[:50]

        print(f"Matched: {len(matched)} posts | Unmatched blog: {len(unmatched_blog)} | Non-blog: {len(unmatched_other)}", file=sys.stderr)
        if cannibalization:
            print(f"Potential cannibalization: {len(cannibalization)} query groups", file=sys.stderr)
    else:
        output['pages'] = page_data

    # Write output
    with open(args.output, 'w') as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nOutput written to {args.output}", file=sys.stderr)


if __name__ == '__main__':
    main()
