"""Reproduce 11 figures from reviewed numeric inputs (no network access).

Python: pandas, matplotlib, Pillow. Use Malgun Gothic on Windows.
Values are financial/statistical facts, not extracted copyrighted page images.
"""
import json,csv,textwrap
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch
from PIL import Image,ImageOps,ImageDraw
ROOT=Path(__file__).resolve().parents[1];DATA=ROOT/'data';OUT=ROOT/'images';OUT.mkdir(exist_ok=True)
font=Path('C:/Windows/Fonts/malgun.ttf')
if font.exists():font_manager.fontManager.addfont(str(font));plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams.update({'axes.unicode_minus':False,'font.size':12,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'#faf8f3','axes.facecolor':'#faf8f3','savefig.facecolor':'#faf8f3','text.color':'#202b36','axes.labelcolor':'#202b36'})
BLUE='#25688d';RED='#bc4b3e';GRAY='#747d88';GOLD='#c58c2d';GREEN='#3f7e68';made=[]
def fig(title,sub='',size=(14,8)):
 f=plt.figure(figsize=size);f.suptitle(title,x=.07,y=.965,ha='left',fontsize=23,fontweight='bold');f.text(.07,.91,sub,fontsize=12,color=GRAY);return f
def save(f,name,note):
 f.text(.07,.035,note,fontsize=10,color=GRAY,va='bottom');f.savefig(OUT/name,dpi=160);plt.close(f);made.append(name)
def write_csv(name,rows):
 with (DATA/name).open('w',newline='',encoding='utf-8-sig') as f:
  w=csv.writer(f);w.writerows(rows)
def table(f,headers,rows,widths=None,position=(.07,.16,.86,.66),fs=11):
 ax=f.add_axes(position);ax.axis('off');t=ax.table(cellText=rows,colLabels=headers,colWidths=widths,cellLoc='left',loc='center',bbox=[0,0,1,1]);t.auto_set_font_size(False);t.set_fontsize(fs)
 for (r,c),cell in t.get_celld().items():
  cell.set_edgecolor('#ffffff');cell.PAD=.055;cell.set_facecolor('#e7ebed' if r%2 else '#f2f1ed')
  if r==0:cell.set_facecolor(BLUE);cell.get_text().set_color('white');cell.get_text().set_fontweight('bold')
 return t

# 1. Real GDP, same 1990=100 base; not household income.
wdi=pd.read_csv(DATA/'prewar_wdi.csv');g=wdi[wdi.indicator=='NY.GDP.MKTP.KD'].pivot(index='year',columns='country',values='value');idx=g.div(g.loc[1990]).mul(100)
idx.to_csv(DATA/'gdp_index_1990_100.csv',encoding='utf-8-sig')
names={'UKR':'우크라이나','POL':'폴란드','CZE':'체코','SVK':'슬로바키아','ROU':'루마니아','MDA':'몰도바','EST':'에스토니아','LVA':'라트비아','LTU':'리투아니아'}
f=fig('전면 침공 이전에도 회복하지 못한 총생산','실질 GDP 지수 · 1990=100 · 1990~2021 · 세계은행 WDI',size=(14,9));a=f.add_axes([.09,.24,.8,.60])
colors=['#25688d','#3f7e68','#c58c2d','#8e659d','#be805d','#4f8e9a','#788238','#b76a86']
for i,k in enumerate(sorted(names,key=lambda k:idx.loc[2021,k],reverse=True)):
 col=RED if k=='UKR' else colors[i%len(colors)];a.plot(idx.index,idx[k],label=f'{names[k]} {idx.loc[2021,k]:.1f}',color=col,lw=3.6 if k=='UKR' else 1.9)
