##  pandas 심화

# import pandas as pd

# data = {
#     "도서명": ["파이썬 기초", "데이터분석", "머신러닝", "웹개발", "AI입문"],
#     "카테고리": ["프로그래밍", "데이터", "AI", "프로그래밍", "AI"],
#     "가격": [25000, 32000, 38000, 28000, 35000],
#     "판매량": [120, 85, 60, 95, 110]
# }

# df = pd.DataFrame(data)

# result = df.groupby("카테고리")["판매량"].mean()
# print(result)

# result = df.groupby("카테고리")["판매량"].agg(["mean", "sum", "max"])
# print(result)



# df1 = pd.DataFrame({
#     "도서명": ["파이썬 기초", "데이터분석", "머신러닝"],
#     "가격": [25000, 32000, 38000]
# })

# df2 = pd.DataFrame({
#     "도서명": ["파이썬 기초", "데이터분석", "머신러닝"],
#     "판매량": [120, 85, 60]
# })

# merged = pd.merge(df1, df2, on="도서명")
# print(merged)




# import numpy as np

# df = pd.DataFrame({
#     "이름": ["홍길동", "김철수", "이영희", "박민준"],
#     "점수": [85, np.nan, 72, np.nan]
# })

# print(df)
# print(df["점수"].isna())         # 빈 값 확인
# df["점수"] = df["점수"].fillna(0)  # 빈 값을 0으로 채우기
# print(df)



## 실전 미니 과제

import pandas as pd

data = {
    "지역": ["서울", "부산", "서울", "대구", "부산", "서울"],
    "상품": ["A", "B", "A", "C", "B", "C"],
    "매출": [150, 200, 130, 180, 220, 160]
}

df = pd.DataFrame(data)
print(df)

result_1 = df.groupby("지역")["매출"].sum()
print("\n=== 지역별 총매출===")
print(result_1)

result_2= df.groupby("상품")["매출"].mean()
print("\n=== 상품별 평균매출 ===")
print(result_2)

print("\n=== 매출 100이상 150미만 ===")
print(df[(df["매출"]>= 100) & (df["매출"] < 150)])