import sys, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

fm.fontManager.addfont("C:/Windows/Fonts/malgun.ttf")
fm.fontManager.addfont("C:/Windows/Fonts/malgunbd.ttf")
plt.rcParams.update({
    "font.family": "Malgun Gothic",
    "axes.unicode_minus": False,
    "figure.dpi": 100,
    "savefig.dpi": 150,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.edgecolor": "#888",
    "axes.labelcolor": "#333",
    "xtick.color": "#444",
    "ytick.color": "#222",
})

INK = "#1f2328"
MUTED = "#8a8f98"
RED = "#c8102e"
BLUE = "#2b5fab"
GREY = "#c9ccd1"
LIGHT = "#e8eaed"


def finish(fig, title, subtitle, source, name):
    fig.text(0.02, 0.975, title, fontsize=19, fontweight="bold", color=INK, va="top")
    if subtitle:
        fig.text(0.02, 0.915, subtitle, fontsize=11.5, color="#555", va="top")
    fig.text(0.02, 0.02, source, fontsize=8.5, color=MUTED, va="bottom")
    fig.savefig(os.path.join(OUT, name), facecolor="white")
    plt.close(fig)
    print("wrote", name)


# 1. 숫자 다섯 개, 기준은 다섯 개
def chart_numbers():
    rows = [
        ("2026년 우선사업 (1년)", 152.5, BLUE, "세계은행 RDNA5"),
        ("직접 물적 피해 (2022.2~2025.12 누적)", 1951, BLUE, "세계은행 RDNA5"),
        ("[참고] 우크라이나 2025년 명목 GDP", 2100, GREY, "필자 환산·추정치"),
        ("10년 재건·회복 필요액 (2026~2035)", 5877, RED, "세계은행 RDNA5"),
        ("경제·사회적 손실 (64개월, 일부 추정)", 6667, BLUE, "세계은행 RDNA5"),
        ("Ukraine Prosperity Plan (10년 구상)", 8000, "#6b4fa0", "우크라이나 정부"),
    ]
    fig, ax = plt.subplots(figsize=(11, 6.4))
    fig.subplots_adjust(left=0.33, right=0.93, top=0.84, bottom=0.12)
    y = range(len(rows))
    ax.barh(y, [r[1] for r in rows], color=[r[2] for r in rows], height=0.62)
    ax.set_yticks(list(y), [r[0] for r in rows], fontsize=11.5)
    for i, r in enumerate(rows):
        label = f"{r[1]:,.1f}억 달러" if r[1] < 1000 else f"{r[1]:,.0f}억 달러"
        if r[0].startswith("[참고]"):
            label = "약 " + label
        if r[0].startswith("Ukraine"):
            label = "약 " + label
        ax.text(r[1] + 80, i, f"{label}  ·  {r[3]}", va="center", fontsize=10.5, color=INK)
    ax.set_xlim(0, 11500)
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    ax.tick_params(axis="y", length=0)
    finish(fig, "'재건비'라고 불리는 숫자들은 서로 다른 것을 잰다",
           "피해액(과거 자산의 전쟁 전 가격) ≠ 손실(놓친 생산·소득) ≠ 필요액(BBB·인플레이션 포함 미래 투자) ≠ 개발 구상",
           "자료: World Bank RDNA5 (2026.2.23), 우크라이나 경제부 (2026.1.3). GDP는 우크라이나 통계청 잠정치(8조9,312억 흐리우냐)를 RDNA5 환율(42.39)로 필자가 환산.",
           "02_numbers.png")


