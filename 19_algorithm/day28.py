def count_evens(input):
    count = 0

    for i in input:
        if isinstance(i, list):
            count += count_evens(i)
        else:
            if i % 2 == 0:
                count += 1
    return count


print(count_evens([1, 2, 3, 4]))
print(count_evens([1, [2, 3], 4]))
print(count_evens([1, [2, [3, 4]], 6]))
print(count_evens([[1, 3], [5, 7]]))
print(count_evens([2, [4, [6, [8]]]]))
