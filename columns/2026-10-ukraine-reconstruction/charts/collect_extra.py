import concurrent.futures, json, ast, urllib.parse, urllib.request
from collect_sources import CACHE, DATA, cache_one, fetch

JOBS = {
 'ukrainvest_lugano':'https://ukraineinvest.gov.ua/en/news/15-07-22-2/',
 'kse_2022':'https://kse.ua/russia-will-pay/',
 'sambu_q1':'https://kind.krx.co.kr/external/2026/05/15/002323/20260515005207/11013.htm',
 'ukrn':'https://hanetf.com/fund/ukrn-defiance-ukraine-reconstruction-etf/',
 'ukrn_holdings':'https://etf.hanetf.com/Holdings-UKRN-IE000R8PO127-all-all',
 'ukrn_factsheet':'https://etf.hanetf.com/Factsheet-UKRN-IE000R8PO127-en',
 'elementum':'https://disclosures.ifc.org/project-detail/SII/49272/elementum-debt',
 'ukrenergo':'https://www.ebrd.com/home/work-with-us/projects/psd/55539.html',
 'uz_alstom':'https://www.ebrd.com/home/news-and-events/news/2025/international-support-for-ukraine-demonstrated-through-major-rai.html',
 'm15':'https://pppagency.gov.ua/one-more-pilot-public-investment-project-has-begun-preparations-under-the-ukraine-government-ppf/',
 'kherson_port':'https://www.ebrd.com/home/news-and-events/news/2020/ebrd-supports-first-concession-project-in-ukraine.html',
 'mykolaiv':'https://www.eib.org/en/press/all/2024-453-ukraine-eib-provides-eur14-5-million-to-support-municipal-projects-in-war-torn-cities-of-mykolaiv-and-dnipro',
 'm10':'https://www.ebrd.com/home/news-and-events/news/2023/ebrd-invests-in-developing-lviv-industrial-park-in-western-ukraine.html',
 'm10_open':'https://ukraineinvest.gov.ua/en/news/27-02-2024-1/',
 'poland_mou':'https://www.gov.pl/web/aktywa-panstwowe/synergia-dla-odbudowy-ukrainy--podpisanie-porozumienia-o-wspolpracy-na-rzecz-odbudowy-ukrainy-w-ministerstwie-aktywow-panstwowych',
 'siemens_mou':'https://www.naftogaz.com/en/news/naftogaz-and-siemens-energy-sign-memorandum-on-energy-security-and-underground-gas-storage-modernisation',
 'crh_buzzi':'https://www.buzzi.com/w/completata-la-cessione-delle-attivita-in-ucraina',
 'aecom':'https://aecom.com/press-releases/aecom-to-serve-as-infrastructure-delivery-advisor-for-ukraine-reconstruction/',
 'ferrexpo_2026':'https://www.ferrexpo.com/media/nl5nlb2l/ferrexpo-2026-interim-results_website_final.pdf',
 'ferrexpo_2024':'https://www.ferrexpo.com/media/4pflducv/2025-3-19-ferrexpo-full-year-financial-results-for-2024-final-for-release.pdf',
 'euroclear_h1':'https://www.euroclear.com/newsandinsights/en/press/2026/mr-20-euroclear-h1-2026-results.html',
 'cbr_moscow':'https://www.cbr.ru/eng/press/PR/?file=639011472901412429OBAUT_E.htm',
 'cbr_eu':'https://www.cbr.ru/eng/press/pr/?file=639080409737537862OBAUT_E.htm',
 'eu_case':'https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A62026TN0150',
 'brussels_case':'https://www.brusselstimes.com/world/2209129/euroclear-sues-russian-central-bank-in-brussels-court',
 'midas_original':'https://nabu.gov.ua/en/news/operatciia-midas-vykryto-vysokorivnevu-zlochynnu-organizatciiu-shcho-diiala-u-sferi-energetyky/',
 'midas_update':'https://nabu.gov.ua/en/news/operatciia-midas-nova-pidozra/',
 'well_correction':'https://v.daum.net/v/VxCmJt4qcf',
 'sambu_indictment':'https://mobile.newsis.com/view_amp.html?ar_id=NISX20250926_0003345388',
 'sambu_rehab':'https://www.mt.co.kr/amp/stock/2026/06/29/2026062916314035715',
 'trial_latest':'https://v.daum.net/v/20260724163709596',
 'well_delist':'https://kr.investing.com/news/global-filings/article-93CH-2055634',
 'korea_kiep':'https://www.kiep.kr/galleryDownload.es?bid=0001&list_no=11547&seq=1',
}

if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as p: results=list(p.map(cache_one,JOBS.items()))
 (DATA/'additional_source_access_audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
 print([(x['id'],x.get('http_status'),x.get('extracted_chars'),x['access_result'] if not x.get('http_status') else '') for x in results])
 u='https://api.finance.naver.com/siseJson.naver?symbol=010600&requestType=1&startTime=20230501&endTime=20230731&timeframe=day'
 raw,*_=fetch(u); rows=ast.literal_eval(raw.decode('utf-8-sig').strip());(DATA/'well_may_july_provider.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8');print('well endpoints',rows[1],max(rows[1:],key=lambda x:x[4]),max(rows[1:],key=lambda x:x[2]))
 try:
  url='https://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'
  payload=urllib.parse.urlencode({'bld':'dbms/MDC/STAT/standard/MDCSTAT01701','isuCd':'KR7001470009','strtDd':'20230515','endDd':'20230717','inqCondTpCd':'Y','share':'1','money':'1','csvxls_isNo':'false'}).encode()
  req=urllib.request.Request(url,data=payload,headers={'User-Agent':'Mozilla/5.0','Referer':'https://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd'})
  with urllib.request.urlopen(req,timeout=30) as r: content=r.read().decode('utf-8',errors='replace')
  (CACHE/'krx_response.txt').write_text(content,encoding='utf-8'); print('KRX response',content[:300])
 except Exception as e:print('KRX direct access',str(e));(CACHE/'krx_response.txt').write_text(str(e),encoding='utf-8')
