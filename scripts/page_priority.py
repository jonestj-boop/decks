import json
with open('gsc_kremp.json') as f:
    data = json.load(f)
pages = data['pages']

all_pages = sorted(pages.values(), key=lambda x: x['total_impressions'], reverse=True)

commercial = [p for p in all_pages if '/collections' in p['url'] or '/products' in p['url']]
informational = [p for p in all_pages if '/blogs' in p['url'] or '/pages' in p['url']]

print('TOP COMMERCIAL PAGES:')
for p in commercial[:15]:
    url = p['url'].replace('/kremp.com','')
    print(f"  {url[:55]:<55}  impr={p['total_impressions']:>7}  pos={p['avg_position']:>5.1f}  ctr={p['ctr']:.1f}%")

print()
print('TOP INFORMATIONAL PAGES:')
for p in informational[:20]:
    url = p['url'].replace('/kremp.com','')
    print(f"  {url[:55]:<55}  impr={p['total_impressions']:>7}  pos={p['avg_position']:>5.1f}  ctr={p['ctr']:.1f}%")