# 2. 분야별 피해액 vs 필요액
def chart_sectors():
    data = [
        ("교통", 40.3, 96.3),
        ("에너지·자원", 24.8, 90.6),
        ("주택", 61.1, 89.8),
        ("상업·산업", 19.2, 63.3),
        ("농업", 12.1, 55.3),
        ("사회보장·생계", 0.5, 42.7),
        ("교육·과학", 13.9, 33.5),
        ("지뢰·폭발물 제거", 0.0, 27.6),
        ("보건", 1.8, 23.6),
        ("상하수도", 7.8, 17.5),
        ("관개·수자원", 0.9, 12.5),
        ("문화·관광", 4.5, 11.5),
        ("기타 6개 분야", 8.4, 23.4),
    ]
    data = data[::-1]
    fig, ax = plt.subplots(figsize=(11, 8))
    fig.subplots_adjust(left=0.17, right=0.95, top=0.86, bottom=0.11)
    y = list(range(len(data)))
    h = 0.38
    ax.barh([i + h / 2 for i in y], [d[2] for d in data], height=h, color=RED, label="10년 필요액 (BBB·인플레이션 포함)")
    ax.barh([i - h / 2 for i in y], [d[1] for d in data], height=h, color=GREY, label="직접 피해액 (전쟁 전 교체가격)")
    for i, d in enumerate(data):
        ax.text(d[2] + 1, i + h / 2, f"{d[2]:.1f}", va="center", fontsize=9.5, color=INK)
        ax.text(d[1] + 1, i - h / 2, f"{d[1]:.1f}", va="center", fontsize=9.5, color=MUTED)
    ax.set_yticks(y, [d[0] for d in data], fontsize=11.5)
    ax.tick_params(axis="y", length=0)
    ax.set_xlabel("10억 달러", fontsize=10)
    ax.set_xlim(0, 110)
    ax.legend(loc="lower right", frameon=False, fontsize=10.5)
    ax.grid(axis="x", color=LIGHT)
    ax.set_axisbelow(True)
    finish(fig, "부서진 것 1,951억 달러, 고치겠다는 것 5,877억 달러",
           "분야별 직접 피해액과 10년 재건 필요액. 둘의 차이가 전부 '현대화 할증'은 아니다 — 그런데 얼마가 할증인지는 공식 수치가 없다.",
           "자료: World Bank RDNA5 (2026.2.23) Table 1. '기타'는 도시서비스·통신·환경·민방위·금융·행정. 피해 0.0 = 1억 달러 미만.",
           "03_sectors.png")


# 3. RDNA 1~5 추이
def chart_trend():
    eds = ["RDNA1\n2022.6", "RDNA2\n2023.2", "RDNA3\n2023.12", "RDNA4\n2024.12", "RDNA5\n2025.12"]
    damage = [97, 135, 152, 176, 195.1]
    needs = [348.5, 410.6, 486.2, 523.6, 587.7]
    fig, ax = plt.subplots(figsize=(11, 6.2))
    fig.subplots_adjust(left=0.08, right=0.95, top=0.84, bottom=0.15)
    x = range(len(eds))
    ax.plot(x, needs, marker="o", color=RED, lw=3, label="10년 재건 필요액")
    ax.plot(x, damage, marker="o", color=MUTED, lw=3, label="직접 피해액")
    for i in x:
        ax.text(i, needs[i] + 18, ["349","411","486","524","588"][i], ha="center", fontsize=11, color=RED, fontweight="bold")
        ax.text(i, damage[i] - 38, f"{damage[i]:.0f}", ha="center", fontsize=11, color="#555")
    ax.set_xticks(list(x), eds, fontsize=10.5)
    ax.set_ylim(0, 680)
    ax.set_ylabel("10억 달러")
    ax.grid(axis="y", color=LIGHT)
    ax.set_axisbelow(True)
    ax.legend(loc="upper left", frameon=False, fontsize=11)
    finish(fig, "보고서가 나올 때마다 늘어나는 청구서",
           "기준일별 누적 피해액과 10년 필요액. 세계은행 스스로 '시점 간 단순 비교는 어렵다'고 밝힌다(방법론·환율·인플레이션 변경).",
           "자료: World Bank RDNA1~5 (RDNA5 부록 요약 기준). x축은 각 평가의 집계 기준일.",
           "04_trend.png")


# 4. 난민 귀국 의향 추이
def chart_return():
    rounds = ["2022.8~9", "2023\n(1차)", "2023\n(2차)", "2024.1~2", "2024.7~8", "2025.12~\n2026.1"]
    vals = [83, 77, 76, 65, 61, 49]
    fig, ax = plt.subplots(figsize=(11, 6.2))
    fig.subplots_adjust(left=0.08, right=0.95, top=0.84, bottom=0.15)
    x = list(range(len(rounds)))
    cols = [GREY] * (len(vals) - 1) + [RED]
    ax.bar(x, vals, color=cols, width=0.6)
    for i, v in enumerate(vals):
        ax.text(i, v + (4 if i == len(vals) - 1 else 1.5), f"{v}%", ha="center", fontsize=13, fontweight="bold", color=RED if i == len(vals) - 1 else INK)
    ax.axhline(50, color=MUTED, lw=1, ls="--")
    ax.text(len(vals) - 0.55, 51.5, "50%", color=MUTED, fontsize=9.5)
    ax.set_xticks(x, rounds, fontsize=10.5)
    ax.set_ylim(0, 100)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.text(4.45, 99, "최근 조사(2025.12~2026.1) 내역\n· 1년 안에 귀국 계획: 3%\n· 언젠가 귀국 희망: 46%\n· 미정: 28%\n· 귀국 희망 없음: 23%",
            ha="left", va="top", fontsize=10.5, color=INK, linespacing=1.5,
            bbox=dict(boxstyle="round,pad=0.6", fc="#f6f7f8", ec=LIGHT))
    finish(fig, "돌아오겠다는 난민, 처음으로 절반 아래",
           "유럽 내 우크라이나 난민 중 '귀국을 계획하거나 언젠가 희망한다'는 응답 비율 (UNHCR 정기 의향조사)",
           "자료: UNHCR, Lives on Hold #7 (2026.7; 2025.12~2026.1 조사, 4,375가구). 영토가 회복된 종전이라면 귀국 '가능성 높음' 65%, 점령지 미회복 종전이면 32%.",
           "07_return.png")


