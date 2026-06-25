# Day 1~4: Python 기초

# 변수
name = "홍길동"
score = 85
is_pass = True

# 조건문
if score >= 60:
    print("합격")
elif score >= 40:
    print("재시험")
else:
    print("불합격")

# 반복문
for i in range(1, 6):      # 1~5
    print(i)

count = 0
while count < 5:
    count += 1

# 함수
def add(a, b):
    return a + b

result = add(3, 5)   # 8


# Day 5~6: 리스트 / 딕셔너리

# 리스트 — 순서 있는 데이터
scores = [85, 92, 78]
scores[0]          # 85
scores.append(100) # 추가
scores.remove(78)  # 삭제
len(scores)        # 길이

# 딕셔너리 — key:value 쌍
student = {"name": "홍길동", "score": 85}
student["name"]        # 접근
student["grade"] = "B" # 추가/수정

# 조합 패턴 (가장 많이 씀)
for student in students:
    print(student["name"])


# Day 7~9: 문자열 / 파일 / 에러처리

# 문자열
text = "Hello Python"
text.upper()           # 대문자
text.replace("Hello", "Hi")
text.split(",")        # 분리
f"{name}님 {score}점"  # f-string

# 파일
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("내용\n")

with open("test.txt", "r", encoding="utf-8") as f:
    print(f.read())

# 에러처리
try:
    number = int(input())
except ValueError:
    print("숫자만 입력하세요")


# Day 10: 클래스

class Student:
    def __init__(self, name, score):  # 초기화
        self.name = name
        self.score = score

    def check_pass(self):             # 메서드
        return "합격" if self.score >= 60 else "불합격"

s1 = Student("홍길동", 85)
s1.check_pass()   # "합격"


# Day 12~13: pandas / numpy

import pandas as pd
import numpy as np

# DataFrame 생성
df = pd.DataFrame({"이름": ["홍길동"], "점수": [85]})

# 기본 조작
df["점수"].mean()          # 평균
df[df["점수"] >= 60]       # 필터링
df["등급"] = df["점수"].apply(lambda x: "A" if x >= 90 else "B")

# groupby
df.groupby("부서")["매출"].mean()

# CSV
df.to_csv("file.csv", index=False, encoding="utf-8-sig")
df = pd.read_csv("file.csv", encoding="utf-8-sig")

# numpy
arr = np.array([1, 2, 3, 4, 5])
arr * 2            # 전체 연산
np.mean(arr)       # 평균
arr[arr > 3]       # 필터링


# Day 16: matplotlib

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

# 막대
plt.bar(x, y)

# 꺾은선
plt.plot(x, y, marker="o")

# 파이
plt.pie(sizes, labels=labels, autopct="%1.1f%%")

# DataFrame으로 바로
df.plot(kind="bar", x="열", y="열", title="제목")

plt.show()


















































































import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

data = {
    "이름": ["김민준", "이수진", "박태양", "최하늘", "정지수", "강민서"],
    "부서": ["영업", "개발", "영업", "마케팅", "개발", "마케팅"],
    "매출": [850, 920, 630, 450, 780, 880],
    "고객수": [42, 38, 25, 18, 35, 40]
}

# 1. DataFrame 생성
df = pd.DataFrame(data)
print(df)

# 2. 성과점수 열 추가 (소수점 1자리)
df["성과점수"] = (df["매출"] / df["고객수"]).round(1)

# 3. 부서별 평균 매출
result = df.groupby("부서")["매출"].mean()
print(result)

# 4. 성과점수 상위 3명
top3 = df.sort_values("성과점수", ascending=False).head(3)
print(top3[["이름", "성과점수"]])

# 5. 부서별 평균 매출 막대 그래프
result.plot(kind="bar", title="부서별 평균 매출")
plt.tight_layout()
plt.show()
