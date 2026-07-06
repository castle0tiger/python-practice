# 과제 1: 학생 성적 관리

# 요구사항 : 요구사항:

# 학생 3명의 정보를 담아라. 각 학생은 이름과 점수를 가진다.
# 전체 학생의 평균 점수를 계산해서 출력하라.
# 평균 이상인 학생의 이름만 출력하라.
# 출력 예시:

# 평균: 82.3
# 평균 이상: 김철수
# 평균 이상: 박영희

# 예시 답안
# students = [
#     {"name": "김철수", "score": 85},
#     {"name": "박영희", "score": 78},
#     {"name": "이민수", "score": 92}
# ]

# average = sum(student["score"] for student in students) / len(students)
# print("평균:", average)


# print("평균 이상:")
# for student in students:
#     if student["score"] >= average:
#         print(f"  {student['name']}")


students = [
     {"name": "김철수", "score": 85, "absence":1},
     {"name": "박영희", "score": 78, "absence":2},
     {"name": "이민수", "score": 92, "absence":0},
     {"name": "최수현", "score": 68, "absence":3}
 ]

highest_score = 0
highest_name = ""

for student in students: 
    if student["score"] > highest_score:
        highest_score = student["score"]
        highest_name = student["name"]
        

print(f"최고점: {highest_name} ({highest_score})")


for student in students:
    if student["score"] >= 80 and student["absence"] <= 2:
        print(f"합격: {student['name']}")

