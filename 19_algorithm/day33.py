def tree_depth(tree):
    layers = []
    
    if tree["children"]:
        for node in tree["children"]:
            layers.append(tree_depth(node) + 1) 
    else:
        layers.append(1) # 자식이 없으면 1층

    return max(layers)

print(tree_depth({"value": 5, "children": []}))
print(tree_depth({
    "value": 1,
    "children": [
        {"value": 7, "children": []},
        {"value": 3, "children": [
            {"value": 9, "children": []},
            {"value": 2, "children": []}
        ]}
    ]
}))
print("")


## 피드백 : 더 나은 방식(더 짧게 쓰면)
def tree_depth(tree):
    if not tree["children"]:
        return 1
    return 1 + max(tree_depth(node) for node in tree["children"])


print(tree_depth({"value": 5, "children": []}))
print(tree_depth({
    "value": 1,
    "children": [
        {"value": 7, "children": []},
        {"value": 3, "children": [
            {"value": 9, "children": []},
            {"value": 2, "children": []}
        ]}
    ]
}))