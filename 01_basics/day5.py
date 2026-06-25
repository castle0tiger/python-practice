# scores = [85, 92, 78, 60, 45]

# for score in scores:
#    print(score)

# print(len(scores))  # 리스트의 길이
# scores.append(100)  # 리스트에 요소 추가
# print(scores)  # 요소가 추가된 리스트 출력
# scores.remove(45)  # 리스트에서 요소 제거
# print(scores)  # 요소가 제거된 리스트 출력

# for score in scores:
#     if score >= 60:
#         print(score, "합격")
#     else:
#         print(score, "불합격")


## 실전 미니 과제 _ 1

scores = [85, 92, 78, 60, 45]
total = 0
count = 0

for score in scores:
    total += score
    if score >= 60:
        count += 1

print("합격자 수:", count)
print("전체 평균:", total / len(scores))
    