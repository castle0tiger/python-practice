import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))

# print(arr + 10)      # 각 요소에 10 더하기
# print(arr * 2)       # 각 요소에 2 곱하기
# print(arr ** 2)      # 각 요소 제곱


# arr = np.array([85, 92, 60, 45, 78])

# print(np.mean(arr))   # 평균
# print(np.sum(arr))    # 합계
# print(np.max(arr))    # 최댓값
# print(np.min(arr))    # 최솟값
# print(np.std(arr))    # 표준편차


# matrix = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# print(matrix)
# print(matrix.shape)    # 배열 크기 (행, 열)
# print(matrix[0])       # 첫 번째 행
# print(matrix[0][1])    # 0번째 행, 1번째 열의 값


scores = np.array([85, 92, 60, 45, 78, 88, 55, 70])

print(np.max(scores))    # 최댓값
print(np.min(scores))    # 최솟값

mean = np.mean(scores)
print(scores[scores > mean])