a.axhline(100,color=GRAY,lw=.9,ls='--');a.set_xlim(1990,2021);a.set_ylabel('실질 GDP 지수');a.grid(axis='y',alpha=.2);a.legend(loc='upper center',bbox_to_anchor=(.5,-.13),ncol=5,frameon=False,fontsize=11)
save(f,'01_prewar_gdp.png','출처 [5] WDI NY.GDP.MKTP.KD, 2026.10.9 조회. GDP는 개인소득이 아님.\n1990년 전환경제 통계와 2014년 이후 영토·집계 범위 변화에 유의. 국가별 1990년 자체 기준으로 재계산.')

# 2. These are separate indicators, not parts of one total.
rows=[['상수도 관망','비상 상태',35,'2021','[6]'],['하수도 관망','비상 상태',38,'2021','[6]'],['식수','평균 손실률',36,'2021','[6]'],['화력발전 설비','설계 수명 소진',90,'2021','[7] 장관 발언'],['기관차','노후화 지표',95,'2020','[8] 보도']];write_csv('prewar_infrastructure.csv',[['대상','지표','비율_%','자료연도','출처']]+rows)
f=fig('시설 문제는 2022년에 처음 생긴 것이 아니다','각각 다른 지표 · 단위 % · 침공 이전 자료',size=(14,8));a=f.add_axes([.24,.19,.63,.61]);vals=[r[2] for r in rows];a.barh(range(5),vals,color=[BLUE,BLUE,BLUE,RED,RED],height=.6);a.set_yticks(range(5),[r[0]+'\n'+r[1] for r in rows]);a.invert_yaxis();a.set_xlim(0,105);a.set_xlabel('%');a.grid(axis='x',alpha=.15)
for i,v in enumerate(vals):a.text(v+1,i,f'{v}%',va='center',fontweight='bold')
save(f,'02_old_infrastructure.png','출처 [6] 2021년 내각 식수 프로그램, [7] 2021년 장관 발언, [8] 2020년 철도 보도.\n비상 상태·손실률·수명 소진·노후화는 다른 개념이며 합계나 국가 전체 비율로 사용할 수 없음.')

# 3. All 18 sectors, official rounded values; no summed fake total.
s=pd.DataFrame(json.loads((DATA/'rdna5_sectors.json').read_text(encoding='utf-8'))).sort_values('needs');s.to_csv(DATA/'rdna5_sectors.csv',index=False,encoding='utf-8-sig')
f=fig('필요액은 파괴된 자산의 가격과 다르다','RDNA5 18개 부문 · 단위 십억 달러 · 2025년 말 평가',size=(14,11));a=f.add_axes([.22,.15,.68,.68]);y=list(range(18));a.barh([i+.17 for i in y],s.damage,height=.31,color=GRAY,label='직접 피해');a.barh([i-.17 for i in y],s.needs,height=.31,color=BLUE,label='복구·재건 필요액');a.set_yticks(y,s.sector,fontsize=11);a.set_xlim(0,109);a.set_xlabel('십억 달러');a.legend(loc='lower right',frameon=False);a.grid(axis='x',alpha=.15)
for i,v in enumerate(s.needs):a.text(v+.8,i-.17,f'{v:.1f}',va='center',fontsize=10)
save(f,'03_rdna_sectors.png','출처 [2] RDNA5 표1. 직접 피해 총계 195.1, 필요액 총계 587.7. 부문 반올림값 합산은 공식 총계와 다를 수 있음.\n금융·폭발물 위험 부문의 피해 0.0은 반올림값. 직접 피해는 침공 전 가격, 필요액은 2025년 말 가격·개선 기준.')

