import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

data = {
    "주문번호": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "음식종류": ["치킨", "피자", "치킨", "중식", "피자", "치킨", "중식", "피자", "치킨", "중식"],
    "주문금액": [18000, 25000, 19000, 15000, 32000, 21000, 17000, 28000, 22000, 16000],
    "배달시간": [30, 45, 25, 35, 50, 28, 40, 42, 33, 38],
    "평점": [4.5, 3.8, 4.9, 4.2, 3.5, 4.7, 4.0, 3.9, 4.6, 4.3]
}

df = pd.DataFrame(data)
print("\n===DataFrame 만들고 출력===")
print(df)

result = df.groupby("음식종류")[["주문금액", "배달시간", "평점"]].agg("mean")
print("\n===음식 종류별 평균주문금액/평균 배달시간/평균 평점===")
print(result)

print("\n===평점 4.5 이상 주문만 필터링 출력===")
print(df[(df["평점"] >= 4.5)])

df["배달등급"] = df["배달시간"].apply(lambda x: "빠름" if x <= 30 else "보통")
print("\n===배달등급 추가===")
print(df)

sorted_df = df.sort_values("주문금액", ascending=False).head(3)
print("\n===주문금액 기준 내림차순 상위 3개 출력===")
print(sorted_df[["주문번호", "음식종류" ,"주문금액"]])


result2 = df.groupby("음식종류")["주문금액"].mean()
result2.plot(kind="bar", title="음식종류별 평균 주문금액")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
print("\n===음식주문별 평균 주문금액 막대 그래프===")