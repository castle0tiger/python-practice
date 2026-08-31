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
print("")


## 피드백 _ 효율성 제고
def has_pair_sum_v2(numbers, target):
    for i in range(len(numbers)):
        for j in range(1+i, len(numbers)): # i 다음부터 → 중복·자기자신 방지
            if numbers[i] + numbers[j] == target:
                return True

    return False

print(f"([2, 7, 11, 15], 9) -> {has_pair_sum_v2([2, 7, 11, 15], 9)}")
print(f"([1, 2, 3, 4], 8) -> {has_pair_sum_v2([1, 2, 3, 4], 8)}")
print(f"([5, 5], 10) -> {has_pair_sum_v2([5, 5], 10)}")


## range() 정리
# range(끝)           →  0부터 끝 직전까지        range(5)     → 0,1,2,3,4
# range(시작, 끝)      →  시작부터 끝 직전까지     range(1, 5)  → 1,2,3,4
# range(시작, 끝, 간격) →  간격만큼 건너뛰며       range(0,10,2)→ 0,2,4,6,8

## 리스트[시작:끝:간격] 슬라이싱 정리
# nums = [10, 20, 30, 40, 50]
#         0   1   2   3   4     ← 인덱스

# nums[1:4]     →  [20, 30, 40]     # 1번~3번 (끝 4 제외)
# nums[:3]      →  [10, 20, 30]     # 처음~2번 (시작 생략=0부터)
# nums[2:]      →  [30, 40, 50]     # 2번~끝 (끝 생략=끝까지)
# nums[:]       →  [10,20,30,40,50] # 전체 (통째 복사)