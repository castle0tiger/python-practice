def nested_sum(input):
    total = 0

    for i in input:
        if isinstance(i, list) == True:
            total += nested_sum(i)
        else:
            total += i

    return total

print(nested_sum([1, 2, 3]))
print(nested_sum([1, [2, 3], 4]))
print(nested_sum([1, [2, [3, 4]], 5]))
print(nested_sum([[1, 2], [3, [4, 5]]]))