# import math

# print(math.sqrt(16))    # 제곱근
# print(math.pi)          # 파이값
# print(math.ceil(3.2))   # 올림
# print(math.floor(3.8))  # 내림


# import random

# print(random.randint(1, 10))     # 1~10 사이 랜덤 정수
# print(random.choice(["가위", "바위", "보"]))  # 리스트에서 랜덤 선택


# from datetime import datetime

# now = datetime.now()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)

# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
# data = response.json()
# print(data)


## 미니 실습 과제 1

import random

choices = ["가위", "바위", "보"]
computer = random.choice(choices)
user = input("가위/바위/보 중 입력: ")

print(f"컴퓨터: {computer}")

if user == computer:
    print("비겼습니다!")
elif (user == "가위" and computer == "보") or \
     (user == "바위" and computer == "가위") or \
     (user == "보" and computer == "바위"):
    print("이겼습니다!")                             # 사용자가 이기는 조건 3가지
else:
    print("졌습니다.")
