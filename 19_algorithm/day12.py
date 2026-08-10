def closest_diff(numbers):
    sorted_numbers = sorted(numbers)
    closest_diff = sorted_numbers[1] - sorted_numbers[0]

    for l in range(len(sorted_numbers) - 1):
        if sorted_numbers[l+1] - sorted_numbers[l] < closest_diff:
            closest_diff = sorted_numbers[l+1] - sorted_numbers[l]
    return closest_diff

print(f"[3, 8, 1, 12, 5] -> {closest_diff([3, 8, 1, 12, 5])}")     
print(f"[10, 40, 20] -> {closest_diff([10, 40, 20])}")
print(f"[1, 100] -> {closest_diff([1, 100])}")
