import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

data = {
    "고객명": ["김민준", "이수진", "박태양", "최하늘", "정지수", "강민서", "윤하은", "한소희"],
    "등급": ["VIP", "일반", "VIP", "일반", "골드", "골드", "일반", "VIP"],
    "구매횟수": [15, 3, 12, 5, 8, 9, 2, 18],
    "총구매금액": [850000, 120000, 680000, 200000, 450000, 520000, 80000, 950000],
    "반품횟수": [1, 0, 2, 1, 0, 1, 0, 2]
}

df = pd.DataFrame(data)
print("\n===DataFrame 만들고 출력===")
print(df)

df["순구매금액"] = df["총구매금액"] - (df["반품횟수"] * 50000)
print("\n===순구매금액 열 추가===")
print(df)

result = df.groupby("등급")[["구매횟수", "순구매금액"]].agg("mean")
print("\n===등급별 평균 구매횟수, 평균 순구매 동시 출력===")
print(result)

df["고객등급"] = df["순구매금액"].apply(lambda x: "우수" if x >= 500000 else "일반")
print("\n===고객등급 열 추가===")
print(df[["고객명", "고객등급"]])

df_vip = df[df["등급"] == "VIP"]
sorted_df_vip = df_vip.sort_values("순구매금액", ascending=False)
print("\n===VIP 고객만 필터링해서 순구매금액 내림차순 정렬===")
print(sorted_df_vip[["고객명", "구매횟수", "반품횟수", "순구매금액"]])

result2 = df.groupby("등급")["순구매금액"].mean()
result2.plot(kind="bar", title="등급별 평균 순구매금액 그래프")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
print("\n===등급별 평균 순구매금액 그래프===")