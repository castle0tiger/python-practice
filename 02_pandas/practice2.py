import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

data = {
    "날짜": ["월", "화", "수", "목", "금", "토", "일"],
    "아메리카노": [45, 38, 52, 41, 60, 75, 80],
    "라떼": [30, 25, 35, 28, 45, 60, 65],
    "케이크": [15, 12, 18, 14, 25, 40, 45]
}

# 1.DataFrame 만들고 출력
df = pd.DataFrame(data)
print(df)

# 2."총판매량" 열 추가 (세 메뉴 합계)
df["총판매량"] = df["아메리카노"] + df["라떼"] + df["케이크"]
print(df)

# 3."주말여부" 열 추가
df["주말여부"] = df["날짜"].apply(lambda x: "주말" if x in ["토", "일"] else "평일")

# 4.주말vs평일 평균 이상 날만 필터링 출력
result = df.groupby("주말여부")["총판매량"].mean()
print(result)

# 5.총판매량이 평균 이상인 날만 필터링 출력
avg = df["총판매량"].mean()
print(df[df["총판매량"] >= avg])

# 6.날짜별 아메리카노/라떼/케이크 꺾은선 그래프 (3개 같이)
df.plot(kind="line", x="날짜", y=["아메리카노", "라떼", "케이크"], title="날짜별 판매량", marker="o")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

