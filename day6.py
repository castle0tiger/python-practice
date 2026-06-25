# student = {"name":"캐슬타이거", "score":85, "grade":"B"}

# student["grade"] = "B"      # 새 키 추가

# for key, value in student.items():
#     print(key, ":", value)

# students = [
#     {"name": "홍길동", "score": 85},
#     {"name": "김철수", "score": 45},
#     {"name": "이영희", "score": 72}
# ]

# for student in students:
#     if student["score"] >= 60:
#         print(student["name"], ":", "합격")
#     else:
#         print(student["name"], ":","불합격")


students = [
    {"name": "박민준", "score": 55},
    {"name": "최수진", "score": 91},
    {"name": "정태양", "score": 68},
    {"name": "강하늘", "score": 40}
]

for student in students:
    if student["score"] >= 90:
        print(student["name"], ":", student["score"], ":", "우수")
    elif student["score"] >= 60:
        print(student["name"], ":", student["score"], ":", "합격")
    else :
        print(student["name"], ":", student["score"], ":", "불합격")