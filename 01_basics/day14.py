# import pandas as pd

# data = {
#     "이름": ["박민준", "최수진", "정태양", "강하늘", "김지수"],
#     "국어": [85, 92, 60, 45, 78],
#     "수학": [70, 88, 55, 90, 65],
#     "영어": [88, 95, 50, 75, 82]
# }

# def get_grade(score):
#     if score >= 270:
#         return "A"
#     elif score >= 240:
#         return "B"
#     elif score >= 210:
#         return "C"
#     else:
#         return "F"
    

# df = pd.DataFrame(data)
# df["총점"] = df["국어"] + df["수학"] + df["영어"]
# # df.to_csv("grade.csv", index=False, encoding="utf-8-sig")
# # print("저장 완료")
# # print(df)

# df2 = pd.read_csv("grade.csv", encoding="utf-8-sig")

# # print("===총점 통계===")
# # print(f"평균: {df2['총점'].mean():.1f}")
# # print(f"최고점: {df2['총점'].max()}")
# # print(f"최고점: {df2['총점'].min()}")

# df2["등급"] = df2["총점"].apply(get_grade)
# print(df2)

# print("|===합격자 (총점 210점 이상) ===")
# passed = df2[df2["총점"] >= 210]
# print(passed[["이름", "총점", "등급"]])

# passed.to_csv("passed.csv", index=False, encoding="utf-8-sig")
# print("합격자 명단 저장 완료")





# 미니 과제 _ 도서 판매 데이터 분석

import pandas as pd

data = {
    "도서명": ["파이썬 기초", "데이터분석", "머신러닝", "웹개발", "AI입문"],
    "카테고리": ["프로그래밍", "데이터", "AI", "프로그래밍", "AI"],
    "가격": [25000, 32000, 38000, 28000, 35000],
    "판매량": [120, 85, 60, 95, 110]
}

df = pd.DataFrame(data)
print(df)

df["매출"] = df["가격"] * df["판매량"]

# sum = 0
# for df[df["매출"]] in df["매출"]:
#     sum += df[df["매출"]]

print(f"전체 총매출: {df['매출'].sum()}")

print(f"평균 판매량: {df["판매량"].mean():.1f}")

print(f"매출 상위 3개 도서: {df.sort_values("매출", ascending=False).head(3)}")

df.to_csv("sales.csv", index=False, encoding="utf-8-sig")
print("CSV 파일 저장 완료")