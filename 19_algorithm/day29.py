## 레이어(리스트안에 리스트)마다 큰 수를 result에 담아 max()로 최대값 추출
def nested_max(input):
    result = []

    for i in input:
        if isinstance(i, list):
            result.append(nested_max(i))
        else:
            result.append(i)

    return max(result)

print(nested_max([3, 1, 2]))
print(nested_max([1, [2, 3], 4]))
print(nested_max([1, [2, [9, 4]], 5]))
print(nested_max([[10, 2], [3, [4, 5]]]))
print(nested_max([[[7]]]))
print("")


## 평탄화한 후 바깥에서 max()로 최대값 추출
def flatten(input):
    result = []

    for i in input:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)

    return result

print(max(flatten([3, 1, 2])))
print(max(flatten(([1, [2, 3], 4]))))
print(max(flatten([1, [2, [9, 4]], 5])))
print(max(flatten([[10, 2], [3, [4, 5]]])))
print(max(flatten([[[7]]])))
print("")


## 평탄화 함수를 최대값 뽑는 함수로 감싸는 방법도 있음
def nested_max_v2(input):
    return max(flatten(input))   # 평탄화한 걸 max

print(nested_max_v2([3, 1, 2]))
print(nested_max_v2([1, [2, 3], 4]))
print(nested_max_v2([1, [2, [9, 4]], 5]))
print(nested_max_v2([[10, 2], [3, [4, 5]]]))
print(nested_max_v2([[[7]]]))
print("")

## 교훈 _ 실무 설계 원칙
# 설계가 어렵고 복잡하다면, "한 함수가 다 하려 하지 말고 나눠라"