def tree_search(tree, target):

    if tree["value"] == target:
        return True

    else:
        if tree["children"]:
            for node in tree["children"]:
               if tree_search(node, target) == True:
                   return True

    return False


print("테스트")
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