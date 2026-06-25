import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

data = {
    "영화명": ["인터스텔라", "어벤져스", "기생충", "타이타닉", "조커", "라라랜드", "매트릭스"],
    "장르": ["SF", "액션", "드라마", "드라마", "드라마", "뮤지컬", "SF"],
    "관람객수": [1500, 2200, 1800, 1200, 1600, 900, 1100],
    "평점": [4.8, 4.5, 4.9, 4.3, 4.6, 4.7, 4.4],
    "상영시간": [169, 143, 132, 194, 122, 128, 136]
}

df = pd.DataFrame(data)
print("\n===DataFrame 생성 출력===")
print(df)

result = df.groupby("장르")[["관람객수", "평점"]].agg("mean")
print("\n===장르별 평균 관람객수, 평균 평점 동시 출력===")
print(result)

print("\n===평점 4.5 이상이고 관람객수 1500 이상인 영화 필터링===")
print(df[(df["평점"] >= 4.5) & (df["관람객수"] >= 1500)])

df["추천등급"] = df["평점"].apply(lambda x: "강력추천" if x >= 4.7 else "추천" if x >= 4.5 else "보통" )
print("\n===추천등급 열 추가 생성===")
print(df)

sorted_df = df.sort_values("관람객수", ascending=False).head(3)
print("\n===관람객수 기준 내림차순 상위 3개 출력===")
print(sorted_df[["영화명", "장르", "관람객수", "평점"]])

result2 = df.groupby("장르")["관람객수"].mean()
result2.plot(kind="bar", title="장르별 평균 관람객수 막대 그래프")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
print("\n===장르별 평균 관람객수 막대 그래프===")
