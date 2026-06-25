import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'


orders = {
    "주문ID": [1, 2, 3, 4, 5, 6, 7],
    "고객명": ["김민준", "이수진", "박태양", "최하늘", "정지수", "강민서", "윤하은"],
    "카테고리": ["치킨", "피자", "한식", "치킨", "피자", "한식", "치킨"],
    "주문금액": [18000, 25000, 12000, 22000, 15000, 9000, 20000],
    "배달시간": [25, 40, 20, 35, 28, 45, 30]
}

reviews = {
    "주문ID": [1, 2, 3, 4, 5, 6, 7],
    "평점": [4.8, 4.3, 4.6, 4.5, 4.9, 4.1, 4.7],
    "재주문의향": ["예", "아니오", "예", "예", "예", "아니오", "예"]
}


df1 = pd.DataFrame(orders)
print("\n===1.주문데이터(orders) DataFrame 생성===")
print(df1)

df2 = pd.DataFrame(reviews)
print("\n===1.리뷰(reviews) DataFrame 생성===")
print(df2)


df = pd.merge(df1, df2, on="주문ID")
print("\n===2.두 개의 DataFrame을 주문ID 기준으로 합치기===")
print(df)


result = df.groupby("카테고리").agg({"주문금액" : "sum", "평점" : "mean"})
print("\n===3.카테고리별 평균 주문금액 합계, 평균 평점 동시 출력===")
print(result)


print("\n===4.주문금액 15000 이상이고 평점 4.5 이상인 주문 필터링===")
print(df[(df["주문금액"] >= 15000) & (df["평점"] >= 4.5)])


df["배달등급"] = df["배달시간"].apply(lambda x: "빠름" if x <= 30 else "보통")
print("\n===5.배달등급 열 추가===")
print(df)


sorted_df = df.sort_values("평점", ascending=False).head(3)
print("\n===6.평점 기준 내림차순 상위 3개 출력===")
print(sorted_df[["고객명", "카테고리", "주문금액", "평점"]])


result2 = df.groupby("카테고리")["주문금액"].sum()
result2.plot(kind="bar", title="카테고리별 주문금액 합계 막대 그래프")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
print("\n===7/카테고리별 주문금액 합계 막대 그래프===")