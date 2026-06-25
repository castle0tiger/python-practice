import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

data = {
    "이름": ["김민준", "이수진", "박태양", "최하늘", "정지수", "강민서", "윤하은"],
    "등급": ["골드", "실버", "골드", "브론즈", "실버", "골드", "브론즈"],
    "월이용횟수": [22, 15, 18, 8, 12, 25, 5],
    "개인PT횟수": [4, 2, 0, 1, 3, 6, 0],
    "월회비": [80000, 50000, 80000, 30000, 50000, 80000, 30000]
}

print("\n=== Dataframe 생성 ===")
df = pd.DataFrame(data)
print(df)


df["총납부금액"] = (df["월회비"] + df["개인PT횟수"] * 50000)
print("\n=== 총납부금액 생성 ===")
print(df)


result = df.groupby("등급")["월이용횟수"].mean()
print("\n=== 등급별 평균 월이용횟수 ===")
print(result)


print("\n=== 월이용횟수 15회 이상 개인PT횟수 2회 이상 회원 ===")
print(df[(df["월이용횟수"] >= 15) & (df["개인PT횟수"] >= 2)])


sorted_df = df.sort_values("총납부금액", ascending=False).head(3)
print("\n=== 총납부금액 상위 3명 ===")
print(sorted_df[["이름", "등급" ,"총납부금액"]])


result2 = df.groupby("등급")["총납부금액"].mean()
result2.plot(kind="bar", title="등급별 평균 총납부금액")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()