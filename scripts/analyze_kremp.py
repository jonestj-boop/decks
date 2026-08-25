import json

with open('gsc_kremp.json') as f:
    data = json.load(f)

pages = data['pages']

# Site-wide totals
total_clicks = sum(p['total_clicks'] for p in pages.values())
total_impressions = sum(p['total_impressions'] for p in pages.values())
avg_ctr = (total_clicks / total_impressions * 100) if total_impressions else 0

# Collect all queries
all_queries = {}
for page in pages.values():
    for q in page.get('queries', []):
        qk = q['query']
        if qk not in all_queries:
            all_queries[qk] = {'clicks': 0, 'impressions': 0, 'position_sum': 0, 'count': 0}
        all_queries[qk]['clicks'] += q['clicks']
        all_queries[qk]['impressions'] += q['impressions']
        all_queries[qk]['position_sum'] += q['position'] * q['impressions']
        all_queries[qk]['count'] += q['impressions']

query_list = []
for q, v in all_queries.items():
    avg_pos = v['position_sum'] / v['count'] if v['count'] else 0
    ctr = (v['clicks'] / v['impressions'] * 100) if v['impressions'] else 0
    query_list.append({'query': q, 'clicks': v['clicks'], 'impressions': v['impressions'], 'position': round(avg_pos, 1), 'ctr': round(ctr, 2)})

# Brand vs non-brand
brand_terms = ['kremp', 'kremp florist', 'krempflorist']
brand_clicks = sum(q['clicks'] for q in query_list if any(b in q['query'].lower() for b in brand_terms))
nonbrand_clicks = total_clicks - brand_clicks
brand_impr = sum(q['impressions'] for q in query_list if any(b in q['query'].lower() for b in brand_terms))
nonbrand_impr = total_impressions - brand_impr

print("=== SITE TOTALS (180 days) ===")
print(f"Total Clicks: {total_clicks:,}")
print(f"Total Impressions: {total_impressions:,}")
print(f"Avg CTR: {avg_ctr:.2f}%")
print(f"Unique Pages: {len(pages):,}")
print(f"Unique Queries: {len(query_list):,}")
print(f"Brand Clicks: {brand_clicks:,} ({brand_clicks/total_clicks*100:.1f}%)")
print(f"Non-Brand Clicks: {nonbrand_clicks:,} ({nonbrand_clicks/total_clicks*100:.1f}%)")

print("\n=== TOP 20 PAGES BY CLICKS ===")
top_pages = sorted(pages.values(), key=lambda x: x['total_clicks'], reverse=True)[:20]
for p in top_pages:
    url = p['url'][:60]
    print(f"  {url:<60} clicks={p['total_clicks']:>6}  impr={p['total_impressions']:>8}  ctr={p['ctr']:.1f}%  pos={p['avg_position']:.1f}")

print("\n=== TOP 20 QUERIES BY CLICKS ===")
top_queries = sorted(query_list, key=lambda x: x['clicks'], reverse=True)[:20]
for q in top_queries:
    qstr = q['query'][:50]
    print(f"  {qstr:<50} clicks={q['clicks']:>6}  impr={q['impressions']:>8}  ctr={q['ctr']:.1f}%  pos={q['position']:.1f}")

print("\n=== TOP OPPORTUNITY QUERIES (pos 4-20, high impressions, low CTR) ===")
opps = [q for q in query_list if 4 <= q['position'] <= 20 and q['impressions'] >= 500
        and not any(b in q['query'].lower() for b in brand_terms)]
opps.sort(key=lambda x: x['impressions'], reverse=True)
for q in opps[:20]:
    qstr = q['query'][:50]
    print(f"  {qstr:<50} clicks={q['clicks']:>6}  impr={q['impressions']:>8}  ctr={q['ctr']:.1f}%  pos={q['position']:.1f}")

print("\n=== HIGH IMPRESSION / LOW CTR PAGES (ctr < 2%, impr > 5000) ===")
low_ctr_pages = [p for p in pages.values() if p['ctr'] < 2.0 and p['total_impressions'] >= 5000]
low_ctr_pages.sort(key=lambda x: x['total_impressions'], reverse=True)
for p in low_ctr_pages[:15]:
    url = p['url'][:60]
    print(f"  {url:<60} clicks={p['total_clicks']:>6}  impr={p['total_impressions']:>8}  ctr={p['ctr']:.1f}%  pos={p['avg_position']:.1f}")

print("\n=== PAGES IN POSITION 11-20 (page 2 - quick wins) ===")
p2_pages = [p for p in pages.values() if 11 <= p['avg_position'] <= 20 and p['total_impressions'] >= 1000]
p2_pages.sort(key=lambda x: x['total_impressions'], reverse=True)
for p in p2_pages[:15]:
    url = p['url'][:60]
    print(f"  {url:<60} clicks={p['total_clicks']:>6}  impr={p['total_impressions']:>8}  ctr={p['ctr']:.1f}%  pos={p['avg_position']:.1f}")

print("\n=== TOP NON-BRAND QUERIES BY IMPRESSIONS ===")
nonbrand_queries = [q for q in query_list if not any(b in q['query'].lower() for b in brand_terms)]
nonbrand_queries.sort(key=lambda x: x['impressions'], reverse=True)
for q in nonbrand_queries[:20]:
    qstr = q['query'][:50]
    print(f"  {qstr:<50} clicks={q['clicks']:>6}  impr={q['impressions']:>8}  ctr={q['ctr']:.1f}%  pos={q['position']:.1f}")
