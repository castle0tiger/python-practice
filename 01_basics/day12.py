# import pandas as pd

# data = { "이름": ["홍길동", "김철수", "이영희"],
#         "점수": [85, 45, 72],
#         "합격": [True, False, True]
# }

# df = pd.DataFrame(data)

# print(df)

# print(df["이름"])        # 특정 열 조회
# print(df["점수"].mean()) # 평균
# print(df["점수"].max())  # 최댓값
# print(df["점수"].min())  # 최솟값

# print(df[df["점수"] >= 60])

# df["등급"] = df["점수"].apply(lambda x: "합격" if x >= 60 else "불합격")
# # print(df)

# # 저장하기
# df.to_csv("students.csv", index=False, encoding="utf-8-sig")
# print("저장 완료")

# # 불러오기
# df2 = pd.read_csv("students.csv", encoding="utf-8-sig")
# print(df2)



## 실전 미니 과제 1

import pandas as pd

data = {
    "이름": ["박민준", "최수진", "정태양", "강하늘", "김지수"],
    "국어": [85, 92, 60, 45, 78],
    "수학": [70, 88, 55, 90, 65]
}

df = pd.DataFrame(data)

print(df)  #DataFrame 출력
print(df["국어"].mean()) # 국어 평균
print(df["수학"].mean()) # 수학 평균
df["총점"] = df["국어"] + df["수학"] # "총점" 열 추가 (국어 + 수학)
print(df[df["총점"] >= 150])  # 총점 150 이상인 학생만 필터링해서 출력


