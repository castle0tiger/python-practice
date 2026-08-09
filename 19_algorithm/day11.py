def rank_names(students):
    result = []

    sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)

    for s_s in sorted_students:
        result.append(s_s["name"])

    return result

students = [
    {"name": "김철수", "score": 85},
    {"name": "이영희", "score": 92},
    {"name": "박민수", "score": 78},
]

print(rank_names(students))
print("")