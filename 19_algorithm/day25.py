def flatten(input):
    result = []

    for i in input:
        if isinstance(i, list) == True:
            result.extend(flatten(i))
        else:
            result.append(i)

    return result


print(flatten([1, 2, 3]))
print(flatten([1, [2, 3], 4]))
print(flatten([1, [2, [3, 4]], 5]))
print(flatten([[1, 2], [3, [4, 5]]]))
