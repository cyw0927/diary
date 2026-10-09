import re,json,concurrent.futures,pandas as pd
from collect_sources import fetch,cache_one,CACHE,DATA
h=(CACHE/'sambu_h1_viewer.html').read_text(encoding='utf-8')
tasks=[]
for m in re.finditer(r"node\d+\['text'\] = \"([^\"]+)\";(.*?)(?:cnt\+\+|node\d+\['text'\])",h,re.S):
 title,block=m.groups()
 if any(s in title for s in ['사업의 내용','매출 및 수주','재무에 관한 사항']):
  p={k:re.search(r"\['"+k+r"'\] = \"([^\"]+)\"",block).group(1) for k in ['rcpNo','dcmNo','eleId','offset','length','dtd']}
  url='https://dart.fss.or.kr/report/viewer.do?'+'&'.join(f'{k}={v}' for k,v in p.items());tasks.append(('sambu_h1_'+p['eleId'],url));print(title,url)
tasks.append(('sambu_review_latest','https://dart.fss.or.kr/report/viewer.do?rcpNo=20260831800966&dcmNo=11561863&eleId=0&offset=0&length=0&dtd=HTML'))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for r in ex.map(cache_one,tasks):print(r)
df=pd.read_csv(DATA/'ukrn_official_holdings_0.csv',header=None).iloc[5:].copy();df.columns=['name','shares','value','currency','id','country','region','isin','weight'];df['weight']=pd.to_numeric(df.weight,errors='coerce');df['value']=pd.to_numeric(df.value,errors='coerce');df=df.dropna(subset=['weight']);df.to_csv(DATA/'ukrn_holdings_20261008.csv',index=False,encoding='utf-8-sig');print(df.groupby('country').weight.sum().mul(100).round(2).to_dict());print('valuesum',df.value.sum(),'weightsum',df.weight.sum())
