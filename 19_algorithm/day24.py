def nested_sum(input):
    total = 0

    for i in input:
        if isinstance(i, list) == True:
            total += nested_sum(i)
        else:
            total += i

    return total

print(nested_sum([1, 2, 3]))
print(nested_sum([1, [2, 3], 4]))
print(nested_sum([1, [2, [3, 4]], 5]))
print(nested_sum([[1, 2], [3, [4, 5]]]))


### isinstance(x, 타입) — "x가 이 타입이야?"
#```python
# isinstance(5, list)      # False  (숫자)
# isinstance([1,2], list)  # True   (리스트)
# isinstance("a", str)     # True   (문자열)
# ```
# - "is instance of"의 줄임. 중첩 구조에서 "숫자냐 리스트냐" 구분해 처리할 때(DFS) 핵심.
# - `== True` 안 붙여도 됨: `if isinstance(x, list):` 로 바로.


### 왜 6번째 줄은 total += nested_sum(i) 인가?
## nested_sum([1, [2,3], 4])   ← 회의실 A, total_A = 0
#    │ 1 → total_A += 1              (total_A = 1)
#    │ [2,3] → nested_sum([2,3]) 호출
#    │            │
#    │            └─ 회의실 B, total_B = 0    ← A랑 별개!
#    │                 2 → total_B += 2       (total_B = 2)
#    │                 3 → total_B += 3       (total_B = 5)
#    │                 return 5   ──────┐
#    │ total_A += 5  ←──────────────────┘  (A가 B의 결과 5를 받음)  (total_A = 6)
#    │ 4 → total_A += 4              (total_A = 10)
#    └ return 10


## 만약 6번째 줄이 nested_sum(i)이 였다면?
# 회의실 A, total_A = 0
#   원소를 하나씩:
#   │
#   ├ 1        → 숫자 → total_A += 1        (total_A = 1)
#   │
#   ├ [2,[3,4]] → 리스트 → nested_sum([2,[3,4]]) 호출
#   │              │
#   │              └ 회의실 B, total_B = 0   (여기서 2도 더하고 파고들지만...)
#   │                 return 어떤 값        ← ★ A가 이걸 안 받음! 버려짐 💥
#   │              (total_A는 그대로 1)
#   │
#   └ 5        → 숫자 → total_A += 5        (total_A = 6)
#   return 6


## def안에 있는 total은 지역변수(전역변수 아님) 그렇기 때문에, 값을 받아주지 않으면 새로 호출되면 값이 날라간다.