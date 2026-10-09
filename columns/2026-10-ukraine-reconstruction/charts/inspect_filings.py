import io,json,re,pandas as pd
from collect_sources import fetch,CACHE,DATA,cache_one

raw,*_=fetch('https://etf.hanetf.com/Holdings-UKRN-IE000R8PO127-all-all')
x=pd.ExcelFile(io.BytesIO(raw)); print('ETF sheets',x.sheet_names)
for i,sheet in enumerate(x.sheet_names):
 df=pd.read_excel(x,sheet_name=sheet,header=None);df.to_csv(DATA/f'ukrn_official_holdings_{i}.csv',index=False,header=False,encoding='utf-8-sig');print(df.head(14).to_string(index=False,header=False))

for ident,rcp in [('sambu_h1','20260814004299'),('sambu_market_review','20260831800966')]:
 try:
  raw,*_=fetch(f'https://dart.fss.or.kr/dsaf001/main.do?rcpNo={rcp}');h=raw.decode('utf-8',errors='replace');(CACHE/f'{ident}_viewer.html').write_text(h,encoding='utf-8')
  print(ident,'doc IDs',re.findall(r'dcmNo[^\n]{0,100}',h)[:4]);print(ident,'viewDoc',re.findall(r'viewDoc\([^\n]{0,250}',h)[:4])
 except Exception as e:print(ident,str(e))

u='https://www.sec.gov/Archives/edgar/data/868857/000086885725000013/acm-20250930.htm';print(cache_one(('aecom_10k',u)))
u='https://zakon.rada.gov.ua/laws/show/388-2021-%D1%80';print(cache_one(('rada_water',u)))
