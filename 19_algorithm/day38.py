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