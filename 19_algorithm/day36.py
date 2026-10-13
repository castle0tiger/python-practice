## Tree 개념 복습 (day34과 유사하지만 좀 다른)
def tree_count_leaves(tree):
    leaves = 0

    if tree["children"]:
        for node in tree["children"]:
            leaves += tree_count_leaves(node)

    else:
        leaves = 1

    return leaves


print(tree_count_leaves({"value": 5, "children": []}))
print(tree_count_leaves({
    "value": 1,
    "children": [
        {"value": 7, "children": []},
        {"value": 3, "children": [
            {"value": 9, "children": []},
            {"value": 2, "children": []}
        ]}
    ]
}))
