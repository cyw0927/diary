# 우크라이나 재건 비판 칼럼

[개정 본문](ukraine_reconstruction_critique.md) · [개정 요약](revision_summary.md) · [출처·팩트체크](sources_and_factcheck.md) · [미확인 주장](unverified_claims.md)

[18개 부문·사업성](sector_business_analysis.md) · [주가·기업 사례](stock_market_cases.md) · [러시아 자산](russian_assets_legal_risks.md)

자료 확인 기준은 2026-10-09다. 본문은 커뮤니티용 비판 칼럼이며, 부록은 주장별 증거와 한계를 확인하는 자료다. 과거 계약·투자와 현재 수익성을 구분하고, 2022~2023년 계약을 2026년 시장성의 성공 사례로 사용하지 않는다.

## 도표 재현

Python 3.12에서 `pandas`, `matplotlib`, `Pillow`를 설치하고, 이 폴더에서 다음 명령을 실행한다. Windows에서는 맑은고딕을 사용한다. 다른 환경에는 한글 폰트 설정이 필요하다.

```powershell
python charts/make_charts.py
```

이미지 11개와 도표별 수치파일을 생성한다. 네트워크나 로그인이 필요 없다. CSV·JSON은 확인 기준일에 저장한 수치 스냅샷이다.

공개 자료의 재수집에는 `pypdf`, `openpyxl`도 사용한다. `collect_sources.py audit`는 기준 커밋의 기존 61개 출처를 다시 찾아 접근 결과를 기록한다. 재수집은 현재 데이터를 가져오므로 2026-10-09 스냅샷을 보존하려면 기존 파일을 덮어쓰지 않아야 한다. 원문 접근 결과는 내용의 검증 완료 판정과 다르다.

가격은 네이버 제공 계열이며 KRX 원본 수정계수의 독립 인증이 미완료다. [주가 부록](stock_market_cases.md)의 기간·거래정지·기업행위 제한을 읽고 사용해야 한다. 각주번호와 판정은 `data/source_registry.json`, `data/claim_audit.json`에도 있다.
