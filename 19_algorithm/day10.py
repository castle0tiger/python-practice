def grade_report(scores):
    result = {}

    passer = 0
    highest = scores[0]
    total = 0

    for score in scores:
        if score >= 60:
            passer += 1

        if highest < score:
            highest = score

        total += score
    average = total/len(scores)

    result["합격자수"] = passer
    result["최고점"] = highest
    result["평균"] = average

    return result

print(f"[85, 45, 70, 30, 90, 60] -> {grade_report([85, 45, 70, 30, 90, 60])}")
print(f"[17, 56, 78, 99, 100, 87, 45] -> {grade_report([17, 56, 78, 99, 100, 87, 45])}")



