"""Check pages for missing local resources, duplicate IDs, and broken fragments."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json

ROOT = Path(__file__).resolve().parents[1]
PAGES = [ROOT/'index.html', ROOT/'assets/resume.html']
errors=[]
class Page(HTMLParser):
    def __init__(self,path):
        super().__init__(); self.path=path; self.ids=set(); self.links=[]; self.json=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids: errors.append(f'{self.path.name}: duplicate id {a["id"]}')
            self.ids.add(a['id'])
        if tag=='img' and not a.get('alt'): errors.append(f'{self.path.name}: missing image alt')
        for field in ['href','src']:
            if a.get(field): self.links.append(a[field])
        self.json=tag=='script' and a.get('type')=='application/ld+json'
    def handle_data(self,data):
        if self.json:
            try: json.loads(data)
            except ValueError as e: errors.append(f'Invalid JSON-LD: {e}')
    def handle_endtag(self,tag):
        if tag=='script': self.json=False

parsed={}
for p in PAGES:
    parser=Page(p); parser.feed(p.read_text(encoding='utf-8')); parsed[p.resolve()]=parser
for p,parser in parsed.items():
    for target in parser.links:
        u=urlsplit(target)
        if u.scheme or u.netloc: continue
        destination=(p.parent/unquote(u.path)).resolve() if u.path else p
        if not destination.is_relative_to(ROOT): errors.append(f'Escaping path: {target}'); continue
        if not destination.exists(): errors.append(f'{p.name}: missing {target}')
        if u.fragment and destination in parsed and unquote(u.fragment) not in parsed[destination].ids:
            errors.append(f'{p.name}: missing fragment {target}')
if errors: raise SystemExit('\n'.join(errors))
print(f'PASS: {len(PAGES)} HTML pages; local resources, internal anchors, image alt text, and JSON-LD.')
