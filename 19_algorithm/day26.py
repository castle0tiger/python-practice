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


## 동작구조 시각화
# 회의실 A: max_depth([1, [2,[3,4]]])
#   layers_A = []
#   │ 1 → 숫자 → layers_A.append(1)              layers_A = [1]
#   │ [2,[3,4]] → 리스트 → 1 + max_depth([2,[3,4]]) 호출
#   │              │
#   │              회의실 B: max_depth([2,[3,4]])
#   │                layers_B = []                ← B만의 layers! (A랑 별개)
#   │                │ 2 → 숫자 → layers_B.append(1)        layers_B = [1]
#   │                │ [3,4] → 리스트 → 1 + max_depth([3,4]) 호출
#   │                │          │
#   │                │          회의실 C: max_depth([3,4])
#   │                │            layers_C = []   ← C만의 layers!
#   │                │            3 → layers_C.append(1)     layers_C = [1]
#   │                │            4 → layers_C.append(1)     layers_C = [1,1]
#   │                │            return max([1,1]) = 1   ──┐  ★ C가 max 구함
#   │                │   1 + 1 = 2 ←────────────────────────┘
#   │                │ layers_B.append(2)          layers_B = [1, 2]
#   │                return max([1,2]) = 2   ──────┐  ★ B가 max 구함
#   │ 1 + 2 = 3 ←──────────────────────────────────┘
#   │ layers_A.append(3)                    layers_A = [1, 3]
#   return max([1,3]) = 3   ★ A가 max 구함

# 재귀 함수 안의 코드(layers 만들고 max 뽑기)는,
# 파고드는 층마다 "통째로 새로" 실행된다.
# 각 층은 자기 layers에서 자기 max를 구해, 그 값 하나를 위층에 올린다.
