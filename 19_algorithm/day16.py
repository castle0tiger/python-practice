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


## 문법 학습
# 1. 딕셔너리 {key:vallue, ...}에서
# counts = {a: 1, b: 2, c: 3} 일때, 

# counts.keys()     →  a, b, c         (키들 = 원소)
# counts.values()   →  1, 2, 3         (값들 = 개수)   ← 이번엔 우연히 같아보이지만 다른 것
# counts.items()    →  (a,1),(b,2),(b,3)  (키-값 쌍들)


# 2. sorted(정렬할_대상, key=기준, reverse=방향)
# 첫 번째(정렬 대상): 이름표 없이 그냥 기재. sorted는 "괄호 열고 맨 처음 온 건 정렬 대상"이라고 약속. → 위치로 알아봄
# key=, reverse=: 반드시 이름표(key=, reverse=)를 기재. 안 붙이면 sorted가 "이게 기준인지 방향인지" 알 수 없음. → 이름으로 알아봄

# sorted([3,1,2])                    # [1,2,3]      기준·방향 다 생략 → 값 크기, 오름차순
# sorted([3,1,2], reverse=True)      # [3,2,1]      방향만 지정
# sorted(students, key=lambda x:x["score"])              # 기준만 (오름차순)
# sorted(students, key=lambda x:x["score"], reverse=True) # 둘 다

### Python 문법 전반적으로 다 이러한 문법으로 사용됨
# -> 함수(필수재료, 옵션이름=값, 옵션이름=값)
#   - 첫 자리(들): 이름표 없이, 위치로 (필수)
#   - 옵션: 이름표(=) 붙여서 (생략 가능, 순서 자유)