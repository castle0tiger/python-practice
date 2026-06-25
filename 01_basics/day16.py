# import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm
# import pandas as pd

# # 한글 폰트 설정
# plt.rcParams['font.family'] = 'Malgun Gothic'

## 막대 그래프(bar)
# categories = ["파이썬 기초", "데이터분석", "머신러닝", "웹개발", "AI입문"]
# sales = [120, 85, 60, 95, 110]

# plt.bar(categories, sales)
# plt.title("도서별 판매량")
# plt.xlabel("도서명")
# plt.ylabel("판매량")
# plt.show()


## 꺽은 선 그래프(line)
# months = [1, 2, 3, 4, 5, 6]
# revenue = [1200, 1500, 1300, 1800, 2000, 1700]

# plt.plot(months, revenue, marker="o")
# plt.title("월별 매출 추이")
# plt.xlabel("월")
# plt.ylabel("매출")
# plt.show()

## 파이 차트(pie)
# labels = ["프로그래밍", "데이터", "AI"]
# sizes = [215, 85, 170]

# plt.pie(sizes, labels=labels, autopct="%1.1f%%")
# plt.title("카테고리별 판매 비중")
# plt.show()

# df = pd.DataFrame({
#     "도서명": ["파이썬 기초", "데이터분석", "머신러닝", "웹개발", "AI입문"],
#     "판매량": [120, 85, 60, 95, 110]
# })


# df.plot(kind="bar", x="도서명", y="판매량", title="도서별 판매량")
# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.show()


## 미니 실습 과제

# import pandas as pd
# import matplotlib.pyplot as plt

# plt.rcParams['font.family'] = 'Malgun Gothic'

# data = {
#     "월": [1, 2, 3, 4, 5, 6],
#     "온라인": [1200, 1500, 1300, 1800, 2000, 1700],
#     "오프라인": [800, 750, 900, 850, 780, 950]
# }

# df = pd.DataFrame(data)

# df["총매출"] = df["온라인"] + df["오프라인"]
# print(df)

# df.plot(kind="line", x="월", y="총매출", title="월별 총매출", marker="o")

# df.plot(kind="bar", x="월", y=["온라인", "오프라인"])

# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.show()

# print(f"총매출 가장 높은 달: {df.loc[df['총매출'].idxmax(), '월']}월")



