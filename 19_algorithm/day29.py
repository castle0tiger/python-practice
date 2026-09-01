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


## 평탄화한 후 max()로 최대값 추출
def nested_max_v2(input):
    result = []

    for i in input:
        if isinstance(i, list):
            result.extend(nested_max_v2(i))
        else:
            result.append(i)

    return result

print(nested_max_v2([3, 1, 2]))
print(nested_max_v2([1, [2, 3], 4]))
print(nested_max_v2([1, [2, [9, 4]], 5]))
print(nested_max_v2([[10, 2], [3, [4, 5]]]))
print(nested_max_v2([[[7]]]))
