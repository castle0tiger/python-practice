## 하반기 신입공고 작성하느라 27일만에 다시 학습 시작하여 쉬운 문제부터 복습

def tree_all_values(tree):
    result = []
    result.append(tree["value"])

    if tree["children"]:
       for node in tree["children"]:
           result.extend(tree_all_values(node))

    return result


print(tree_all_values({"value": 5, "children": []}))

print(tree_all_values({
    "value": 1,
    "children": [
        {"value": 7, "children": []},
        {"value": 3, "children": [
            {"value": 9, "children": []},
            {"value": 2, "children": []}
        ]}
    ]
}))
