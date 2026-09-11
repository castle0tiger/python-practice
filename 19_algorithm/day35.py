def tree_search(tree, target):

    if tree["value"] == target:
        return True

    else:
        if tree["children"]:
            for node in tree["children"]:
               if tree_search(node, target): # if tree_search(node, target) == True:
                   return True

    return False


print(tree_search({"value": 5, "children": []}, 5))
print(tree_search({
    "value": 1,
    "children": [
        {"value": 7, "children": []},
        {"value": 3, "children": [
            {"value": 9, "children": []},
            {"value": 2, "children": []}
        ]}
    ]
}, 9))
print(tree_search({
    "value": 1,
    "children": [
        {"value": 7, "children": []},
        {"value": 3, "children": [
            {"value": 9, "children": []},
            {"value": 2, "children": []}
        ]}
    ]
}, 100))
print("---------------------------------------")

## any 사용하는 문법
def tree_search_v2(tree, target):
    return tree["value"] == target or any(tree_search(node, target) for node in tree["children"])

print(tree_search_v2({"value": 5, "children": []}, 5))
print(tree_search_v2({
    "value": 1,
    "children": [
        {"value": 7, "children": []},
        {"value": 3, "children": [
            {"value": 9, "children": []},
            {"value": 2, "children": []}
        ]}
    ]
}, 9))
print(tree_search_v2({
    "value": 1,
    "children": [
        {"value": 7, "children": []},
        {"value": 3, "children": [
            {"value": 9, "children": []},
            {"value": 2, "children": []}
        ]}
    ]
}, 100))



## 이해를 위한 동작구조
# tree_search(1, 9)                     1==9? 아니오 → children 순회 시작
#  │
#  ├─ node=7 → tree_search(7, 9)        7==9? 아니오 → children=[] → return False
#  │            if False: (통과 안 됨) → 다음 형제로
#  │
#  ├─ node=3 → tree_search(3, 9)        3==9? 아니오 → children 순회 시작
#  │            │
#  │            ├─ node=9 → tree_search(9, 9)   9==9? 예! → return True   ─┐
#  │            │                                                          │
#  │            │   if True:     ◄─────────────────────────────────────────┘
#  │            │      return True   ★ (3의 프레임, 여기서 즉시 끝)
#  │            │
#  │            └─ node=2 →  (실행 안 됨! 이미 return True로 빠져나감)
#  │
#  │   if True:  ◄─────────────── (3이 돌려준 True를 1이 받음)
#  │      return True   ★ (1의 프레임도 즉시 끝)
#  │
#  └─ 최종 결과: True


## 새로운 문법 이해
# any(iterable)
# iterable 안에 하나라도 참(True)인 게 있으면 True, 하나도 없으면 False. (형제 격인 all()은 반대로 "전부 다 참이어야 True".)


# any([False, False, True])   # True  (하나라도 참이 있음)
# any([False, False, False])  # False (참이 하나도 없음)
# any([])                     # False (빈 걸 넣으면 무조건 False — 자식 없는 노드에서 중요!)