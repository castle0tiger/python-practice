import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

## 연습 문제1 

# data = {
#     "주문번호": [1, 2, 3, 4, 5, 6, 7, 8],
#     "카테고리": ["의류", "전자", "의류", "식품", "전자", "식품", "의류", "전자"],
#     "가격": [35000, 120000, 28000, 15000, 89000, 22000, 45000, 200000],
#     "수량": [2, 1, 3, 5, 1, 4, 2, 1],
#     "반품여부": [False, False, True, False, True, False, False, False]
# }

# # 1. DataFrame 만들고 출력
# df = pd.DataFrame(data)
# print(df)

# # 2. "총금액" 열 추가(가격 x 수량)
# df["총금액"] = df["가격"] * df["수량"]

# # 3. 카테고리별 총금액 합계 출력
# result = df.groupby("카테고리")["총금액"].sum()
# print(result)

# # 4. 반품된 주문만 필터링해서 출력
# print(df[df["반품여부"] == True])

# # 5. 총금액 기준 내림차순 정렬 후 상위 3개 출력
# top3 = df.sort_values("총금액", ascending=False).head(3)
# print(top3[["주문번호", "총금액"]])

# # 5. 부서별 평균 매출 막대 그래프
# result.plot(kind="bar", title="카테고리별 총금액")
# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.show()


## 연습문제 2

data = {
    "이름": ["김민준", "이수진", "박태양", "최하늘", "정지수"],
    "부서": ["개발", "마케팅", "개발", "영업", "마케팅"],
    "출근일수": [22, 18, 20, 15, 21],
    "지각횟수": [1, 3, 0, 5, 2],
    "초과근무시간": [10, 5, 15, 3, 8]
}

df = pd.DataFrame(data)

df["근태점수"] = (df["출근일수"] * 2) - (df["지각횟수"] * 3) + df["초과근무시간"]
print(df)

result = df.groupby("부서")["근태점수"].mean()
print(result)

print(df[df["근태점수"] >= 40])

sorted_df = df.sort_values("근태점수", ascending=False)
print(sorted_df[["이름", "부서" ,"근태점수"]])

result.plot(kind="bar", title="근태점수 그래프")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()