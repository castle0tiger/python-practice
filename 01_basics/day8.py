# with open("test.txt", "w", encoding="utf-8") as f:
#    f.write("안녕하세요\n")
#    f.write("Python 파일 입출력 테스트입니다.\n")

# with open("test.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())


# with open("test.txt", "a", encoding="utf-8") as f:
#    f.write("추가된 줄입니다.\n")

students = [
    {"name": "홍길동", "score": 85},
    {"name": "김철수", "score": 45},
    {"name": "이영희", "score": 72}
]

with open("result.txt", "w", encoding="utf-8") as f:
    for student in students:
        if student["score"] >= 60:
            f.write(f"{student['name']} : {student['score']}점 : 합격\n")
        else:
            f.write(f"{student['name']} : {student['score']}점 : 불합격\n")

