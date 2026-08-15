def sort_by_frequency(inputs):
    counts = {}

    for i in inputs:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    sorted_counts = sorted(counts, key=lambda x: counts[x], reverse=True)
    return sorted_counts


print(f"[1, 2, 2, 3, 3, 3] -> {sort_by_frequency([1, 2, 2, 3, 3, 3])}")
print(f"['a', 'b', 'b', 'c', 'c', 'c'] -> {sort_by_frequency(['a', 'b', 'b', 'c', 'c', 'c'])}")
print(f"[5, 5, 7] -> {sort_by_frequency([5, 5, 7])}")