# 5. 마리우폴 타임라인
def chart_mariupol():
    import datetime as dt
    ev = [
        (dt.date(2022, 2, 24), "러시아 전면 침공", INK),
        (dt.date(2022, 5, 20), "아조우스탈 함락, 러시아 '완전 장악' 발표", RED),
        (dt.date(2022, 7, 5), "루가노 재건회의: 우크라 정부 7,500억 달러 재건계획 제시", INK),
        (dt.date(2022, 7, 6), "서울: 타루타 의원 등, 원희룡 장관에 마리우폴 재건 참여 요청", RED),
        (dt.date(2022, 9, 30), "러시아, 도네츠크 등 4개주 '병합' 선포", INK),
        (dt.date(2022, 10, 12), "유엔총회, 병합 무효 결의 (찬성 143)", INK),
        (dt.date(2023, 10, 6), "타루타 의원단 재방한, 포스코 회장 면담", INK),
        (dt.date(2025, 11, 23), "NYT: 크렘린, 마리우폴 재개발에 수십억 달러 투입", INK),
        (dt.date(2026, 5, 13), "점령당국, '버려진' 아파트 약 900채 압류 목록 (우크라 측 발표)", INK),
    ]
    fig, ax = plt.subplots(figsize=(11, 7.6))
    fig.subplots_adjust(left=0.04, right=0.98, top=0.86, bottom=0.08)
    n = len(ev)
    ys = list(range(n))[::-1]
    ax.axvspan(0.12, 0.16, ymin=0, ymax=1, color=LIGHT)
    for (d, label, c), y in zip(ev, ys):
        ax.plot([0.14], [y], marker="o", ms=11, color=c, zorder=3)
        ax.text(0.0, y, d.strftime("%Y.%m.%d"), va="center", fontsize=11, color=MUTED)
        ax.text(0.18, y, label, va="center", fontsize=12.5, color=c, fontweight="bold" if c == RED else "normal")
    # 러시아 통제 구간 표시
    y_fall = ys[1]
    ax.annotate("", xy=(0.105, ys[-1] - 0.3), xytext=(0.105, y_fall + 0.3),
                arrowprops=dict(arrowstyle="-", color=RED, lw=4))
    ax.text(0.105, y_fall + 0.5, "러시아 통제 ▼", va="center", ha="center", fontsize=10, color=RED, fontweight="bold")
    ax.text(0.18, ys[3] - 0.45, "→ 점령 47일째. 보도자료에는 '전후 재건'이라는 표현만 있고 점령 사실은 언급되지 않음",
            fontsize=10.5, color="#555")
    ax.set_xlim(-0.01, 1)
    ax.set_ylim(-0.8, n - 0.3)
    ax.axis("off")
    finish(fig, "마리우폴 재건 제안은 언제 나왔나",
           "한국에 재건 참여를 요청한 시점, 도시는 이미 러시아 통제 아래 있었다",
           "자료: 국토교통부 보도참고자료(2022.7.6), AP·Reuters(2022.5), 유엔총회 ES-11/4(2022.10.12), POSCO 뉴스룸(2023.10), NYT(2025.11), 마리우폴 시의회 via Euromaidan Press(2026.5.13).",
           "05_mariupol.png")


