def average_scores(students):
    result = {}

    for student in students:
        total = 0
        for score in student["scores"]:
            total += score

        average = total / len(student["scores"])
        result[student["name"]] = average

    return result

    
students = [
    {"name": "김철수", "scores": [80, 90, 100]},
    {"name": "이영희", "scores": [70, 80]},
    {"name": "박민수", "scores": [100, 100, 100, 100]},
]

print(average_scores(students))



