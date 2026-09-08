def tree_sum(tree):
    total = 0

    total += tree["value"]

    for node in tree["children"]:
        total += tree_sum(node)  #node는 딕셔너리 노드 그 자체

    return total


print(tree_sum({"value": 1, "children": []}))
print(tree_sum({
    "value": 1,
    "children": [
        {"value": 2, "children": []},
        {"value": 3, "children": [
            {"value": 4, "children": []},
            {"value": 5, "children": []}
        ]}
    ]
}))
print("")


## 피드백 : 더 나은 방식
def tree_sum_v2(tree):
    return tree["value"] + sum(tree_sum(child) for child in tree["children"])


print(tree_sum_v2({"value": 1, "children": []}))
print(tree_sum_v2({
    "value": 1,
    "children": [
        {"value": 2, "children": []},
        {"value": 3, "children": [
            {"value": 4, "children": []},
            {"value": 5, "children": []}
        ]}
    ]
}))


## 동작구조 시각화
# tree_sum(1)                              total=0 → +1 → total=1
#  ├─ for node in [2, 3]:
#  │   node=2 → tree_sum(2)                total=0 → +2 → total=2
#  │              children=[] → for 안 돔
#  │              return 2    ────────────────┐
#  │                                          │
#  │   (1의 total) += 2  →  total = 3  ◄──────┘
#  │
#  │   node=3 → tree_sum(3)                total=0 → +3 → total=3
#  │              for node in [4, 5]:
#  │                node=4 → tree_sum(4)   total=0 → +4 → total=4
#  │                           return 4  ──────┐
#  │                (3의 total) += 4 → 7  ◄────┘
#  │
#  │                node=5 → tree_sum(5)   total=0 → +5 → total=5
#  │                           return 5  ──────┐
#  │                (3의 total) += 5 → 12 ◄────┘
#  │
#  │              return 12   ───────────────────┐
#  │                                             │
#  │   (1의 total) += 12  →  total = 15  ◄───────┘
#  │
#  └─ return 15
