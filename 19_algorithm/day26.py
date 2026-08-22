def max_depth(input):
    layer = 0
    layers = []

    for i in input:
        if isinstance(i, list) == True:
            layer = 1 + max_depth(i)
            layers.append(layer)
        else:
            layer = 1
            layers.append(1)

    return max(layers)

print(max_depth([1, 2, 3]))
print(max_depth([1, [2, 3]]))
print(max_depth([1, [2, [3, 4]]]))
print(max_depth([1, [2, [3, [4]]]]))
print(max_depth([[1], [2, [3]]]))
print("최대 깊이 찾기 오류 테스트")
print(max_depth([[2, [3]], [1]]))
print("")

## 피드백 코드 효율화

def max_depth_v2(input):
    layers = []

    for i in input:
        if isinstance(i, list):
            layers.append(1 + max_depth(i))
        else:
            layers.append(1)

    return max(layers)

print(max_depth_v2([[2, [3]], [1]]))


## 