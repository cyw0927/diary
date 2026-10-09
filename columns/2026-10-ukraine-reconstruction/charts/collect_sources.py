"""Public-source retrieval. Run from the column directory; no credentials required.

Downloaded copyrighted documents stay in the local, untracked research cache.
The committed audit records access, not an assertion that every claim is true.
"""
import concurrent.futures, csv, io, json, re, sys, urllib.request,subprocess
from pathlib import Path
from html.parser import HTMLParser
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / '.research-cache'
DATA = ROOT / 'data'
CACHE.mkdir(exist_ok=True)
DATA.mkdir(exist_ok=True)

class TextParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.hidden=0
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style'): self.hidden+=1
        if tag in ('p','tr','div','br','h1','h2','h3'): self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script','style'): self.hidden=max(0,self.hidden-1)
    def handle_data(self, data):
        if not self.hidden: self.parts.append(data)

def fetch(url):
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 Research; public data'})
    with urllib.request.urlopen(req,timeout=35) as r: return r.read(),r.status,r.headers.get_content_type(),r.url

def cache_one(item):
    ident,url=item
    try:
        raw,status,ctype,final=fetch(url)
        if raw.startswith(b'%PDF'):
            text='\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+(p.extract_text() or '') for i,p in enumerate(PdfReader(io.BytesIO(raw)).pages))
        else:
            html=raw.decode('utf-8',errors='replace'); parser=TextParser(); parser.feed(html)
            text=''.join(parser.parts); text=re.sub(r'[ \t]+',' ',text);text=re.sub(r'\n\s*\n','\n',text)
        (CACHE/f'{ident}.txt').write_text(text,encoding='utf-8')
        return {'id':ident,'url':url,'http_status':status,'content_type':ctype,'final_url':final,'extracted_chars':len(text),'access_result':'retrieved; substantive review separate'}
    except Exception as e: return {'id':ident,'url':url,'access_result':str(e)}

if __name__=='__main__':
    if sys.argv[1]=='audit':
        original=subprocess.check_output(['git','show','ea55d09c43c4452235d2c71e861549dc2af3aa3f:columns/2026-10-ukraine-reconstruction/ukraine_reconstruction_critique.md'],cwd=ROOT,encoding='utf-8')
        source=original.split('### 주요 출처')[1]
        jobs=[]
        for line in source.splitlines():
            m=re.match(r'(\d+)\. ',line)
            if m:
                for n,url in enumerate(re.findall(r'https?://[^\s;]+',line)):
                    jobs.append((f'old_{int(m[1]):02}_{n}',url.rstrip(').')))
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool: results=list(pool.map(cache_one,jobs))
        (DATA/'original_source_access_audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
        print(json.dumps(results,ensure_ascii=False,indent=2))
    elif sys.argv[1]=='get':
        print(json.dumps(cache_one((sys.argv[2],sys.argv[3])),ensure_ascii=False))
    elif sys.argv[1]=='wdi':
        countries='UKR;POL;CZE;SVK;ROU;MDA;EST;LVA;LTU'
        rows=[]
        for indicator in ['NY.GDP.MKTP.KD','NY.GDP.PCAP.CD','NE.GDI.FTOT.ZS']:
            url=f'https://api.worldbank.org/v2/country/{countries}/indicator/{indicator}?format=json&date=1990:2021&per_page=20000'
            raw,*_=fetch(url); result=json.loads(raw)
            (DATA/f'wdi_{indicator}.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
            for r in result[1]: rows.append({'country':r['countryiso3code'],'year':int(r['date']),'indicator':indicator,'value':r['value']})
        with (DATA/'prewar_wdi.csv').open('w',newline='',encoding='utf-8-sig') as f:
            w=csv.DictWriter(f,fieldnames=['country','year','indicator','value']);w.writeheader();w.writerows(rows)
        print('WDI rows',len(rows))
