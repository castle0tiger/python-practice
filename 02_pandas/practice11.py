import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

students = {
    "학생ID": [1, 2, 3, 4, 5, 6, 7, 8],
    "이름": ["김민준", "이수진", "박태양", "최하늘", "정지수", "강민서", "윤하은", "한소희"],
    "과목": ["수학", "영어", "수학", "과학", "영어", "과학", "수학", "영어"],
    "출석률": [98, 82, 91, 75, 95, 88, 70, 93],
    "수강료": [150000, 120000, 150000, 130000, 120000, 130000, 150000, 120000]
}

scores = {
    "학생ID": [1, 2, 3, 4, 5, 6, 7, 8],
    "중간고사": [95, None, 88, 72, 91, None, 65, 89],
    "기말고사": [92, 85, None, 78, 94, 80, None, 91],
    "평점": [4.9, 4.3, 4.7, 4.1, 4.8, 4.5, 3.9, 4.6]
}

print("\n===1.DataFrame 생성 후 각각 출력===")

df1 = pd.DataFrame(students)
print(df1)

print("\n")

df2 = pd.DataFrame(scores)
print(df2)

df = pd.merge(df1, df2, on="학생ID")
print("\n===2.두 개의 DataFrame을 학생ID 기준으로 합치기===")
print(df)

print("\n===3.isnull().sum() 결측값 확인 예측하기===")
print(df.isnull().sum())

df["중간고사"] = df["중간고사"].fillna(df["중간고사"].mean())  # 평균으로 채울 때
df["기말고사"] = df["기말고사"].fillna(0)
print("\n===4.결측값 채우기 — 중간고사 빈 값은 평균으로, 기말고사 빈 값은 0 ===")
print(df)

result = df.groupby("과목").agg({"수강료" : "sum", "평점" : "mean"})
print("\n===5.과목별 수강료 합계, 평균 평점 동시 출력===")
print(result)

print("\n===6.출석률 85 이상이고 평점 4.5 이상인 학생 필터링===")
print(df[(df["출석률"] >= 85) & (df["평점"] >= 4.5)])

df["출석등급"] = df["출석률"].apply(lambda x: "우수" if x >= 95 else "양호" if x >= 85 else "미흡")
print("\n===7.출석등급 열 추가===")
print(df)

sorted_df = df.sort_values("평점", ascending=False).head(3)
print("\n===8.평점 기준 내림차순 상위 3개 출력 (이름, 과목, 출석률, 평점 열만)===")
print(sorted_df[["이름", "과목", "출석률", "평점"]])

print("\n===9.과목별 평균 평점 막대 그래프===")
result2 = df.groupby("과목")["평점"].mean()
result2.plot(kind="bar", title="과목별 평균 평점 막대 그래프")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
