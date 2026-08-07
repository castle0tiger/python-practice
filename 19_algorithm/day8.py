## 리스트에 중복이 되지 않는다고 가정.
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
print("숫자리스트에서 2번째로 큰 수 찾기 - 방법B")
print(f"[3, 7, 1, 9, 4] -> {second_largest_v2([3, 7, 1, 9, 4])}")
print(f"[10, 5, 8] -> {second_largest_v2([10, 5, 8])}")         
print(f"[1, 2] -> {second_largest_v2([1, 2])}")


# 피드백_ 만약 리스트 안에 요소로 중복이 될때 방법B 오류 개선
def second_largest_v3(numbers):
    result = list(set(numbers))     # 집합으로 중복 제거하고 다시 리스트화
    sorted_numbers = sorted(result)

    return sorted_numbers[-2]

print("\n")
print("숫자리스트에서 2번째로 큰 수 찾기 - 중복허용 방법B 개선")
print(f"[3, 7, 1, 9, 4, 9, 7] -> {second_largest_v3([3, 7, 1, 9, 4, 9, 7])}")
print(f"[10, 5, 8, 8, 5] -> {second_largest_v3([10, 5, 8, 8, 5])}")         