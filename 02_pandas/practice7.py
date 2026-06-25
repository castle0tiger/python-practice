import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'


data = {
    "강의명": ["파이썬 기초", "데이터분석", "머신러닝", "웹개발", "SQL 기초", "딥러닝", "통계학"],
    "카테고리": ["프로그래밍", "데이터", "AI", "프로그래밍", "데이터", "AI", "데이터"],
    "수강생수": [1200, 850, 620, 980, 540, 430, 390],
    "평점": [4.8, 4.5, 4.7, 4.2, 4.3, 4.9, 4.1],
    "가격": [50000, 80000, 120000, 60000, 40000, 150000, 70000]
}


df = pd.DataFrame(data)
print("\n===DataFrame 생성 출력===")
print(df)

df["총매출"] = df["수강생수"] * df["가격"]
print("\n===총매출 열 추가===")
print(df)

result = df.groupby("카테고리").agg({"총매출": "sum", "평점":"mean"})
print("\n===카테고리별 총매출 합계, 평균 평점 동시 출력===")
print(result)

print("\n===평점 4.5 이상이고 수강생수 600 이상인 강의 필터링===")
print(df[(df["평점"] >= 4.5) & (df["수강생수"] >= 600)])

df["추천여부"] = df["평점"].apply(lambda x: "추천" if x >= 4.5 else "보통")
print("\n===추천여부 열 추가===")
print(df)

sorted_df = df.sort_values("총매출", ascending=False).head(3)
print("\n===총매출 기준 내림차순 상위 3개 출력 (강의명, 카테고리, 총매출만)===")
print(sorted_df[["강의명", "카테고리", "총매출"]])

result2 = df.groupby("카테고리")["총매출"].sum()
result2.plot(kind="bar", title="카테고리별 총매출 합계 막대 그래프")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
print("\n===카테고리별 총매출 합계 막대 그래프===")