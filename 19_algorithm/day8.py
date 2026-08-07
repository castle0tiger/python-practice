# 방법 A
def second_largest(numbers):
    first = numbers[0]
    second = numbers[1]

    if first < second:
        first = numbers[1]
        second = numbers[0]

    for n in numbers:
        if n > first:
            second = first
            first = n

        elif n < first and n > second:
            second = n

    return second

print("숫자리스트에서 2번째로 큰 수 찾기 - 방법A")
print(f"[3, 7, 1, 9, 4] -> {second_largest([3, 7, 1, 9, 4])}")
print(f"[10, 5, 8] -> {second_largest([10, 5, 8])}")         
print(f"[1, 2] -> {second_largest([1, 2])}")             


# 방법 B
def second_largest_v2(numbers):
    sorted_numbers = sorted(numbers)

    return sorted_numbers[-2]

print("\n")
print(f"[3, 7, 1, 9, 4] -> {second_largest_v2([3, 7, 1, 9, 4])}")
print(f"[10, 5, 8] -> {second_largest_v2([10, 5, 8])}")         
print(f"[1, 2] -> {second_largest_v2([1, 2])}")    