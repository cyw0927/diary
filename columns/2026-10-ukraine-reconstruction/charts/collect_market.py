import ast, csv, json, re, urllib.parse, urllib.request, concurrent.futures
from collect_sources import ROOT, DATA, CACHE, fetch, cache_one

def daily(code):
    url=f'https://api.finance.naver.com/siseJson.naver?symbol={code}&requestType=1&startTime=20230515&endTime=20230731&timeframe=day'
    try:
        raw,*_=fetch(url); text=raw.decode('utf-8-sig')
        (CACHE/f'naver_{code}.txt').write_text(text,encoding='utf-8')
        data=ast.literal_eval(text.strip()); rows=[]
        for row in data[1:]:
            if len(row)<6: continue
            rows.append(dict(code=code,date=str(row[0]),open=row[1],high=row[2],low=row[3],close=row[4],volume=row[5],provider='Naver Finance; adjustment not independently certified'))
        with (DATA/f'stock_{code}_20230515_20230731.csv').open('w',newline='',encoding='utf-8-sig') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
        window=[r for r in rows if r['date']<='20230717']; base=window[0]; peak=max(window,key=lambda x:x['close']);end=window[-1]
        return dict(code=code,base=base,peak=peak,end=end,peak_return=100*(peak['close']/base['close']-1),end_return=100*(end['close']/base['close']-1),url=url)
    except Exception as e:return dict(code=code,error=str(e),url=url)

if __name__=='__main__':
    codes=['001470','010600','001140','317850','041440','039560']
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as p: results=list(p.map(daily,codes))
    (DATA/'korean_stocks_comparison.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8'); print(json.dumps(results,ensure_ascii=False,indent=2))
    for ident,url in [('lugano_page','https://www.urc-international.com/past-conferences/urc22/urc2022-recovery-plan'),('ukrn','https://hanetf.com/fund/ukrn-defiance-ukraine-reconstruction-etf/')]:
        try:
            html=fetch(url)[0].decode('utf-8');links=re.findall(r'href=[\"\']([^\"\']+)[\"\']',html)
            matches=[x for x in links if ('.pdf' in x if ident=='lugano_page' else ('holdings' in x.lower() or 'factsheet' in x.lower()))]
            (CACHE/f'{ident}_links.json').write_text(json.dumps(matches,indent=2),encoding='utf-8');print(ident,matches[:4])
            if ident=='lugano_page' and matches:print(cache_one(('lugano_blueprint',matches[0])))
        except Exception as e:print(ident,str(e))
