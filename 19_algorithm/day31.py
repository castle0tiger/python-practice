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
