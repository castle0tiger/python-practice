def common_elements(list1, list2):
    result = []

    for c in list1:
        if c in list2:
            result.append(c)

    return result


print(f"[1, 2, 3, 4], [3, 4, 5, 6] -> {common_elements([1, 2, 3, 4], [3, 4, 5, 6])}")
print(f"['a', 'b'], ['b', 'c'] -> {common_elements(['a', 'b'], ['b', 'c'])}")
print(f"[1, 2], [3, 4] -> {common_elements([1, 2], [3, 4])}")