# 6. 한국: 약속과 실제 돈
def chart_korea():
    rows = [
        ("윤석열 대통령 지원 발표 (2023.9, G20)", 2300, GREY, "정치적 약속 · 23억 달러"),
        ("EDCF 기본약정 한도 (2024.4, 2024~2029)", 2100, GREY, "한도일 뿐 · 21억 달러"),
        ("보리스필 공항 MOU (2023.11, 공사·현대건설)", 983, GREY, "양해각서 · 약 9.8억 달러"),
        ("철도차량 20편성 EDCF 차관 '요청서' (2025.9)", 450, GREY, "요청 단계 · 약 4~4.5억 달러 (보도 추정)"),
        ("실제 서명·집행된 EDCF 차관 (2024.10)", 100, RED, "1억 달러 · 재정지원용 (건설 아님)"),
        ("확인된 한국 기업 건설·공급 계약 대금", 0, RED, "확인된 건 없음"),
    ]
    rows = rows[::-1]
    fig, ax = plt.subplots(figsize=(11, 6.2))
    fig.subplots_adjust(left=0.36, right=0.97, top=0.84, bottom=0.12)
    y = list(range(len(rows)))
    ax.barh(y, [max(r[1], 8) if r[1] else 0 for r in rows], color=[r[2] for r in rows], height=0.6)
    for i, r in enumerate(rows):
        ax.text(r[1] + 30, i, r[3], va="center", fontsize=11, color=RED if r[2] == RED else INK,
                fontweight="bold" if r[2] == RED else "normal")
    ax.set_yticks(y, [r[0] for r in rows], fontsize=11)
    ax.tick_params(axis="y", length=0)
    ax.set_xlim(0, 3400)
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    finish(fig, "MOU는 많았고, 돈은 적었다",
           "한국-우크라이나 재건 협력: 발표·약정·양해각서 vs 실제 서명·집행 (단위: 백만 달러, 2026년 10월 확인 기준)",
           "자료: Korea Times(2023.9.10), 우크라이나 내각(2024.4.19·10.2), Korea JoongAng Daily(2023.11), 우크라이나 지역개발부(2025.9.17).\n2026.7 이재명 대통령의 1억 달러 지원 발표는 세부 내용 미확정으로 제외. 막대 길이는 금액 비례.",
           "06_korea.png")


# 0. 전쟁 전 30년: 실질 GDP 지수
def chart_prewar():
    years = list(range(1990, 2022))
    ukr = [100.0, 91.3, 82.3, 70.6, 54.4, 47.8, 43.0, 41.7, 40.9, 40.8, 43.2, 47.1, 49.6, 54.3, 60.7, 62.5,
           67.3, 72.8, 74.4, 63.2, 65.8, 69.3, 69.4, 69.5, 62.5, 56.4, 57.7, 59.1, 61.2, 63.1, 60.8, 62.9]
    pol = [100.0, 93.0, 95.3, 98.9, 104.1, 112.4, 119.2, 126.8, 132.7, 138.9, 145.4, 147.2, 150.0, 155.2, 163.1,
           168.5, 178.9, 191.0, 199.4, 204.6, 211.1, 222.2, 225.5, 227.1, 236.0, 246.4, 253.9, 267.0, 283.7,
           296.7, 290.6, 310.8]
    fig, ax = plt.subplots(figsize=(11, 6.4))
    fig.subplots_adjust(left=0.07, right=0.88, top=0.84, bottom=0.12)
    ax.plot(years, pol, color=MUTED, lw=3)
    ax.plot(years, ukr, color=RED, lw=3.5)
    ax.axhline(100, color=INK, lw=0.8, ls=":")
    ax.text(2021.4, pol[-1], f"폴란드\n{pol[-1]:.0f}", va="center", fontsize=12, color="#555", fontweight="bold")
    ax.text(2021.4, ukr[-1], f"우크라이나\n{ukr[-1]:.0f}", va="center", fontsize=12, color=RED, fontweight="bold")
    for yr, label in [(1999, "1999년 바닥\n40.8"), (2009, "2009\n-15.1%"), (2015, "2014~15\n-10.1%, -9.8%")]:
        v = ukr[yr - 1990]
        ax.annotate(label, xy=(yr, v), xytext=(yr, v - 26), ha="center", fontsize=9.5, color=INK,
                    arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    ax.text(1990.3, 103, "1990년 = 100", fontsize=9.5, color=INK)
    ax.set_ylim(0, 340)
    ax.set_xlim(1989.5, 2021.5)
    ax.grid(axis="y", color=LIGHT)
    ax.set_axisbelow(True)
    finish(fig, "전쟁 전 31년, 우크라이나는 1990년을 회복하지 못했다",
           "실질 GDP 지수 (1990년 = 100). 같은 출발선에서 폴란드는 3.1배가 됐고 우크라이나는 63%에 머물렀다.",
           "자료: World Bank WDI, NY.GDP.MKTP.KD (2015년 불변 달러, 2026.10.8 갱신). 성장률은 WB·IMF 시계열 기준.",
           "01_prewar_gdp.png")


if __name__ == "__main__":
    which = sys.argv[2:] or ["prewar", "numbers", "sectors", "trend", "mariupol", "korea", "return"]
    for w in which:
        globals()["chart_" + w]()
