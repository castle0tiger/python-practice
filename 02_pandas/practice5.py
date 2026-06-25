import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

data = {
    "도서명": ["파이썬", "데이터분석", "머신러닝", "웹개발", "AI입문", "통계학", "딥러닝"],
    "분야": ["프로그래밍", "데이터", "AI", "프로그래밍", "AI", "데이터", "AI"],
    "대출횟수": [45, 38, 52, 30, 60, 25, 48],
    "평점": [4.5, 4.2, 4.8, 3.9, 4.6, 4.1, 4.7],
    "출판연도": [2020, 2019, 2021, 2018, 2022, 2019, 2021]
}

df = pd.DataFrame(data)
print("\n===DataFrame 생성 출력===")
print(df)

result = df.groupby("분야")[["대출횟수", "평점"]].agg("mean")
print("\n===분야별 평균 대출횟수, 평균 평점 동시 출력====")
print(result)

print("\n===평점 4.5점 이상 대출횟수 45 이상 필터링====")
print(df[(df["평점"] >=4.5) & (df["대출횟수"] >= 45)])

df["인기도"] = df["대출횟수"].apply(lambda x: "인기" if x >= 50 else "보통")
print("\n===인기도 열 추가 생성")
print(df)

sorted_df = df.sort_values("대출횟수", ascending=False).head(3)
print("\n===대출횟수 기준 내림차순 상위 3개 출력===")
print(sorted_df[["도서명", "분야", "대출횟수"]])

result2 = df.groupby("분야")["대출횟수"].mean()
result2.plot(kind="bar", title="분야별 평균 대출횟수 막대 그래프")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
print("\n===분야별 평균 대출횟수 막대 그래프===")