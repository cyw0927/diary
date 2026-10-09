# 칼럼 저장소

시사·경제 비평 칼럼의 원고, 도표, 출처를 보관하는 저장소입니다.

## 연재 목록

| 날짜 | 제목 | 폴더 |
|---|---|---|
| 2026-10 | 우크라이나 재건 - 21세기 최악의 사기극 | [columns/2026-10-ukraine-reconstruction](columns/2026-10-ukraine-reconstruction) |

## 폴더 구성 (칼럼마다 동일)

```
columns/<날짜>-<주제>/
├── <칼럼>.md                  # 본문
├── sources_and_factcheck.md   # 항목별 사실검증 및 출처표
├── unverified_claims.md       # 추가 검증이 필요한 주장 목록
├── images/                    # 본문 삽입 도표 (게시 순서대로 번호)
└── charts/make_charts.py      # 도표 생성 스크립트
```

## 게시할 때

- `images/`의 번호 순서가 본문에 삽입되는 순서입니다.
- 도표는 모두 공개 통계로 직접 만든 것이라 저작권 문제가 없습니다.
- 도표를 다시 만들려면 matplotlib과 맑은 고딕 글꼴(Windows)이 필요합니다.

```bash
python charts/make_charts.py images
```
