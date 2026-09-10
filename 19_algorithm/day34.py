## 방법 1 : 초기값 자체를 1로 지정
def tree_count(tree):
    result = 1

    if tree["children"]:
        for node in tree["children"]:
            result += tree_count(node)
    else: 
        result = 1 #초기값을 1로 설정하면 죽은 코드, 삭제해도 전혀 문제없음

    return result

print("방법 1 결과")
print(tree_count({"value": 5, "children": []}))
print(tree_count({
    "value": 1,
    "children": [
        {"value": 7, "children": []},
        {"value": 3, "children": [
            {"value": 9, "children": []},
            {"value": 2, "children": []}
        ]}
    ]
}))
print(tree_count({
    "value": 1,
    "children": [
        {"value": 7, "children": []},
        {"value": 3, "children": [
            {"value": 9, "children": []},
            {"value": 2, "children": []},
            {"value": 5, "children": []}
        ]}
    ]
}))
print("")


## 방법 2 : 초기값도 value 여부로 확인하고 누적, But 코드 복잡해지고 연산 늘어서 비효율
def tree_count_v2(tree):
    result = 0

    if tree["value"]: 
        result += 1

    if tree["children"]:
        for node in tree["children"]:
            result += tree_count_v2(node)
    else: 
        result = 1

    return result

print("방법 2 결과")
print(tree_count_v2({"value": 5, "children": []}))
print(tree_count_v2({
    "value": 1,
    "children": [
        {"value": 7, "children": []},
        {"value": 3, "children": [
            {"value": 9, "children": []},
            {"value": 2, "children": []}
        ]}
    ]
}))
print(tree_count_v2({
    "value": 1,
    "children": [
        {"value": 7, "children": []},
        {"value": 3, "children": [
            {"value": 9, "children": []},
            {"value": 2, "children": []},
            {"value": 5, "children": []}
        ]}
    ]
}))


## 피드백 : if / if-else vs if-elif-else 차이
# 1) if / if-else
# 각 두 개의 if는 서로 아무 상관 없음. 첫 번째 if가 참이든 거짓이든, 두 번째 if는 무조건 또 검사
    # if tree["value"]:
    #     result += 1
    #               # ← 여기서 첫 번째 if 완전히 끝남

    # if tree["children"]:      # ← 완전히 별개의 새로운 검사
    #     ...
    # else:
    #     ...

# 2) if-elif-else
# 하나의 묶음(체인). 셋 중 딱 하나의 블록만 실행
# if tree["value"]:
#     result += 1
# elif tree["children"]:    # ← 위 if가 "거짓"일 때만 검사함
#     ...
# else:
#     ...
