def common_elements(list1, list2):
    result = []

    for c in list1:
        if c in list2:
            result.append(c)

    return result


print(f"[1, 2, 3, 4], [3, 4, 5, 6] -> {common_elements([1, 2, 3, 4], [3, 4, 5, 6])}")
print(f"['a', 'b'], ['b', 'c'] -> {common_elements(['a', 'b'], ['b', 'c'])}")
print(f"[1, 2], [3, 4] -> {common_elements([1, 2], [3, 4])}")


## 실무적 피드백 _ "엣지 케이스(예외 상황)"를 떠올리는 감각"
# 만약 list1에 중복이 있으면?
# common_elements([3, 3, 4], [3, 4]) → [3, 3, 4]
# "공통 원소를 중복 없이" 원한다면 처리할 경우

# 방법 A _ 조건 추가
def common_elements_v2(list1, list2):
    result = []

    for c in list1:
        if c in list2 and c not in result:
            result.append(c)

    return result

print("\n")
print(f"[3, 3, 4], [3, 4] -> {common_elements_v2([3, 3, 4], [3, 4])}")


#방법 B _ set(집합) 쓰기
def common_elements_v3(list1, list2):
    return list(set(list1) & set(list2))

print("\n")
print(f"[1, 2, 3, 4], [3, 4, 5, 6] -> {common_elements_v3([1, 2, 3, 4], [3, 4, 5, 6])}")
print(f"[3, 3, 4], [3, 4] -> {common_elements_v3([3, 3, 4], [3, 4])}")
print(f"[1, 2], [3, 4] -> {common_elements_v3([1, 2], [3, 4])}")