# 4. Plans have incompatible scope; table, not misleading time-series bars.
rows=[['KSE 직접 피해','2022.6.13','95.5','그때까지의 물적 손상'],['루가노 회복계획','2022.7 / ~2032','750 이상','회복 + 현대화 + 국가개발'],['RDNA5 직접 피해','2025.12.31 평가','195.1','파괴·손상 자산 / 침공 전 대체가격'],['RDNA5 필요액','2026~2035','587.7','복구·서비스·개선 / 2025년 말 가격'],['Prosperity Plan','2026.1 발표 / 10년','800','성장·현대화 / 공공·민간 조달 구상']]
write_csv('plans_and_definitions.csv',[['지표','기간','십억달러','범위']]+rows);f=fig('7,500억 · 5,877억 · 8,000억은 같은 견적이 아니다','계획·평가의 범위와 시점 비교 · 금액 단위 십억 달러');table(f,['자료','기준·기간','금액','무엇을 계산했나'],rows,[.19,.24,.12,.45]);save(f,'04_plans_and_definitions.png','출처 [62] 루가노 원문, [64] KSE, [2] RDNA5, [3] 우크라이나 경제부.\n서로 다른 범위의 숫자를 더하거나 증가율·허위 청구액으로 계산하지 않음.')

# 5. No addition across currencies or across programme envelopes.
rows=[['RDNA5 2026 우선사업','152.45억 달러','필요액','2026.2 보고서'],['같은 우선사업 확보·확약','57.65억 달러','예산·확약 / 집행액 아님','2026.2 보고서'],['같은 우선사업 부족분','94.80억 달러','62% 재원 격차','2026.2 보고서'],['한국 EDCF 기본약정','최대 21억 달러','한도 / 사업별 계약 필요','2024.4'],['EDCF 개별 재정지원','1억 달러','차관 서명 / 건설 수주 아님','2024.10'],['EU 2026~2027 지원대출','900억 유로','차입·지원 틀 / 방위·예산','2025.12 결정 이후'],['EU 드론·미사일 지원','12.4억 유로','실제 집행 / 재건 공사 아님','2026.10.8']]
write_csv('funding_stages.csv',[['항목','금액','단계','기준일']]+rows);f=fig('약정과 계약, 집행은 다른 숫자다','금액은 각 통화 그대로 · 아래 항목은 중첩 가능하며 합산하지 않음',size=(14,9));table(f,['항목','금액','단계·의미','자료시점'],rows,[.29,.18,.34,.19],fs=11);save(f,'05_funding_stages.png','출처 [2] RDNA5, [18][19] EDCF 발표, [24][25][26] EU 결정·집행 공지.\n2026년 재원 격차는 2월 보고서 상태이며 10월 9일의 미집행 잔액이 아님.')

# 6. Dated, limited evidence of access and construction.
rows=[['2022.5.20','러시아 완전 통제 주장','AP 보도 [13]'],['2022.7.4~5','루가노 국가 회복계획','회복·현대화 구상 [62]'],['2022.7.6','한국에 마리우폴 재건 제안','의원·대사 면담 보도 [59]'],['2024.4 / 10','EDCF 한도 / 개별 차관','마리우폴 공사계약과 다름 [18][19]'],['2026.8.18','마리우폴 학교 공사 진행','러시아 시공사 자체 발표 [60]'],['2026.9','공동주택 복구 완료 사례','개별 시설 / 도시 전체 완료 아님 [60]'],['2026.10.9 확인 기준','한국의 해당 도시 공사대금','공개 계약·지급 근거 미확인']]
write_csv('mariupol_timeline.csv',[['시점','사건','확인범위']]+rows);f=fig('제안 당시에도 현장 접근과 지급 조건이 먼저였다','마리우폴 · 사실, 당사자 발표, 미확인을 구분',size=(14,9));table(f,['시점','사건','확인된 범위'],rows,[.2,.34,.46]);save(f,'06_mariupol_timeline.png','출처 [13][59][60][18][19]. 러시아 시공사 발표는 독립적인 도시 전체 준공 검증이 아님.\n마리우폴 제안과 한국 주가조작 사건의 정부 간 공모는 확인되지 않음.')

