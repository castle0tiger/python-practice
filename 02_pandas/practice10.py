import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Malgun Gothic'

data = {
    "이름": ["김민준", "이수진", "박태양", "최하늘", "정지수", "강민서", "윤하은", "한소희"],
    "부서": ["개발", "마케팅", "개발", None, "마케팅", "개발", None, "마케팅"],
    "성과점수": [92, 78, None, 85, 91, None, 88, 76],
    "연봉": [7500, 5800, 6200, 7000, 6800, 5500, 6500, 5200]
}

df = pd.DataFrame(data)
print("\n===1.DataFrame 생성===")
print(df)

print("\n===2.결측값 예측하기===")
print(df.isnull().sum())

df["성과점수"] = df["성과점수"].fillna(df["성과점수"].mean())  # 평균으로 채울 때
df["부서"] = df["부서"].fillna("미배정")
print("\n===3.결측값 채우기 — 성과점수 빈 값은 평균으로, 부서 빈 값은 '미배정' 으로===")
print(df)

result = df.groupby("부서").agg({"성과점수":"sum", "연봉":"mean"})
print("\n===4.부서별 성과점수 합계, 평균 연봉 동시 출력===")
print(result)

print("\n===5.성과점수 80 이상이고 연봉 6000 이상인 직원 필터링===")
print(df[(df["성과점수"] >= 80) & (df["연봉"] >= 6000)])

df["등급"] = df["성과점수"].apply(lambda x: "S" if x >= 90 else "A" if x >= 80 else "B")
print("\n===6.등급 열 추가===")
print(df)

sorted_df = df.sort_values("연봉", ascending=False).head(3)
print("\n===7.연봉 기준 내림차순 상위 3개 출력 (이름, 부서, 성과점수, 연봉 열만)===")
print(sorted_df[["이름", "부서", "성과점수", "연봉"]])

result2 = df.groupby("부서")["성과점수"].mean()
result2.plot(kind="bar", title="부서별 평균 성과점수 막대 그래프")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
print("\n===8.부서별 평균 성과점수 막대 그래프===")