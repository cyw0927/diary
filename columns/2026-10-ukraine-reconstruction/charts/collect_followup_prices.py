import ast,csv,json,concurrent.futures
from collect_sources import DATA,fetch
def one(code):
 u=f'https://api.finance.naver.com/siseJson.naver?symbol={code}&requestType=1&startTime=20230515&endTime=20261008&timeframe=day';raw,*_=fetch(u);r=ast.literal_eval(raw.decode('utf-8-sig').strip());rows=[x for x in r[1:] if len(x)>5];eligible=[x for x in rows if float(x[5])>0 and float(x[4])>0];first=eligible[0];last=eligible[-1]
 with (DATA/f'stock_{code}_20230515_20261008.csv').open('w',newline='',encoding='utf-8-sig') as f:
  w=csv.writer(f);w.writerow(['date','open','high','low','close','volume','foreign_ratio']);w.writerows(rows)
 return dict(code=code,url=u,base_date=first[0],base_close=first[4],last_trading_date=last[0],last_close=last[4],provider_return_percent=(last[4]/first[4]-1)*100,limitation='Naver-provided series, corporate-action coefficients not KRX-certified; price return excludes dividends')
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as p:r=list(p.map(one,['317850','041440','039560']))
(DATA/'other_korean_stocks_followup.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8');print(r)