# 7. Provider-normalized index, not falsely certified KRX adjusted-close won.
d=pd.read_csv(DATA/'stock_001470_20230515_20230731.csv',dtype={'date':str});d['day']=pd.to_datetime(d.date);d['index']=d.close/d.close.iloc[0]*100;d[['date','close','index']].to_csv(DATA/'sambu_daily_index.csv',index=False,encoding='utf-8-sig')
f=fig('재건 기대가 먼저 움직인 주가','삼부토건 001470 · 일별 종가 재지수화 · 2023.5.15=100',size=(14,9));a=f.add_axes([.09,.22,.81,.61]);a.plot(d.day,d['index'],lw=3,color=RED);a.fill_between(d.day,d['index'],100,color=RED,alpha=.08);a.axhline(100,color=GRAY,lw=.8);a.set_ylim(75,610);a.set_ylabel('지수');a.grid(axis='y',alpha=.2)
for date,label,yv in [('2023-05-23','5.23 재건 관련 홍보 보도',555),('2023-07-15','7.15 대통령 우크라이나 방문',590)]:
 dt=pd.Timestamp(date);a.axvline(dt,color=GRAY,ls='--',lw=1);a.text(dt,yv,label,ha='right' if date.endswith('15') else 'left',fontsize=11,color=GRAY)
peak=d.loc[d.date=='20230717'].iloc[0];a.annotate(f"7.17 종가\n지수 {peak['index']:.1f} (+394.6%)",xy=(peak.day,peak['index']),xytext=(-155,-90),textcoords='offset points',arrowprops={'arrowstyle':'->','color':RED},fontsize=13,fontweight='bold');a.tick_params(axis='x',rotation=15)
save(f,'07_sambu_daily.png','출처 [70] 네이버 일별 제공 가격 / [66] 당시 종가 1,013→5,010원 보도. [67] 관련 홍보 혐의.\nKRX 원본 수정주가·감자 계수 독립 검증 미완. 사건 표시는 시간 관계이며 상승의 인과·기여분 추정이 아님.')

# 8. One window for all valid bases. Kukbo halted on base day.
r=json.loads((DATA/'korean_stocks_comparison.json').read_text(encoding='utf-8'));r=[x for x in r if x['code']!='001140'];nm={'001470':'삼부토건','010600':'웰바이오텍','317850':'대모','041440':'현대에버다임','039560':'다산네트웍스'}
f=fig('같은 기간으로 비교한 한국 재건 테마주','2023.5.15~7.17 · 단위 % · 최고는 장중 고가가 아닌 종가',size=(14,8));a=f.add_axes([.19,.19,.7,.61]);ys=list(range(5));a.barh([y-.17 for y in ys],[x['peak_return'] for x in r],height=.31,color=BLUE,label='구간 최고종가까지');a.barh([y+.17 for y in ys],[x['end_return'] for x in r],height=.31,color=GOLD,label='7.17 종가까지');a.set_yticks(ys,[nm[x['code']] for x in r]);a.invert_yaxis();a.set_xlim(0,450);a.legend(frameon=False,loc='lower right');a.grid(axis='x',alpha=.2);a.set_xlabel('기준일 대비 상승률 (%)')
for y,x in enumerate(r):
 for offset,key in [(-.17,'peak_return'),(.17,'end_return')]:a.text(x[key]+3,y+offset,f'{x[key]:.1f}%',va='center',fontsize=10)
save(f,'08_korean_stocks_comparison.png','출처 [70] 네이버금융. 제공 가격의 수정계수에 대한 KRX 독립 검증 미완. 국보는 5.15 거래량·시가 0으로 비교 제외.\n웰바이오텍 5.2~7.28 +225.1%와 다른 기간. 주가 상승은 회사 매출이나 매도자의 실현이익이 아님.')

