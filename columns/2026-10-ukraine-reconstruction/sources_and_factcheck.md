# 출처와 팩트체크 — 2026년 10월 9일 기준

기존 원고의 **61개 출처 번호 전부**를 아래에서 판정했다. 번호 하나에 여러 URL이 있는 경우 실제 접근 기록은 64개다. HTTP 성공은 원문 접근의 결과이고 주장 검증은 별도다. 접근 기록 원본은 [JSON](data/original_source_access_audit.json), 수치·추가 출처는 [데이터 폴더](data/)에 있다.

판정은 `확인 / 일부 확인 / 당사자 주장 / 수사기관 혐의 / 추정 / 미확인 / 반증 또는 수정 필요`로 구분했다. `확인`도 공개 자료의 해당 범위에 대한 판정이며 미래 성과나 기업 내부 모형까지 검증했다는 의미가 아니다. 자동화 수집 중 차단된 자료를 웹 도구로 읽은 경우 경로를 구분했다. PDF·기사 전문은 로컬 캐시에만 보관하고 Git에 올리지 않는다.

## 기존 61개 출처 감사

|번호|검증대상|판정|원문·위치|확인 범위·한계|본문 처리|직접 수집 결과|
|---:|---|---|---|---|---|
|1|RDNA5 피해·손실·필요 총액|확인|[원문1](https://www.worldbank.org/en/news/press-release/2026/02/23/updated-ukraine-recovery-and-reconstruction-needs-assessment-released)|2026.2.23 발표; 195.1/666.7/587.7 십억 달러|유지; 서로 합산 금지|200 / 11,761자|
|2|18부문·방법론·2026 재원 격차|확인|[원문1](https://documents1.worldbank.org/curated/en/099022026094036395/pdf/P514499-22f93f3a-4278-42bc-b907-db9553d12069.pdf)|표1·그림7·표5 및 부록. 손실기간 설명에 내부 문구 불일치|표 주석의 46개월 실제+18개월 전망=64개월 적용; 확보≠집행|200 / 187,726자|
|3|8,000억 달러 Prosperity Plan|당사자 주장|[원문1](https://me.gov.ua/News/Detail/a39127c6-0df8-4880-b795-74150fd0c278?isSpecial=true&lang=uk-UA&title=UkraineProsperityPlan)|2026.1.3 정부 발표; 국가 현대화 계획임을 확인|지급 약속·RDNA 잔액과 구별|200 / 3,576자|
|4|침공 전 저투자·국가 포획|확인|[원문1](https://www.worldbank.org/en/brief/2021/09/06/scd-consultations) · [원문2](https://thedocs.worldbank.org/en/doc/76b8952cdeee76b061cb9ced4baaee80-0080062021/original/Ukraine-SCD-2021-en.pdf)|2021 SCD 본문; 진단은 전쟁 이전|제도적 문제 사용; GDP 차이 전부의 단일 원인으로 단정 안 함|200 / 6,977자; 200 / 178,203자|
|5|1990~2021 GDP·2021 투자율|확인|[원문1](https://api.worldbank.org/v2/country/UKR;POL;CZE;SVK;ROU;MDA;EST;LVA;LTU/indicator/NY.GDP.MKTP.KD?format=json&date=1990:2021&per_page=20000)|국가 페이지 대신 WDI API 3지표·9개국 CSV 재계산|UKR 62.9, GDPpc $4,775.95, 고정자본 13.2048%; 개인소득과 구별|200 / 7,899자|
|6|상수35%·하수38% 비상, 식수손실36%|일부 확인|[원문1](https://zakon.rada.gov.ua/laws/show/388-2021-р)|공식 Rada 검색 색인 원문 문장 확인; 본문 직접 접근 실패|출처·접근 한계 명시; 국가 시설 전체의 노후비율로 쓰지 않음|실패 / 0자|
|7|화력발전 설비90% 수명 소진|당사자 주장|[원문1](https://zn.ua/ECONOMICS/v-ukraine-90-enerhoblokov-tes-otrabotali-svoj-resurs-halushchenko.html)|2021.6.18 ZN 장관 인터뷰|장관 발언으로만 사용|200 / 8,164자|
|8|기관차 노후95%|일부 확인|[원문1](https://gmk.center/?p=32065)|2020.10 GMK 업계 보도; UZ 기초통계 전수 미확보|기관차 대상임을 유지; 철도망 전체로 확대 안 함|200 / 4,679자|
|9|CPI2021 32점·122위|미확인|[원문1](https://ti-ukraine.org/en/news/no-progress-ukraine-s-result-in-the-corruption-perceptions-index-2021/)|기존 TI 링크 직접 403; 이번 판의 원자료 재확인 미완|사용하지 않음; 2025 공식 자료 별도 검토|실패 / 0자|
|10|취약국가지수2021 순위|미확인|[원문1](https://fragilestatesindex.org/)|링크는 홈페이지이며 해당 연도 데이터·산식 미확보|삭제; 홈페이지 HTTP200을 통계 검증으로 취급 안 함|200 / 972자|
|11|2021 일반정부부채 비율|미확인|[원문1](https://www.imf.org/external/datamapper/)|IMF 일반 홈페이지로 정확한 조회계열 미확보|본문은 MoF 정부채무/정부보증채무의 2025 지표로 교체|실패 / 0자|
|12|국토부 마리우폴 재건 면담|일부 확인|[원문1](https://www.molit.go.kr/USR/NEWS/m_72/dtl.jsp?id=95086933)|기존 정부 링크 반복 리디렉션; 국토부 인용 전자신문[59]로 교차확인|정부 원문 직접 확보라고 표기하지 않음|실패 / 0자|
|13|2022.5.20 마리우폴 통제|일부 확인|[원문1](https://triblive.com/news/world/russia-claims-to-have-taken-full-control-of-mariupol)|AP 기사의 재게재·아카이브 접근; 당시 러시아 발표를 보도|7월 제안의 현장 접근 조건에 사용|200 / 9,931자|
|14|2022.10 합병 관련 UN 표결|확인|[원문1](https://www.aljazeera.com/news/2022/10/12/un-condemns-russias-move-to-annex-parts-of-ukraine)|기사에서 사건 확인; 사업성 논점과 별개|장황한 영토·법률 설명 삭제|200 / 5,182자|
|15|러시아 점령 마리우폴의 변화|일부 확인|[원문1](https://www.sanjuandailystar.com/post/russian-occupied-mariupol-everything-ukrainian-must-go)|NYT 재게재 기사이지 본래 NYT 원문 직접 확인은 아님|도시 전체 복구 완료의 증거로 사용 안 함|200 / 8,963자|
|16|아파트900채 압류|당사자 주장|[원문1](https://euromaidanpress.com/2026/05/13/russia-seizes-900-mariupol-apartments-from-owners-it-forced-to-flee/)|2026.5.13 망명 시의회 발표를 인용한 보도|전수 등기 확인 아님을 적고 소유·이용 불확실성에만 사용|200 / 8,516자|
|17|2023 한국23억달러 지원 발표|일부 확인|[원문1](https://www.koreatimes.co.kr/foreignaffairs/20230910/seoul-pledges-23-bil-aid-package-to-rebuild-ukraine)|당시 언론 기사; 발표 단계|총 집행이나 추가 수주액으로 합산하지 않음|200 / 6,630자|
|18|EDCF 최대21억달러 기본약정|확인|[원문1](https://www.kmu.gov.ua/en/news/ukraina-otrymaie-mozhlyvist-zaluchaty-kredytni-resursy-zahalnym-obsiahom-do-21-mlrd-vid-pivdennoi-korei-uriady-krain-pidpysaly-vidpovidnu-uhodu)|2024.4.19 내각 원문; 2024~2029 한도|약정 한도·개별 계약 구별|200 / 10,180자|
|19|EDCF 개별1억달러 차관|확인|[원문1](https://www.kmu.gov.ua/en/news/ukraina-vpershe-otrymaie-pilhove-finansuvannia-vid-respubliky-koreia-serhii-marchenko-pidpysav-kredytnyi-dohovir-na-100-mln-dolariv-ssha)|2024.10.2 내각:20년·1%·재정지원 계약|계약 서명 확인, 집행 전액/건설수주로 변경 금지|200 / 9,505자|
|20|철도차량20편성 한국 협력|당사자 주장|[원문1](https://mindev.gov.ua/en/news/spivpratsia-z-koreiskymy-kompaniiamy-posylyt-stiikist-ukrainskoi-zaliznytsi-oleksii-kuleba)|2025.9.17 부처 발표, 차관 요청·협력 단계|최종 공급자·수주 확정으로 사용 안 함|200 / 7,976자|
|21|보리스필 공항9.83억달러|일부 확인|[원문1](https://www.koreajoongangdaily.com/business/kac-hyundai-ec-ink-983m-deal-to-revamp-kyiv-intl-airport/11017714)|2023.11 기사에 MOU로 명시|사업 규모와 확정 계약액 구별|200 / 5,238자|
|22|기업 참여에 재원·수익 정보 부족|확인|[원문1](https://eiec.kdi.re.kr/policy/domesticView.do?ac=0000189716) · [원문2](https://www.kiep.kr/galleryDownload.es?bid=0001&list_no=11547&seq=1)|KIEP 보고서 PDF 직접 확보; 인터뷰·제도 검토|참여 애로의 증거; 모든 프로젝트에 FS가 없다는 근거는 아님|200 / 5,328자|
|23|EU Facility500억유로|확인|[원문1](https://enlargement.ec.europa.eu/funding-technical-assistance/ukraine-facility_en)|2024~27 공식 지원 구조; 보조금·대출·보증·기술지원 혼합|총액 전부를 건설 보조금으로 쓰지 않음|200 / 15,373자|
|24|EU900억유로 대출 결정|확인|[원문1](https://www.eeas.europa.eu/delegations/ukraine/european-council-18-december-2025-ukraine_en)|2025.12.18 정상회의, 시장차입·EU예산 여력·러시아 배상 연계|ERA와 분리해 사용|200 / 13,055자|
|25|우크라이나의 EU대출 환영|당사자 주장|[원문1](https://www.kmu.gov.ua/en/news/minfin-vitaie-rishennia-rady-ies-shchodo-namiru-nadaty-ukraini-90-mlrd-ievro-finansovoi-dopomohy-na-2026-2027-roky)|2025.12.19 내각 설명|지급 구조는 EU[24][26]와 교차검증|200 / 9,751자|
|26|2026.10.8 12.4억유로 집행|확인|[원문1](https://defence-industry-space.ec.europa.eu/commission-disburses-eur124-billion-ukraine-drones-and-missiles-2026-10-08_en)|EU DG DEFIS 공식 공지; 드론·미사일 용도|최신 실제 집행 포함; 주택·도로 예산으로 둔갑 금지|200 / 5,945자|
|27|IMF 신규81억달러 EFF|일부 확인|[원문1](https://www.imf.org/en/news/articles/2026/02/26/pr-26066-ukraine-imf-executive-board-approves-usd-8point1-billion-under-an-eff-arrangement)|IMF 직접403; 정부 발표[28]로 내용 교차확인|IMF 원문을 직접 모두 읽었다고 주장 안 함|실패 / 0자|
|28|IMF 48개월·1365억달러 금융수요|당사자 주장|[원문1](https://www.kmu.gov.ua/en/news/minfin-rada-vykonavchykh-dyrektoriv-mvf-skhvalyla-novu-prohramu-rozshyrenoho-finansuvannia-dlia-ukrainy-u-rozmiri-81-mlrd)|2026.2.27 재무부 발표|거시·재정 지원, 재건 총액을 채우는 별도 공사기금 아님|200 / 11,538자|
|29|미·우크라이나 기금 첫 투자|반증 또는 수정 필요|[원문1](https://home.treasury.gov/news/press-releases/sb0424)|미 재무부 발표의 Swarmer는 방산·드론 기술 투자|미국 건설기업 재건매출의 증거에서 제외|200 / 12,377자|
|30|Donor Platform 지원 정보|일부 확인|[원문1](https://ukrainedonorplatform.com/?p=20326)|2026.7 뉴스레터의 프로그램 설명|국가별 전체 순집행 통계가 아니므로 총 지원액으로 계산 안 함|200 / 6,400자|
|31|2024 유로본드 재조정|확인|[원문1](https://www.kmu.gov.ua/en/news/ukraina-zavershyla-restrukturyzatsiiu-derzhavnykh-oblihatsii-ta-harantovanykh-derzhavoiu-ievrooblihatsii-na-sumu-205-mlrd-dolariv-ssha)|정부 공식 발표:원금20.5bn, 이자 포함 기준의37% 감액|원금 단독 기준37%로 오표기 금지; 채무 소멸 아님|200 / 10,602자|
|32|S&P CCC+|일부 확인|[원문1](https://finance.liga.net/en/ekonomika/novosti/sp-upgrades-ukraines-credit-rating-to-ccc-after-debt-restructuring)|언론 기사; MoF2025보고서 2026.3말 평정과 교차확인|상환 가능의 보증으로 사용 안 함|200 / 5,797자|
|33|2025 예산·정부채무|반증 또는 수정 필요|[원문1](https://mof.gov.ua/storage/files/ENG_Report_on_State_Debt_and_State-Guaranteed_Debt_Management_Results_for_2025.pdf)|MoF PDF 웹 본문 직접 검토; 다운로드403과 별개. pp2~3,26~27|98.2%는 정부채무만; 보증 포함101.3%, ERA제외91.1%로 정정|실패 / 0자|
|34|부차 비용·에너지·회수기간|확인|[원문1](https://en.ecoaction.org.ua/wp-content/uploads/2024/03/Executive_Summary_The_Green_Reconstruction_of_the_Residential_Sector.pdf)|3쪽 연구 요약 PDF:기본106m+추가108/212m유로|총214/318m, 현행27/33.6년 vs 원가요금15.3/19.4년; 단순 회수 모형|200 / 8,004자|
|35|분산형 전력 필요·운영 조건|일부 확인|[원문1](https://www.iea.org/reports/empowering-ukraine-through-a-decentralised-electricity-system)|IEA 페이지 자동 접근403; 이번 판 상세 계산 재확인 미완|개별 IFC·EBRD 공개 사업으로 교체|실패 / 0자|
|36|난민귀환49%·조건별65/32%|확인|[원문1](https://data.unhcr.org/en/documents/download/123284)|UNHCR PDF 직접 검토, 본문·방법론|보고2026.7/조사2025.12~2026.1 구별; 표본 수 요약·부록 차이로 N단정 제외|200 / 70,483자|
|37|EU 임시보호443만|일부 확인|[원문1](https://www.eunews.it/en/2026/09/10/eurostat-4-43-million-ukrainians-under-temporary-protection-in-the-eu-in-july-2026/)|Eurostat 인용 매체 기사이지 Eurostat 원자료 직접 확보 아님|중복 숫자 삭제; UNHCR 난민·실향민 수치 사용|200 / 6,423자|
|38|임시보호2028.3 연장|확인|[원문1](https://www.eeas.europa.eu/delegations/ukraine/eu-countries-agree-extend-temporary-protection-those-fleeing-ukraine-until-march-2028_en)|EEAS 공식 발표의 해당 기간|본문 축소 과정에서 제외; 인구의 영구 이탈로 간주 안 함|200 / 6,039자|
|39|통제지역 인구2900만|당사자 주장|[원문1](https://en.interfax.com.ua/news/general/1186657.html)|2026.7.20 연구소장 인터뷰; 추정오차 약30만|2022 전역 추계와 범위 차이 명시|200 / 7,090자|
|40|2025 출생·사망등록|미확인|[원문1](https://opendatabot.ua/en/analytics/birth-death-2025-12)|Opendatabot 원문403; 이번 판 원자료 직접 재검증 미완|정확한 원자료 없이 사용하지 않음|실패 / 0자|
|41|취업1070만·연금1020만|반증 또는 수정 필요|[원문1](https://kse.ua/about-the-school/news/human-capital-trends-in-ukraine-make-reforms-of-the-labour-market-social-benefits-system-and-education-funding-key-priorities-for-2026-human-capital-chartbook-kse-institute/)|KSE 본문에 취업연금자280만 중첩|두 집단 독립 합계/개인 부양비율 계산 금지|200 / 6,492자|
|42|2026.1 점령비율|일부 확인|[원문1](https://news.online.ua/en/deepstate-calculated-the-area-of-ukraine-occupied-by-the-russian-federation-in-2025-900209/)|DeepState 인용 기사; 지도 원데이터 재현 미완|10월 현재 점령비율로 사용 안 함; 현재 수주가능액 계산 제외|200 / 4,352자|
|43|도시 재건·공간배분|확인|[원문1](https://www.nber.org/papers/w34598)|NBER WP34598의 연구 요지|시나리오 분석이며 정책의 실측 성과·귀환 예측 아님|200 / 7,065자|
|44|미다스 전직 장관 혐의|수사기관 혐의|[원문1](https://euromaidanpress.com/2026/02/16/ukraine-ex-energy-minister-halushchenko-charged-midas/)|언론 기사; NABU[92][93]로 직접 출처 보강|확정 유죄·RDNA전체 도난 비율로 바꾸지 않음|200 / 12,477자|
|45|NABU 독립성 복원|일부 확인|[원문1](https://ukranews.com/en/news/1097057-zelenskyy-signs-law-on-restoring-independence-of-nabu-and-sapo)|원링크403; TI2025 공식평가에서 후퇴·복원 맥락 확인|부패 단락의 반복 서사 줄이고 실제 거래위험 사용|실패 / 0자|
|46|CPI2025 36점·104위|확인|[원문1](https://ti-ukraine.org/en/research/corruption-perceptions-index-2025/)|TI 공식 검색·웹 본문 확인. 평가기간2023.1~2025.9|미다스2025.11 반영하지 않는 시차 명시|실패 / 0자|
|47|EU 분할금 축소|일부 확인|[원문1](https://kyivindependent.com/eu-cuts-next-ukraine-facility-aid-tranche-over-delayed-reforms/)|기사의 개혁 미이행·지급 삭감 설명|감액·유보·최종 지원 철회 구별 불충분해 본문 숫자 제외|200 / 8,379자|
|48|800bn 계획의 구성|일부 확인|[원문1](https://kyivindependent.com/what-we-know-about-ukraines-800-billion-economic-peace-plan/)|Kyiv Independent의 정부 계획 보도|원문 정부[3]를 주출처로 사용; 확정 지원액이라고 쓰지 않음|200 / 9,875자|
|49|Prosperity초안·136.5bn|일부 확인|[원문1](https://www.pravda.com.ua/eng/news/2026/01/23/8017583/)|보도된 초안이며 협정 체결 원문이 아님|공식발표[3][28]와 구별; 초안 전부 확정 조건으로 쓰지 않음|200 / 5,553자|
|50|지역후원 모델 폐기|일부 확인|[원문1](https://www.kyivpost.com/post/29917)|Kyiv Post 기사, 당시 방안의 조정|모든 지방사업 전면 취소의 근거로 확대 안 함; 본문 제외|200 / 10,093자|
|51|CES 난민5차 조사|확인|[원문1](https://ces.org.ua/en/ukrainian-refugees-fifth-wave/)|조사 발표 원문; UNHCR과 모집·문항·시점 다름|일관된 본문 비교는 UNHCR[36] 사용; 수치 혼합 안 함|200 / 10,433자|
|52|2022.1 공식 인구4117만|확인|[원문1](https://lv.ukrstat.gov.ua/ukr/help/pb_fig2021/en/chapter_2_1.html)|국가통계청 표, 크림 제외|2026 통제지역 추정과 차액 계산 금지|200 / 5,567자|
|53|G7 ERA50bn 구조|확인|[원문1](https://economy-finance.ec.europa.eu/international-economic-relations/candidate-and-neighbouring-countries/ukraine_en)|EU 공식 개요:특별수익 기반 대출|원금 몰수·러시아 배상합의·EU90bn과 분리|200 / 26,108자|
|54|2026상반기 사망/출생 약4배|일부 확인|[원문1](https://zmina.info/en/news-en/ukraines-mortality-rate-exceeds-birth-rate-fourfold/)|2026 상반기 등록 통계 인용 기사; 2025연간과 다른 기간|2025 비율에4배를 붙이지 않음; 본문에서는 제외|200 / 6,704자|
|55|출산율0.9|당사자 주장|[원문1](https://english.nv.ua/nation/ukraine-s-birth-rate-hits-record-low-50494770.html)|차관 발언을 인용한 기사; 전시 분모 추정 불확실|등록 출생수와 출산율 혼동을 피하려 본문 제외|200 / 3,523자|
|56|IFC73bn/18% vs130bn/약1/3|확인|[원문1](https://www.ifc.org/en/insights-reports/2023/private-sector-opportunities-for-a-green-and-resilient-reconstruction-in-ukraine)|IFC 본문, RDNA2 411bn 기준; 추가282bn개발 별도|조건부 시나리오; 현재 약정·RDNA5 확정조달로 사용 금지|200 / 5,964자|
|57|FIRST30m유로|확인|[원문1](https://www.eib.org/en/press/all/2025-285-ukraine-to-rebuild-infrastructure-with-support-from-ukraine-first-initiative)|EIB2025.7.11:사업 준비·타당성 지원 초기자금|건설공사계약·모든 조사 완료와 구별|200 / 11,657자|
|58|한국 간접155mm 포탄 공급|일부 확인|[원문1](https://m-en.yna.co.kr/view/AEN20231205000300315)|연합뉴스의 WP 취재 인용; 공식 확정 총량·경로 미공개|큰 기여를 인정; 직접 무상제공 수량이나 현금원조로 합산 금지|200 / 4,336자|
|59|2022.7.6 마리우폴 제안|일부 확인|[원문1](https://www.etnews.com/20220706000197)|국토부 발표 인용 전자신문 원문; 의원2명·대사 이름 확인|면담 확인; 유상 공사계약의 증거 아님|200 / 3,315자|
|60|러시아의 마리우폴 복구|당사자 주장|[원문1](https://rks-nr.ru/news/273/) · [원문2](https://rks-nr.ru/news/)|시공사 개별 공동주택 준공·학교 진행 공지|개별 복구는 인정; 도시 전체 완료 주장 수정|200 / 1,871자; 200 / 23,876자|
|61|한국의 지원 분야|확인|[원문1](https://www.mofa.go.kr/www/brd/m_4080/view.do?page=1&pitem=102026&seq=375100)|외교부2024.6.13 원문; 인도지원·IFI·KOICA|기간·단계가 다른 항목을 전액 집행 총액으로 합산 안 함|200 / 3,576자|

## 새로 추가한 핵심 자료와 판정

|번호|자료·주장|판정|원문·위치|확인 범위|본문 처리|한계·시점|
|---:|---|---|---|---|---|
|62|URC22 회복계획 원문, p8·10·12|확인|[원문1](https://cdn.prod.website-files.com/621f88db25fbf24758792dd8/62c166751fcf41105380a733_NRC%20Ukraine%27s%20Recovery%20Plan%20blueprint_ENG.pdf)|원문자료의 공개된 범위 확인|계획·손상·자금 구분|기준일은 자료 제목 참조|
|63|UkraineInvest, 루가노 850개 사업과 단계(2022.7.15)|확인|[원문1](https://ukraineinvest.gov.ua/en/news/15-07-22-2/)|원문자료의 공개된 범위 확인|계획·손상·자금 구분|기준일은 자료 제목 참조|
|64|KSE, 2022.6.13 피해 추정과 국가 계획의 범위|확인|[원문1](https://kse.ua/russia-will-pay/)|원문자료의 공개된 범위 확인|계획·손상·자금 구분|기준일은 자료 제목 참조|
|65|삼부토건 반기보고서(2026.8.14), II.4 매출·수주|확인|[원문1](https://dart.fss.or.kr/report/viewer.do?rcpNo=20260814004299&dcmNo=11540645&eleId=13&offset=164355&length=24051&dtd=dart4.xsd)|해외사업0%, 국내37,677,137천원+기타50,580천원|반기 매출 약377억원, 우크라이나 주요계약 미확인|2026.6말 / 8.14 공시|
|66|일요신문, 삼부토건 2023년 당시 주가·매매 보도(2024.10.11)|일부 확인|[원문1](https://www.ilyo.co.kr/?ac=article_view&entry_id=479842)|역사적 가격·매매 보도|네이버 재지수화 비율과 교차확인|KRX 원본 인증 아님|
|67|뉴시스, 삼부토건 기소 내용·369억원 혐의(2025.9.26)|수사기관 혐의|[원문1](https://mobile.newsis.com/view_amp.html?ar_id=NISX20250926_0003345388)|기소 내용을 인용한 뉴스,369억원|영업이익과 구별|공소장 원본·확정판결 미확보|
|68|머니투데이, 삼부토건 회생·감자(2026.6.29)|일부 확인|[원문1](https://www.mt.co.kr/amp/stock/2026/06/29/2026062916314035715)|회생계획·감자 보도|과거와 현재 주가 직접 비교 제외|전체 수정계수 미확보|
|69|조선비즈, 웰바이오텍 공소장 변경 신청(2026.3.11)|수사기관 혐의|[원문1](https://v.daum.net/v/VxCmJt4qcf)|302→215억원 공소장 변경 신청 보도|최초 수치 교체; 유죄 확정액 아님|2026.3.10 신청 / 3.11 보도|
|70|네이버금융 일별 가격 API(2026.10.9 조회; KRX 수정계수 독립 검증 미완료)|일부 확인|[원문1](https://api.finance.naver.com/siseJson.naver?symbol=001470&requestType=1&startTime=20230515&endTime=20230731&timeframe=day) · [원문2](https://api.finance.naver.com/siseJson.naver?symbol=317850&requestType=1&startTime=20230515&endTime=20261008&timeframe=day) · [원문3](https://api.finance.naver.com/siseJson.naver?symbol=041440&requestType=1&startTime=20230515&endTime=20261008&timeframe=day) · [원문4](https://api.finance.naver.com/siseJson.naver?symbol=039560&requestType=1&startTime=20230515&endTime=20261008&timeframe=day)|네이버 일별 CSV6종·공통기간 계산|원본·수정계수 제한 명시, 국보 제외|KRX 접근400; 인증 미완|
|71|다산네트웍스 2023년 회사 발표·사업보고서|당사자 주장|[원문1](https://www.dasannetworks.com/sub/sub03_04.php?category=2023) · [원문2](https://www.dasannetworks.com/) · [원문3](https://kind.krx.co.kr/external/2024/03/21/001479/20240321005920/11011.htm)|회사 발표·2023 사업보고서|시범·협력과 유상 대형 발주 구별|재건별 매출·회수액 미확인|
|72|Ferrexpo 2026년 중간 실적(2026.9.25)|확인|[원문1](https://www.ferrexpo.com/media/nl5nlb2l/ferrexpo-2026-interim-results_website_final.pdf)|중간보고서 생산·손익·현금·증자|2026H1 production1.556m/CF-24mUSD|회사세금분쟁 설명은 당사자 입장|
|73|HANetf UKRN 공식 상품 페이지·보유종목 파일|확인|[원문1](https://hanetf.com/fund/ukrn-defiance-ukraine-reconstruction-etf/) · [원문2](https://etf.hanetf.com/Holdings-UKRN-IE000R8PO127-all-all) · [원문3](https://etf.hanetf.com/Factsheet-UKRN-IE000R8PO127-en)|공식10.8 보유파일 CSV,10.7 사이트,8.31 factsheet|43.88/0.18%와.65% 비용률|순유입·기업별UA매출 비공개|
|74|폴란드 국유자산부, 3사 재건 협력 MOU(2026.5.15)|확인|[원문1](https://www.gov.pl/web/aktywa-panstwowe/synergia-dla-odbudowy-ukrainy--podpisanie-porozumienia-o-wspolpracy-na-rzecz-odbudowy-ukrainy-w-ministerstwie-aktywow-panstwowych)|폴란드 정부 MOU발표|협력≠수주|2026.5.15|
|75|Naftogaz, Siemens Energy MOU(2026.10.5)|당사자 주장|[원문1](https://www.naftogaz.com/en/news/naftogaz-and-siemens-energy-sign-memorandum-on-energy-security-and-underground-gas-storage-modernisation)|Naftogaz 최신 MOU|실제 터빈발주 금액·금융종결 미확인|2026.10.5|
|76|Buzzi, 우크라이나 사업 매각 완료(2024.10.14)|확인|[원문1](https://www.buzzi.com/w/completata-la-cessione-delle-attivita-in-ucraina)|Buzzi의 2024년 인수 완료 발표·2023년 실적|과거 매각대금과 CRH의 현재 재건 이익·회수를 분리|2026년 해당 자산 순현금·투자 회수 미확인; 현재 시장성 근거로 사용 안 함|
|77|AECOM, 재건 인프라 자문 MOU(2023.6.20)|당사자 주장|[원문1](https://aecom.com/press-releases/aecom-to-serve-as-infrastructure-delivery-advisor-for-ukraine-reconstruction/)|AECOM 자문MOU|확정 거액 건설매출의 증거로 사용 안 함|2023.6|
|78|AECOM 2025 Form 10-K|확인|[원문1](https://www.sec.gov/Archives/edgar/data/868857/000086885725000013/acm-20250930.htm)|2025 SEC10-K 웹 본문 직접 읽음|해당 보고서에서UA재건매출 별도 미확인|2026분기까지 전체전수조회 아님|
|79|Euroclear 2026년 상반기 실적·법률 대응|당사자 주장|[원문1](https://www.euroclear.com/newsandinsights/en/press/2026/mr-20-euroclear-h1-2026-results.html)|회사H1 발표; 러시아 항소기각·Fitch평가|202bn제재자산 범위, 가까운위험평가 구별|기관 설명이지 EU최종판결 아님|
|80|러시아 중앙은행, 모스크바 소송 발표(2025.12.12)|당사자 주장|[원문1](https://www.cbr.ru/eng/press/PR/?file=639011472901412429OBAUT_E.htm)|CBR 모스크바소송 발표|청구·권리주장과 재판결론 구별|2025.12|
|81|러시아 중앙은행, EU 법원 제소 발표(2026.3.3)|당사자 주장|[원문1](https://www.cbr.ru/eng/press/pr/?file=639080409737537862OBAUT_E.htm)|CBR EU제소 발표|제소일2.27/발표3.3 구별|원고주장|
|82|EU 관보, 사건 T-150/26, 2026.4.13 공고|확인|[원문1](https://eur-lex.europa.eu/legal-content/EN/CASE/?uri=oj%3AC_202602053)|공식EU관보 사건색인·공고검색 본문|T-150/26제소 공고; PDF직접봇차단|본안 최종판결 미확보|
|83|Brussels Times/Belga, 브뤼셀 대응소송(2026.6.30)|일부 확인|[원문1](https://www.brusselstimes.com/world/2209129/euroclear-sues-russian-central-bank-in-brussels-court)|Belga/LEcho인용 BrusselsTimes|브뤼셀 소송 보도 수준|사건기록·최종판결 미확보|
|84|IFC, Elementum SII 49272; 2026.8.6 갱신|확인|[원문1](https://disclosures.ifc.org/project-detail/SII/49272/elementum-debt)|IFC SII49272|400mEUR,79m혼합금융,9%보조금상당액|승인7.21,갱신8.6서명대기|
|85|EBRD, Ukrenergo PSD 55539(2025.12 승인)|확인|[원문1](https://www.ebrd.com/home/work-with-us/projects/psd/55539.html)|EBRD PSD55539|90m대출+최대60m조건부보조금|2025.12 승인; 수입모형 공개범위 제한|
|86|EBRD, 기관차 계약·국제 금융지원(2025)|확인|[원문1](https://www.ebrd.com/home/news-and-events/news/2025/international-support-for-ukraine-demonstrated-through-major-rai.html)|EBRD 실제 공급계약 행사·금융발표|300mEUR대출+최대190mUSD보조금|서로다른통화 합산 안 함|
|87|우크라이나 PPP Agency, M15 예비타당성 조사(2026.6.17)|확인|[원문1](https://pppagency.gov.ua/one-more-pilot-public-investment-project-has-begun-preparations-under-the-ukraine-government-ppf/)|PPP Agency 예비FS 용역 선정|검토가 존재; 공사발주 완료 아님|2026.6.17|
|88|EBRD, 헤르손 항만 양허(2020)|확인|[원문1](https://www.ebrd.com/home/news-and-events/news/2020/ebrd-supports-first-concession-project-in-ukraine.html)|2020년 EBRD 양허 체결 발표|과거 운영권·계획을 현재 수익성의 반례로 사용하지 않음|2026년 가동·변경 비용·순현금·회수 미확인; 접근 조건은 [106]으로 보강|
|89|EIB, 미콜라이우·드니프로 집행(2024.11.19)|확인|[원문1](https://www.eib.org/en/press/all/2024-453-ukraine-eib-provides-eur14-5-million-to-support-municipal-projects-in-war-torn-cities-of-mykolaiv-and-dnipro)|EIB의 2024년 지급액 Mykolaiv7.8/Dnipro6.7mEUR|과거 집행과 2026년 요금·대출 회수를 구분|전체 사업의 현재 운영·상환 현금 미확인|
|90|EBRD, M10 리비우 산업단지 투자(2023)|확인|[원문1](https://www.ebrd.com/home/news-and-events/news/2023/ebrd-invests-in-developing-lviv-industrial-park-in-western-ukraine.html)|EBRD의 2023년 투자 계획과 지분 구조|당시 계약·투자는 현재 수익성 증거에서 제외|현재 개발 발표 [107]도 순현금·배당·투자 회수 검증을 대신하지 못함|
|91|UkraineInvest, M10 1단계 개장(2024.2.27)|당사자 주장|[원문1](https://ukraineinvest.gov.ua/en/news/27-02-2024-1/)|UkraineInvest의 2024년 개장·5.5mUSD 투자 발표|과거 개장·자금 투입을 현재 이익으로 전용하지 않음|2026년 임대 순현금·배당·자본 회수 미공개|
|92|NABU, 미다스 최초 혐의 발표(2025.11.11)|수사기관 혐의|[원문1](https://nabu.gov.ua/en/news/operatciia-midas-vykryto-vysokorivnevu-zlochynnu-organizatciiu-shcho-diiala-u-sferi-energetyky/)|NABU 최초발표|10~15%요구·100m세탁혐의|전체원조 도난비율 아님|
|93|NABU, 미다스 추가 혐의(2026.7.10)|수사기관 혐의|[원문1](https://nabu.gov.ua/en/news/operatciia-midas-nova-pidozra/)|NABU 추가혐의|수사 계속 확인|2026.7.10; 확정판결 미확보|
|94|UBS, 유럽 투자 주제·재건(2025.3.11)|일부 확인|[원문1](https://www.ubs.com/us/en/wealth-management/insights/article.1997555.html)|UBS공식검색에재건/독일등투자주제|재건바스켓2025수익률 미검증|다른바스켓 수익률 전용 금지|
|95|한국일보, 삼부토건 사건 재판 진행(2026.7.24)|일부 확인|[원문1](https://v.daum.net/v/20260724163709596)|2026.7.24 재판보도|그 시점 심리 진행|10.9현시점 최종결론 단정 안 함|
|96|KRX 기타시장안내, 삼부토건(2026.8.31)|확인|[원문1](https://dart.fss.or.kr/report/viewer.do?rcpNo=20260831800966&dcmNo=11561863&eleId=0&offset=0&length=0&dtd=HTML)|KRX시장안내 DART재게재; EUC-KR원문 확인|8.31 심사 검토·거래정지 계속|그후 심사 전부 조회 아님|
|97|KRX 웰바이오텍 상장폐지 공고 재게재, 2026.1.26 폐지|일부 확인|[원문1](https://stock.mk.co.kr/news/disclosure/template/855739)|KRX공고 재게재|2026.1.26 상장폐지|KRX 원공고식별번호 미확보|
|98|국보 상장폐지 보도(2026.1.23)|일부 확인|[원문1](https://v.daum.net/v/20260123105034883)|2026.1.23 기사|국보1월상장폐지|KRX 원공고 미확보|
|99|Ferrexpo 주가의 종전 기대 반응 보도(2024.11.6)|일부 확인|[원문1](https://www.proactiveinvestors.co.uk/companies/news/1059984/ferrexpo-shares-spike-as-trump-win-lifts-hopes-for-end-to-ukraine-war-1059984.html)|주가반응 보도|기대와 실적의 차이|거래소 이벤트 인과분석 미완|
|100|SEC Form 4, Troy Rudd/AECOM 매수(2026.5.14)|확인|[원문1](https://www.sec.gov/Archives/edgar/data/1653811/000165381126000002/xslF345X03/wk-form4_1778788962.xml)|SEC Form4 코드P/A|4225주$71.02 매수|매도·재건차익으로 오독 금지|
|101|AP, 러시아 법원 Euroclear 사건 판단(2026.5.15)|일부 확인|[원문1](https://apnews.com/article/85750e45d2da06168a72aeb8f41ec53b)|AP 러시아판결 보도|18.2trRUB 동일청구|러시아→EU자동집행 아님|
|102|삼부토건 2026년 1분기보고서|확인|[원문1](https://kind.krx.co.kr/external/2026/05/15/002323/20260515005207/11013.htm)|KIND분기보고서|해외매출0/진행중해외사업없음|2026Q1 공시; 반기[65]로 보강|
|103|Ferrexpo 이벤트 시점 주가 보도: 2024.11·2025.2·2025.5 (거래소 수정시세 인증 아님)|일부 확인|[원문1](https://www.itiger.com/news/2481271136) · [원문2](https://good-time-invest.com/blog/ukrainian-companies-shares-on-the-rise-amid-prospects-of-wars-end/) · [원문3](https://www.lse.co.uk/news/ftse-100-movers-ferrexpo-gains-on-ukraine-minerals-deal-clarkson-tanks-tjh707hpuvbdjxg.html)|Reuters재게재·Sharecast시점 가격;2월 투자홍보 글|5.1 14:58의70.40p/+19.52%만 본문 수치 사용|장중값≠종가; LSE계열 미확보;2월18.06%는 제외|
|104|우크라이나 복구청 Bechtel MOU(2023.6.23)·Bechtel 체르노빌 실제 사업|확인|[원문1](https://restoration.gov.ua/blog/agentstvo-vidnovlennya-spivpraczyuvatyme-z-liderom-u-sferi-inzhyniryngu-ta-budivnycztva-korporacziyeyu-bechtel/) · [원문2](https://www.bechtel.com/projects/chornobyl-new-safe-confinement/)|복구청MOU 웹원문·Bechtel 실제과거사업 설명|2023구상과 EBRD공적재원 사업 구별|당사자 발표; 재건별 계약이익 미공개|
|105|KRX, 삼부토건 기업심사위원회 심의대상 결정(2026.9.21)|확인|[원문1](https://dart.fss.or.kr/report/viewer.do?rcpNo=20260921800376&dcmNo=11587021&eleId=0&offset=0&length=0&dtd=HTML)|KRX9.21 공시 DART재게재 EUC-KR본문 확인|심의대상 결정, 이후 절차와 거래정지 구별|최종 상장결론을 앞당겨 쓰지 않음|
|106|우크라이나 개발부, 올비야 국영기업 2026년 계획(2025.7.25 승인), pp2~3: 헤르손 자산 접근 조건|확인|[원문1](https://mindev.gov.ua/storage/app/sites/1/uploaded-files/list-ocikuvan-vlasnika-dp-sk-olviia-2026.pdf)|정부의 2026년 국영기업 계획 p3에 헤르손 자산·원본 문서 안전 접근 조건|2020년 양허와 현재 접근 가능성을 분리|2025.7.25 승인 계획; 민간 양허 운영자의 손익·현재 접근 실측 자료는 아님|
|107|Dragon Capital, M10 2단계 건설·1단계 가동·공적 지분과 보증 발표(2026.3.30)|당사자 주장|[원문1](https://dragon-capital.com/media/press-releases/dragon-capital-launches-construction-of-phase-ii-of-m10-lviv-industrial-park/)|2026.3.30 M10 1단계 가동·2단계22,000㎡·공적 지분·MIGA 보증 발표|최근 가동 발표를 기록하되 현재 수익성 성공 사례에서 제외|실제 임대료·순현금·비용·배당·회수 미공개; fully operational은 전면 입주율을 뜻하지 않음|
|108|Dragon Capital, 전쟁 격화와 추가 조달 필요에 관한 2026~27년 전망 갱신(2026.10.8)|당사자 주장|[원문1](https://dragon-capital.com/media/press-releases/onovleniy-makroprognoz-na-2026-2027-roki-ekonomichni-naslidki-posilennya-atak/)|2026.10.8 투자기관 전망 갱신의 영문 공개 본문|2022~2023년 가정을 현재 시장성으로 재사용할 수 없다는 분석의 참고|기관 전망·평가; 모든 사업 실측 손실이나 전국 항만 상태의 독립 조사로 확대 안 함|

## 재현·검산

- GDP: `data/prewar_wdi.csv` → `gdp_index_1990_100.csv`. 국가별 1990 자체 GDP를 분모로 사용. 9개국·32개연도·3개지표 864행.
- 한국 주가: 원본 제공 CSV6개와 `korean_stocks_comparison.json`. 동일기간 최고종가/기말, 거래없는 국보 기준일 제외. KRX원본 인증 미완을 도표와 본문에 적음.
- ETF: 원본 XLSX의 표를 CSV로 보존. 10월8일 파일의 비중 합계99.98%는 개별 반올림 영향. 10월7일 사이트 자산과 다른 날 보유비중을 구별.
- RDNA: 18부문 반올림값과 공식 총계는 별도. 차액은 저자 계산이고 노후화 비용 전액이 아님. 보고서 p5 손실기간 문구와 표1주석이 불일치하여 표 주석을 적용.
- 부차: 총214/318mEUR는106+108/212m. 단순회수기간을 할인 NPV·IRR로 바꾸지 않음.
- 이미지11개: `charts/make_charts.py`; 모든 도표에 통화·기간·출처·제한을 명시. 연락처나 비공개 계정정보를 사용하지 않음.

## 편집적 평가와 검증의 경계

“사기극”, “도둑놈 심보”는 정책·조달·기대 장사에 대한 필자의 평가다. 법적 범죄는 수사기관 혐의와 재판자료 범위를 구분했다. 제공 가격에서 계산한 상승률은 평가손익이지 매도자의 실현수익이 아니다. 국가지표는 필요·총생산·인구 범위에 대한 통계이며 미공개 개별사업 현금흐름을 대체하지 않는다.
