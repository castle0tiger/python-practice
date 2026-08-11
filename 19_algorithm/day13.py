def has_pair_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            if numbers[i] + numbers[j] == target:
                return True
    return False

print(f"([2, 7, 11, 15], 9) -> {has_pair_sum([2, 7, 11, 15], 9)}")
print(f"([1, 2, 3, 4], 8) -> {has_pair_sum([1, 2, 3, 4], 8)}")
print(f"([5, 5], 10) -> {has_pair_sum([5, 5], 10)}")