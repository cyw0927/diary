import re,sys
sys.stdout.reconfigure(encoding='utf-8')
from collect_sources import fetch,CACHE,TextParser
rcp='20260921800376';raw,*_=fetch('https://dart.fss.or.kr/dsaf001/main.do?rcpNo='+rcp);h=raw.decode('utf-8',errors='replace');m=re.search(r'viewDoc\("'+rcp+r'", "(\d+)"',h)
if not m:raise ValueError('No document ID')
url=f'https://dart.fss.or.kr/report/viewer.do?rcpNo={rcp}&dcmNo={m[1]}&eleId=0&offset=0&length=0&dtd=HTML';raw,*_=fetch(url);p=TextParser();p.feed(raw.decode('euc-kr',errors='replace'));(CACHE/'sambu_sept21.txt').write_text(''.join(p.parts),encoding='utf-8');print(url);print(''.join(p.parts))
