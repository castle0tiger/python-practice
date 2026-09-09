## 방법 1 : 센티넬로 초기값 설정 & 비교갱신하기
def tree_max(tree):
    biggest = None

    if biggest is None or tree["value"] > biggest:
        biggest = tree["value"]

    for node in tree["children"]:
        sub_biggest = tree_max(node)
        if sub_biggest > biggest:
            biggest = sub_biggest

    return biggest

print(tree_max({"value": 5, "children": []}))
print(tree_max({
    "value": 1,
    "children": [
        {"value": 7, "children": []},
        {"value": 3, "children": [
            {"value": 9, "children": []},
            {"value": 2, "children": []}
        ]}
    ]
}))
print("--------------------------------------")


## 방법 2 : 리스트에 value 값을 받은 다음 최대 찾기
def tree_max_v2(tree):
    result = []

    result.append(tree["value"])

    for node in tree["children"]:
        result.append(tree_max_v2(node))

    return max(result)

print(tree_max_v2({"value": 5, "children": []}))
print(tree_max_v2({
    "value": 1,
    "children": [
        {"value": 7, "children": []},
        {"value": 3, "children": [
            {"value": 9, "children": []},
            {"value": 2, "children": []}
        ]}
    ]
}))
print("--------------------------------------")


##피드백 : 센티넬은 안전한 시작값이 아예 없을때 사용하는 것!
def tree_max_improved(tree):
    biggest = tree["value"]

    for node in tree["children"]:
        sub_biggest = tree_max_improved(node)
        if sub_biggest > biggest:
            biggest = sub_biggest

    return biggest

print(tree_max_improved({"value": 5, "children": []}))
print(tree_max_improved({
    "value": 1,
    "children": [
        {"value": 7, "children": []},
        {"value": 3, "children": [
            {"value": 9, "children": []},
            {"value": 2, "children": []}
        ]}
    ]
}))