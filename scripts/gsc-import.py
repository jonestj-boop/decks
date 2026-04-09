#!/usr/bin/env python3
"""
Parse Google Search Console CSV exports and output normalized JSON.

Supports three GSC export formats:
  A) Pages report — URL-level aggregate metrics
  B) Queries report — Query-level aggregate metrics
  C) Pages + Queries matrix — Per page+query pair metrics (ideal)

Auto-detects format from column headers.

Usage:
  python3 gsc-import.py <csv_file> [--domain embertribe.com] [--rewrite /=/blog/]
  python3 gsc-import.py <csv1> <csv2> --merge --domain embertribe.com

Options:
  --domain    Domain(s) to strip from URLs. Can be repeated.
  --rewrite   URL path rewrite rule: old_prefix=new_prefix. Can be repeated.
              Example: --rewrite /=/blog/  (rewrites "/" to "/blog/" for old blog subdomain)
  --merge     Merge multiple CSV files into one output (sum clicks/impressions, weighted avg position).
  --post-index  Path to post-index.json for URL matching. Outputs match results.
  --output    Output file path. Defaults to stdout.
  --date-range  Date range label (e.g., "2025-09-01 to 2026-03-01"). Included in output metadata.
"""

import csv
import json
import sys
import re
from collections import defaultdict
from pathlib import Path


def detect_format(headers):
    """Auto-detect GSC export format from column headers."""
    headers_lower = [h.lower().strip() for h in headers]

    has_page = any('page' in h for h in headers_lower)
    has_query = any('query' in h or 'queries' in h for h in headers_lower)

    if has_page and has_query:
        return 'matrix'
    elif has_page:
        return 'pages'
    elif has_query:
        return 'queries'
    else:
        # Try to detect by first column name
        if 'top pages' in headers_lower[0]:
            return 'pages'
        elif 'top queries' in headers_lower[0]:
            return 'queries'
        raise ValueError(f"Cannot detect GSC format. Headers: {headers}")


def find_column(headers, candidates):
    """Find a column by trying multiple possible names."""
    headers_lower = [h.lower().strip() for h in headers]
    for candidate in candidates:
        for i, h in enumerate(headers_lower):
            if candidate in h:
                return i
    return None


def parse_numeric(value, as_float=False):
    """Parse a numeric value, handling commas, percentages, etc."""
    if not value or value.strip() == '':
        return 0.0 if as_float else 0
    value = value.strip().replace(',', '').replace('%', '')
    try:
        return float(value) if as_float else int(float(value))
    except (ValueError, TypeError):
        return 0.0 if as_float else 0


def normalize_url(url, domains=None, rewrites=None):
    """Normalize a GSC URL to a path-only format."""
    # Strip protocol
    url = re.sub(r'^https?://', '', url)

    # Strip www.
    url = re.sub(r'^www\.', '', url)

    # Strip known domains
    if domains:
        for domain in domains:
            domain_clean = domain.replace('www.', '')
            if url.startswith(domain_clean):
                url = url[len(domain_clean):]
                break

    # Ensure starts with /
    if not url.startswith('/'):
        url = '/' + url

    # Apply rewrite rules
    if rewrites:
        for old_prefix, new_prefix in rewrites:
            if url.startswith(old_prefix):
                url = new_prefix + url[len(old_prefix):]
                break

    # Strip trailing slash (but keep root /)
    if url != '/' and url.endswith('/'):
        url = url.rstrip('/')

    return url


