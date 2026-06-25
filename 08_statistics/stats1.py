import pandas as pd

data = {
    "이름": ["김철수", "이영희", "박민준", "최지아", "정우성"],
    "공부시간": [2, 5, 1, 8, 4],
    "시험점수": [55, 80, 40, 95, 70],
    "결석횟수": [3, 1, 5, 0, 2]
}

df = pd.DataFrame(data)

print("=== 기본 통계 ===")
print(df[["공부시간", "시험점수", "결석횟수"]].describe())

print("\n=== 상관관계 ===")
print(df[["공부시간", "시험점수", "결석횟수"]].corr())



import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

# 산점도: 공부시간 vs 시험점수
plt.figure(figsize=(8, 5))
plt.scatter(df["공부시간"], df["시험점수"], color="blue", s=100)

for i, row in df.iterrows():
    plt.annotate(row["이름"], (row["공부시간"], row["시험점수"]), textcoords="offset points", xytext=(5, 5))

plt.xlabel("공부시간")
plt.ylabel("시험점수")
plt.title("공부시간 vs 시험점수 (상관관계: 0.98)")
plt.tight_layout()
plt.savefig("stats_scatter.png")
plt.close()

print("그래프 저장 완료: stats_scatter.png")