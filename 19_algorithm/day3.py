def max_min_diff(numbers):
    max_result = numbers[0]
    min_result = numbers[0]

    for n in numbers:
        if max_result < n:
            max_result = n

    for n in numbers:
        if min_result > n:
            min_result = n

    return max_result - min_result


def max_min_diff_v2(numbers):
    return max(numbers) - min(numbers)


print("비교갱신법을 사용한 함수")
print(f"[3, 7, 1, 9, 4] -> {max_min_diff([3, 7, 1, 9, 4])}")
print(f"[10, 10, 10] -> {max_min_diff([10, 10, 10])}")

print("\n")

print("max(), min() 내장 함수를 사용한 함수")
print(f"[3, 7, 1, 9, 4] -> {max_min_diff_v2([3, 7, 1, 9, 4])}")
print(f"[10, 10, 10] -> {max_min_diff_v2([10, 10, 10])}")