# 9. Company proof and actual official ETF snapshot.
hold=pd.read_csv(DATA/'ukrn_holdings_20261008.csv');countries=(hold.groupby('country').weight.sum()*100).sort_values(ascending=False);countries.to_csv(DATA/'ukrn_countries_20261008.csv',header=['weight_percent'],encoding='utf-8-sig')
f=fig('과거 계약 · 현재 실적 · 금융상품은 다르다','공식 보유종목 2026.10.8 · 과거 계약·인수는 현재 수익성 증거가 아님',size=(14,11));rows=[['Ferrexpo','실제 광산·생산','2026 상반기 영업현금 -2,400만 달러'],['CRH / Buzzi','2024년 과거 자산 인수','매각대금 1억 유로 / 2026 회수 미확인'],['폴란드 3사','협력 MOU','2026.5 / 특정 공사 발주 확인 아님'],['Siemens / Naftogaz','협력·금융 검토 MOU','2026.10.5 / 수량·공급대금 미공개'],['AECOM','2023년 과거 자문 MOU','2025 10-K 재건매출 별도 미확인']];table(f,['대상','자료의 시점·단계','확인 범위와 빈칸'],rows,[.2,.25,.55],position=(.07,.50,.86,.31),fs=11)
other=countries.sum()-countries['United States']-countries['Ukraine']
a=f.add_axes([.14,.18,.74,.23]);a.barh(['기타 국가·현금','미국','우크라이나'],[other,countries['United States'],countries['Ukraine']],color=[GRAY,BLUE,RED]);a.set_xlim(0,65);a.set_xlabel('UKRN 국가 노출 (%)');a.grid(axis='x',alpha=.15)
for i,v in enumerate([other,countries['United States'],countries['Ukraine']]):a.text(v+.7,i,f'{v:.2f}%',va='center')
save(f,'09_global_market_cases.png','출처 [72][73][74][75][76][77][78]. 보유비중 합계 99.98%: 개별 반올림 영향. 과거 인수·MOU ≠ 현재 투자 회수.\nETF 국가 노출은 기업별 재건매출 비율이 아님. 낮은 비중만으로 사기 판정 불가.')

# 10. Monetary flow, with currencies and contingent sources kept separate.
f=fig('동결 원금 · 특별 수익 · 대출 · 배상은 다르다','2026.10.9 확인 기준 · 서로 더할 수 없는 재원·채무 구조',size=(14,9));a=f.add_axes([.06,.16,.88,.68]);a.set_xlim(0,10);a.set_ylim(0,7);a.axis('off')
def box(x,y,w,h,label,c=BLUE):
 a.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',facecolor=c,edgecolor='none'));a.text(x+w/2,y+h/2,label,ha='center',va='center',color='white',fontsize=13)
def arrow(x1,y1,x2,y2,label=''):
 a.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops={'arrowstyle':'->','color':GRAY,'lw':2});a.text((x1+x2)/2,(y1+y2)/2+.16,label,ha='center',fontsize=10,color=GRAY)
box(.2,5.4,3,1.0,'EU 내 CBR 자산 약 €210bn\n동결 ≠ 소유권 이전');box(6.6,5.4,3,1,'러시아의 배상 지급\n합의·일정 미확인',GRAY);a.text(5,5.85,'원금 몰수·장래 배상\n자동 연결 불가',ha='center',color=RED,fontsize=12)
box(.2,3,2.6,1.2,'동결 자산의\n특별 수익');box(3.7,3,2.7,1.2,'G7 ERA\n약 $50bn 대출');box(7.3,3,2.3,1.2,'우크라이나 지원');arrow(2.8,3.6,3.7,3.6,'상환 재원');arrow(6.4,3.6,7.3,3.6,'현재 대출')
box(.2,.5,2.6,1.4,'EU 시장 차입\nEU 예산 여력');box(3.7,.5,2.7,1.4,'2026~27 지원대출\n€90bn');box(7.3,.5,2.3,1.4,'방위 €60bn\n예산 €30bn');arrow(2.8,1.2,3.7,1.2,'보증·차입');arrow(6.4,1.2,7.3,1.2,'용도 구분');a.text(5,.07,'우크라이나 상환은 장래 러시아 배상에 연결 / EU의 시장 차입 의무는 별개',ha='center',fontsize=11,color=RED)
save(f,'10_russian_assets_flow.png','출처 [53] ERA, [24][25][26] EU 지원대출, [79][80][81][82] 자산·소송. bn=십억.\n10.8 실제 집행 €1.24bn은 드론·미사일용. 러시아 판결의 EU 자동 집행이나 EU의 유력한 패소를 가정하지 않음.')

