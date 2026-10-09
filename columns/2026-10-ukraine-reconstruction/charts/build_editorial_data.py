"""Build the source registry, audit and numeric chart inputs from reviewed sources.

The original source numbers are preserved. Access success is not verification.
"""
import json,re,subprocess
from pathlib import Path
from collect_sources import ROOT,DATA
original=subprocess.check_output(['git','show','ea55d09c43c4452235d2c71e861549dc2af3aa3f:columns/2026-10-ukraine-reconstruction/ukraine_reconstruction_critique.md'],cwd=ROOT,encoding='utf-8')
refs={}
for line in original.split('### 주요 출처')[1].splitlines():
 m=re.match(r'(\d+)\. (.+?)(https?://.+)',line)
 if m:refs[int(m[1])]={'title':m[2].strip(),'urls':[u.rstrip(').') for u in re.findall(r'https?://[^\s;]+',m[3])]}
from collect_extra import JOBS
new={
62:('URC22 회복계획 원문, p8·10·12', 'https://cdn.prod.website-files.com/621f88db25fbf24758792dd8/62c166751fcf41105380a733_NRC%20Ukraine%27s%20Recovery%20Plan%20blueprint_ENG.pdf'),
63:('UkraineInvest, 루가노 850개 사업과 단계(2022.7.15)',JOBS['ukrainvest_lugano']),64:('KSE, 2022.6.13 피해 추정과 국가 계획의 범위',JOBS['kse_2022']),
65:('삼부토건 반기보고서(2026.8.14), II.4 매출·수주','https://dart.fss.or.kr/report/viewer.do?rcpNo=20260814004299&dcmNo=11540645&eleId=13&offset=164355&length=24051&dtd=dart4.xsd'),
66:('일요신문, 삼부토건 2023년 당시 주가·매매 보도(2024.10.11)','https://www.ilyo.co.kr/?ac=article_view&entry_id=479842'),67:('뉴시스, 삼부토건 기소 내용·369억원 혐의(2025.9.26)',JOBS['sambu_indictment']),68:('머니투데이, 삼부토건 회생·감자(2026.6.29)',JOBS['sambu_rehab']),69:('조선비즈, 웰바이오텍 공소장 변경 신청(2026.3.11)',JOBS['well_correction']),
70:('네이버금융 일별 가격 API(2026.10.9 조회; KRX 수정계수 독립 검증 미완료)','https://api.finance.naver.com/siseJson.naver?symbol=001470&requestType=1&startTime=20230515&endTime=20230731&timeframe=day'),
71:('다산네트웍스 2023년 회사 발표·사업보고서','https://www.dasannetworks.com/sub/sub03_04.php?category=2023'),72:('Ferrexpo 2026년 중간 실적(2026.9.25)',JOBS['ferrexpo_2026']),73:('HANetf UKRN 공식 상품 페이지·보유종목 파일',JOBS['ukrn']),74:('폴란드 국유자산부, 3사 재건 협력 MOU(2026.5.15)',JOBS['poland_mou']),75:('Naftogaz, Siemens Energy MOU(2026.10.5)',JOBS['siemens_mou']),76:('Buzzi, 우크라이나 사업 매각 완료(2024.10.14)',JOBS['crh_buzzi']),77:('AECOM, 재건 인프라 자문 MOU(2023.6.20)',JOBS['aecom']),78:('AECOM 2025 Form 10-K','https://www.sec.gov/Archives/edgar/data/868857/000086885725000013/acm-20250930.htm'),79:('Euroclear 2026년 상반기 실적·법률 대응',JOBS['euroclear_h1']),80:('러시아 중앙은행, 모스크바 소송 발표(2025.12.12)',JOBS['cbr_moscow']),81:('러시아 중앙은행, EU 법원 제소 발표(2026.3.3)',JOBS['cbr_eu']),82:('EU 관보, 사건 T-150/26, 2026.4.13 공고','https://eur-lex.europa.eu/legal-content/EN/CASE/?uri=oj%3AC_202602053'),83:('Brussels Times/Belga, 브뤼셀 대응소송(2026.6.30)',JOBS['brussels_case']),84:('IFC, Elementum SII 49272; 2026.8.6 갱신',JOBS['elementum']),85:('EBRD, Ukrenergo PSD 55539(2025.12 승인)',JOBS['ukrenergo']),86:('EBRD, 기관차 계약·국제 금융지원(2025)',JOBS['uz_alstom']),87:('우크라이나 PPP Agency, M15 예비타당성 조사(2026.6.17)',JOBS['m15']),88:('EBRD, 헤르손 항만 양허(2020)',JOBS['kherson_port']),89:('EIB, 미콜라이우·드니프로 집행(2024.11.19)',JOBS['mykolaiv']),90:('EBRD, M10 리비우 산업단지 투자(2023)',JOBS['m10']),91:('UkraineInvest, M10 1단계 개장(2024.2.27)',JOBS['m10_open']),92:('NABU, 미다스 최초 혐의 발표(2025.11.11)',JOBS['midas_original']),93:('NABU, 미다스 추가 혐의(2026.7.10)',JOBS['midas_update']),94:('UBS, 유럽 투자 주제·재건(2025.3.11)','https://www.ubs.com/us/en/wealth-management/insights/article.1997555.html'),95:('한국일보, 삼부토건 사건 재판 진행(2026.7.24)',JOBS['trial_latest']),96:('KRX 기타시장안내, 삼부토건(2026.8.31)','https://dart.fss.or.kr/report/viewer.do?rcpNo=20260831800966&dcmNo=11561863&eleId=0&offset=0&length=0&dtd=HTML'),97:('KRX 웰바이오텍 상장폐지 공고 재게재, 2026.1.26 폐지','https://stock.mk.co.kr/news/disclosure/template/855739'),98:('국보 상장폐지 보도(2026.1.23)','https://v.daum.net/v/20260123105034883'),99:('Ferrexpo 주가의 종전 기대 반응 보도(2024.11.6)','https://www.proactiveinvestors.co.uk/companies/news/1059984/ferrexpo-shares-spike-as-trump-win-lifts-hopes-for-end-to-ukraine-war-1059984.html'),100:('SEC Form 4, Troy Rudd/AECOM 매수(2026.5.14)','https://www.sec.gov/Archives/edgar/data/1653811/000165381126000002/xslF345X03/wk-form4_1778788962.xml'),101:('AP, 러시아 법원 Euroclear 사건 판단(2026.5.15)','https://apnews.com/article/85750e45d2da06168a72aeb8f41ec53b'),102:('삼부토건 2026년 1분기보고서',JOBS['sambu_q1'])}
for n,(title,url) in new.items():refs[n]={'title':title,'urls':[url]}
refs[103]={'title':'Ferrexpo 이벤트 시점 주가 보도: 2024.11·2025.2·2025.5 (거래소 수정시세 인증 아님)','urls':['https://www.itiger.com/news/2481271136','https://good-time-invest.com/blog/ukrainian-companies-shares-on-the-rise-amid-prospects-of-wars-end/','https://www.lse.co.uk/news/ftse-100-movers-ferrexpo-gains-on-ukraine-minerals-deal-clarkson-tanks-tjh707hpuvbdjxg.html']}
refs[104]={'title':'우크라이나 복구청 Bechtel MOU(2023.6.23)·Bechtel 체르노빌 실제 사업','urls':['https://restoration.gov.ua/blog/agentstvo-vidnovlennya-spivpraczyuvatyme-z-liderom-u-sferi-inzhyniryngu-ta-budivnycztva-korporacziyeyu-bechtel/','https://www.bechtel.com/projects/chornobyl-new-safe-confinement/']}
refs[105]={'title':'KRX, 삼부토건 기업심사위원회 심의대상 결정(2026.9.21)','urls':['https://dart.fss.or.kr/report/viewer.do?rcpNo=20260921800376&dcmNo=11587021&eleId=0&offset=0&length=0&dtd=HTML']}
refs[106]={'title':'우크라이나 개발부, 올비야 국영기업 2026년 계획(2025.7.25 승인), pp2~3: 헤르손 자산 접근 조건','urls':['https://mindev.gov.ua/storage/app/sites/1/uploaded-files/list-ocikuvan-vlasnika-dp-sk-olviia-2026.pdf']}
refs[107]={'title':'Dragon Capital, M10 2단계 건설·1단계 가동·공적 지분과 보증 발표(2026.3.30)','urls':['https://dragon-capital.com/media/press-releases/dragon-capital-launches-construction-of-phase-ii-of-m10-lviv-industrial-park/']}
refs[108]={'title':'Dragon Capital, 전쟁 격화와 추가 조달 필요에 관한 2026~27년 전망 갱신(2026.10.8)','urls':['https://dragon-capital.com/media/press-releases/onovleniy-makroprognoz-na-2026-2027-roki-ekonomichni-naslidki-posilennya-atak/']}
refs[5]={'title':'세계은행 WDI; 1990~2021, 2026.10.9 조회','urls':['https://api.worldbank.org/v2/country/UKR;POL;CZE;SVK;ROU;MDA;EST;LVA;LTU/indicator/NY.GDP.MKTP.KD?format=json&date=1990:2021&per_page=20000']}
refs[73]['urls'] += [JOBS['ukrn_holdings'],JOBS['ukrn_factsheet']]
refs[70]['urls'] += [f'https://api.finance.naver.com/siseJson.naver?symbol={code}&requestType=1&startTime=20230515&endTime=20261008&timeframe=day' for code in ['317850','041440','039560']]
refs[71]['urls'] += ['https://www.dasannetworks.com/','https://kind.krx.co.kr/external/2024/03/21/001479/20240321005920/11011.htm']
refs[22]['urls'] += [JOBS['korea_kiep']]
(DATA/'source_registry.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2),encoding='utf-8')
p=ROOT/'ukraine_reconstruction_critique.md';s=p.read_text(encoding='utf-8');s=s.replace('진행 중인 해외사업이 없다고 명시했다.[64][65]','진행 중인 해외사업이 없다고 명시했다.[102][65]')
used=sorted({int(n) for n in re.findall(r'\[(\d+)\]',s.split('### 출처')[0])});lines=[]
for n in used:
 r=refs[n];lines.append(f"- **[{n}]** {r['title']}: "+' · '.join(f'[원문{j+1}]({u})' for j,u in enumerate(r['urls'])))
s=s.split('### 출처')[0]+'### 출처\n\n'+'\n'.join(lines)+'\n';p.write_text(s,encoding='utf-8')

sectors=[('주택',61.1,25,89.8),('교육',13.9,11.7,33.5),('보건',1.8,23.1,23.6),('사회보호',.5,18.6,42.7),('문화·관광',4.5,31.9,11.5),('에너지',24.8,88.2,90.6),('교통',40.3,58.9,96.3),('통신·디지털·미디어',2.5,2.7,7.1),('상하수도',7.8,14.4,17.5),('도시서비스',3.1,8,7.4),('농업',12.1,78,55.3),('상공업',19.2,232.9,63.3),('관개·수자원',.9,1.3,12.5),('금융·은행',0,5.2,2.1),('환경·산림',2,36,3.1),('긴급대응·민방위',.4,.8,2.7),('사법·공공행정',.5,3.3,1),('폭발물 위험 관리',0,26.7,27.6)]
(DATA/'rdna5_sectors.json').write_text(json.dumps([dict(sector=a,damage=b,loss=c,needs=d,gap=round(d-b,1)) for a,b,c,d in sectors],ensure_ascii=False,indent=2),encoding='utf-8')
print('Body chars',len(s.split('### 출처')[0]),'references used',len(used),'registry',len(refs),'sectors',len(sectors))
