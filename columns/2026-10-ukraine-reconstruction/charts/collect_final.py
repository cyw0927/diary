import concurrent.futures,json,re
from collect_sources import DATA,CACHE,fetch,cache_one,TextParser
jobs=[('bechtel_mou','https://restoration.gov.ua/blog/agentstvo-vidnovlennya-spivpraczyuvatyme-z-liderom-u-sferi-inzhyniryngu-ta-budivnycztva-korporacziyeyu-bechtel/'),('bechtel_nsc','https://www.bechtel.com/projects/chornobyl-new-safe-confinement/'),('ferrexpo_may_price','https://www.lse.co.uk/news/ftse-100-movers-ferrexpo-gains-on-ukraine-minerals-deal-clarkson-tanks-tjh707hpuvbdjxg.html'),('ferrexpo_feb_price','https://good-time-invest.com/blog/ukrainian-companies-shares-on-the-rise-amid-prospects-of-wars-end/'),('ferrexpo_stooq','https://stooq.com/q/d/l/?s=fxpo.uk&i=d&d1=20241101&d2=20250502')]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as p:
 results=list(p.map(cache_one,jobs))
(DATA/'final_source_access_audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8');print([(r['id'],r.get('http_status'),r.get('extracted_chars')) for r in results])
u='https://dart.fss.or.kr/report/viewer.do?rcpNo=20260831800966&dcmNo=11561863&eleId=0&offset=0&length=0&dtd=HTML';raw,*_=fetch(u);h=raw.decode('euc-kr',errors='replace');p=TextParser();p.feed(h);(CACHE/'sambu_review_decoded.txt').write_text(''.join(p.parts),encoding='utf-8');print('KRX decoded',len(''.join(p.parts)))
