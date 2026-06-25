# text = "Hello, Python!"

# print(len(text))        # 길이
# print(text.upper())     # 대문자
# print(text.lower())     # 소문자
# print(text.replace("Python", "World"))  # 치환

# print(text[0])       # 첫 번째 문자
# print(text[7:13])    # 7번째부터 12번째까지
# print(text[-1])      # 마지막 문자


# text = '사과,바나나,딸기,포도'

# fruits = text.split(",")
# print(fruits)
# print("바나나" in text)


# name = "캐슬타이거"
# score = 85

# print(f"{name}님의 점수는 {score}점입니다.")


# students = [
#     {"name": "홍길동", "score": 85},
#     {"name": "김철수", "score": 45},
#     {"name": "이영희", "score": 72}
# ]

# for student in students:
#     if student["score"] >= 60:
#         print(f"{student['name']}님의 점수는 {student['score']}점이며, 합격입니다.")
#     else :
#         print(f"{student['name']}님의 점수는 {student['score']}점이며, 불합격입니다.")



students = [
    {"name": "박민준", "score": 55},
    {"name": "최수진", "score": 91},
    {"name": "정태양", "score": 68},
    {"name": "강하늘", "score": 40}
]

total = 0
for student in students:
    total += student["score"]

average = total / len(students)


for student in students:
    if student["score"] >= 90:
        print(f"{student['name']}님의 점수는 {student['score']}점이며, 우수합격입니다.")
    elif student["score"] >= 60:
        print(f"{student['name']}님의 점수는 {student['score']}점이며, 합격입니다.")
    else:
        print(f"{student['name']}님의 점수는 {student['score']}점이며, 불합격입니다. 평균까지 {average - student['score']}점 부족합니다.")
