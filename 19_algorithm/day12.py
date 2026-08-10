## 방법 A : 인접한 숫자 서로 비교하기

def closest_diff(numbers):
    sorted_numbers = sorted(numbers)
    closest_diff = sorted_numbers[1] - sorted_numbers[0]

    for l in range(len(sorted_numbers) - 1):
        if sorted_numbers[l+1] - sorted_numbers[l] < closest_diff:
            closest_diff = sorted_numbers[l+1] - sorted_numbers[l]
    return closest_diff

print("방법A")
print(f"[3, 8, 1, 12, 5] -> {closest_diff([3, 8, 1, 12, 5])}")     
print(f"[10, 40, 20] -> {closest_diff([10, 40, 20])}")
print(f"[1, 100] -> {closest_diff([1, 100])}")
print("\n")

## 방법 B : 모든 순서쌍을 비교하여 찾기 _ 중복 반복

def closest_diff_v2(numbers):
    closest = abs(numbers[0] - numbers[1]) #초기값 = 첫 쌍의 차이

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            elif abs(numbers[i] - numbers[j]) < closest:
                closest = abs(numbers[i] - numbers[j])

    return closest

print("방법B")
print(f"[3, 8, 1, 12, 5] -> {closest_diff_v2([3, 8, 1, 12, 5])}")     
print(f"[10, 40, 20] -> {closest_diff_v2([10, 40, 20])}")
print(f"[1, 100] -> {closest_diff_v2([1, 100])}")