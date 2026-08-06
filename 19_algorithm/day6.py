def find_duplicates(numbers):
    counts = {}

    for n in numbers:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1

    result = []

    for key in counts:
        if counts[key] >= 2:
            result.append(key)

    return result


print(f"[1, 2, 2, 3, 3, 3, 4]-> {find_duplicates([1, 2, 2, 3, 3, 3, 4])}")
print(f"['a', 'b', 'a', 'c']-> {find_duplicates(['a','b', 'a', 'c'])}")
print(f"[1, 2, 3]-> {find_duplicates([1, 2, 3])}")