def parse_csv_file(filepath, domains=None, rewrites=None):
    """Parse a single GSC CSV file. Returns (format, rows)."""
    rows = []

    with open(filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        headers = next(reader)

        fmt = detect_format(headers)

        # Find column indices
        if fmt in ('pages', 'matrix'):
            page_col = find_column(headers, ['top pages', 'page', 'pages'])
        if fmt in ('queries', 'matrix'):
            query_col = find_column(headers, ['top queries', 'query', 'queries'])

        clicks_col = find_column(headers, ['clicks'])
        impressions_col = find_column(headers, ['impressions'])
        ctr_col = find_column(headers, ['ctr'])
        position_col = find_column(headers, ['position'])

        for row in reader:
            if not row or not any(cell.strip() for cell in row):
                continue

            entry = {
                'clicks': parse_numeric(row[clicks_col]) if clicks_col is not None else 0,
                'impressions': parse_numeric(row[impressions_col]) if impressions_col is not None else 0,
                'ctr': parse_numeric(row[ctr_col], as_float=True) if ctr_col is not None else 0.0,
                'position': parse_numeric(row[position_col], as_float=True) if position_col is not None else 0.0,
            }

            if fmt in ('pages', 'matrix') and page_col is not None:
                entry['page'] = normalize_url(row[page_col], domains, rewrites)
                entry['raw_url'] = row[page_col].strip()

            if fmt in ('queries', 'matrix') and query_col is not None:
                entry['query'] = row[query_col].strip()

            rows.append(entry)

    return fmt, rows


def aggregate_by_page(all_rows):
    """Aggregate rows by page URL. Handles merging from multiple CSVs."""
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

    for row in all_rows:
        if 'page' not in row:
            continue

        page = row['page']
        pd = page_data[page]
        pd['clicks'] += row['clicks']
        pd['impressions'] += row['impressions']
        pd['position_weighted_sum'] += row['position'] * row['impressions']
        pd['raw_urls'].add(row.get('raw_url', ''))

        if 'query' in row:
            qd = pd['queries'][row['query']]
            qd['clicks'] += row['clicks']
            qd['impressions'] += row['impressions']
            qd['position_weighted_sum'] += row['position'] * row['impressions']

    # Calculate final metrics
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

        # Identify striking distance queries (position 5-20, impressions > 50)
        striking = []
        for q in queries:
            if 5 <= q['position'] <= 20 and q['impressions'] > 50:
                # Estimate clicks at position 3
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
            'queries': queries[:50],  # Top 50 queries per page
            'striking_distance_queries': striking,
            'query_count': len(queries),
            'raw_urls': list(pd['raw_urls'] - {''}),
        }

    return results


def match_to_index(page_data, post_index_path):
    """Match GSC pages to post index entries."""
    with open(post_index_path) as f:
        index = json.load(f)

    # Build URL lookup from index
    url_to_post = {}
    for post in index:
        url = post.get('url', '')
        if url:
            url_to_post[url] = post
        # Also try with slug
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

    # Sort by total impressions (most impactful conflicts first)
    groups.sort(key=lambda g: -sum(p['impressions'] for p in g['pages']))
    return groups


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Parse GSC CSV exports')
    parser.add_argument('csvfiles', nargs='+', help='GSC CSV file(s)')
    parser.add_argument('--domain', action='append', default=[], help='Domain(s) to strip')
    parser.add_argument('--rewrite', action='append', default=[], help='URL rewrite: old=new')
    parser.add_argument('--post-index', help='Path to post-index.json for matching')
    parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    parser.add_argument('--date-range', default='', help='Date range label')

    args = parser.parse_args()

    # Parse rewrite rules
    rewrites = []
    for r in args.rewrite:
        parts = r.split('=', 1)
        if len(parts) == 2:
            rewrites.append((parts[0], parts[1]))

    # Parse all CSVs
    all_rows = []
    sources = []
    for csvfile in args.csvfiles:
        fmt, rows = parse_csv_file(csvfile, args.domain, rewrites)
        all_rows.extend(rows)
        sources.append({
            'filename': Path(csvfile).name,
            'format': fmt,
            'rows': len(rows),
            'truncated': len(rows) == 1000,
        })
        print(f"Parsed {Path(csvfile).name}: {len(rows)} rows, format: {fmt}", file=sys.stderr)

    # Aggregate by page
    page_data = aggregate_by_page(all_rows)
    print(f"Aggregated to {len(page_data)} unique pages", file=sys.stderr)

    # Build output
    output = {
        'sources': sources,
        'date_range': args.date_range,
        'total_pages': len(page_data),
    }

    # Match to post index if provided
    if args.post_index:
        matched, unmatched_blog, unmatched_other = match_to_index(page_data, args.post_index)
        cannibalization = detect_cannibalization(matched) if matched else []

        output['matched_posts'] = len(matched)
        output['unmatched_blog_urls'] = len(unmatched_blog)
        output['non_blog_urls'] = len(unmatched_other)
        output['cannibalization_groups'] = cannibalization[:20]  # Top 20 conflicts
        output['pages'] = matched
        output['unmatched_blog'] = unmatched_blog[:50]  # Sample
        output['unmatched_other'] = unmatched_other[:50]  # Sample

        print(f"Matched: {len(matched)} posts | Unmatched blog: {len(unmatched_blog)} | Non-blog: {len(unmatched_other)}", file=sys.stderr)
        if cannibalization:
            print(f"Potential cannibalization: {len(cannibalization)} query groups", file=sys.stderr)
    else:
        output['pages'] = page_data

    # Write output
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(output, f, indent=2, default=str)
        print(f"Output written to {args.output}", file=sys.stderr)
    else:
        json.dump(output, f=sys.stdout, indent=2, default=str)


if __name__ == '__main__':
    main()