# 11. Intentions vs conditional response vs populations with incompatible scope.
f=fig('귀환 수요와 운영할 인구는 별도로 계산해야 한다','UNHCR 2026.7 보고서 · 조사 2025.12~2026.1 · 의향은 귀환 실적이 아님',size=(14,9));a=f.add_axes([.10,.30,.34,.48]);b=f.add_axes([.58,.30,.34,.48]);a.bar(['2024 조사','2025말~2026초'],[61,49],color=[GRAY,BLUE],width=.55);b.bar(['영토 전체 회복','점령지 미회복'],[65,32],color=[GREEN,RED],width=.55)
for ax,vs in [(a,[61,49]),(b,[65,32])]:
 ax.set_ylim(0,85);ax.set_ylabel('%');ax.grid(axis='y',alpha=.2)
 for x,v in enumerate(vs):ax.text(x,v+2,f'{v}%',ha='center',fontsize=19,fontweight='bold')
a.set_title('귀환을 계획하거나 희망');b.set_title('조건별 귀환 가능성 높음');f.text(.08,.17,'2022.1 공식 인구 4,117만 (크림 제외)    |    2026.7 추정 2,900만 (정부 통제 지역)',fontsize=13);f.text(.08,.12,'영토·추정 방법이 달라 차액을 인구 소멸로 계산할 수 없음. 보고서 난민 약 580만 · 국내 실향민 약 380만.',fontsize=11,color=GRAY)
write_csv('population_and_return.csv',[['지표','값','단위','시점','범위'],['귀환계획·희망',61,'%',2024,'해외 난민 조사'],['귀환계획·희망',49,'%', '2025.12~2026.1','해외 난민 조사'],['전체영토회복 조건',65,'%', '2025.12~2026.1','조건별 가능성 응답'],['점령지미회복 조건',32,'%', '2025.12~2026.1','조건별 가능성 응답'],['공식인구',41.167,'백만명','2022.1','크림제외'],['전시추정인구',29,'백만명','2026.7','정부통제지역']])
save(f,'11_population_and_return.png','출처 [36] UNHCR Lives on Hold #7, [39] 인구연구소장 추정 보도, [52] 국가통계청.\n동일 응답자의 조건별 응답은 별개 실제 귀환집단이 아니며, 인구 추계의 범위 차이를 반드시 유지.')

# Contact sheet outside tracked images; inspect individual images if needed.
thumbs=[]
for name in made:
 im=Image.open(OUT/name).convert('RGB');im.thumbnail((720,600));tile=Image.new('RGB',(740,630),'white');tile.paste(im,((740-im.width)//2,18));ImageDraw.Draw(tile).text((12,604),name,fill='black');thumbs.append(tile)
sheet=Image.new('RGB',(2220,630*4),'#dddddd')
for i,im in enumerate(thumbs):sheet.paste(im,((i%3)*740,(i//3)*630))
sheet.save(ROOT/'.research-cache/chart_contact_sheet.jpg',quality=90)
(DATA/'chart_manifest.json').write_text(json.dumps({'as_of':'2026-10-09','charts':made,'price_limitation':'Naver series; original KRX adjustment factors not independently verified','population_scope_warning':True},ensure_ascii=False,indent=2),encoding='utf-8')
print('Generated',len(made),'figures; contact sheet in ignored cache')
