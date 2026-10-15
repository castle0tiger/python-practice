def tree_values_at_depth(tree, depth):
    result = []

    if depth == 1:
        return [tree["value"]]

    else:
        for node in tree["children"]:
            result.extend(tree_values_at_depth(node, depth - 1))
    
    return result

tree = {
    "value": 1,
    "children": [
        {"value": 7, "children": []},
        {"value": 3, "children": [
            {"value": 9, "children": []},
            {"value": 2, "children": []}
        ]}
    ]
}

print(tree_values_at_depth(tree, 1))
print(tree_values_at_depth(tree, 2))
print(tree_values_at_depth(tree, 3))


## 프로세스 도식화
# tree_values_at_depth(1, depth=3)        depth≠1 → result=[] 로 시작
#  │
#  ├─ node=7 → tree_values_at_depth(7, depth=2)     depth≠1 → result=[] 로 시작
#  │             │  (7의 children=[] → for 루프 한 번도 안 돎)
#  │             └─ return []          ─────────────────┐
#  │                                                    │
#  │   result.extend([])  ◄─────────────────────────────┘
#  │   → result = []   (7 쪽에서는 아무것도 못 건짐)
#  │
#  ├─ node=3 → tree_values_at_depth(3, depth=2)     depth≠1 → result=[] 로 시작
#  │             │
#  │             ├─ node=9 → tree_values_at_depth(9, depth=1)   depth==1! → return [9]   ─┐
#  │             │                                                                        │
#  │             │   result.extend([9])     ◄─────────────────────────────────────────────┘
#  │             │   → result = [9]
#  │             │
#  │             ├─ node=2 → tree_values_at_depth(2, depth=1)   depth==1! → return [2]   ─┐
#  │             │                                                                        │
#  │             │   result.extend([2])     ◄─────────────────────────────────────────────┘
#  │             │   → result = [9, 2]
#  │             │
#  │             └─ return [9, 2]   ──────────────────────────────┐
#  │                                                              │
#  │   result.extend([9, 2])  ◄───────────────────────────────────┘
#  │   → result = [9, 2]
#  │
#  └─ return [9, 2]        ★ 최종 결과
