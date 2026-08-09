def rank_names(students):
    result = []

    sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)

    for s in sorted_students:
        result.append(s["name"])

    return result

students = [
    {"name": "김철수", "score": 85},
    {"name": "이영희", "score": 92},
    {"name": "박민수", "score": 78},
]

print(rank_names(students))
print("")


## 피드백 : 실무자의 간결 버젼 _ 리스트 컴프리헨션
def rank_names_v2(students):
    return [s["name"] for s in sorted(students, key=lambda x: x["score"], reverse=True)]

print("리스트 컴프리헨션 결과값 ->")
print(rank_names_v2(students))
print("")