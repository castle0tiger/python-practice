## 방법 A global로 memo = {} 전역함수로 만들기
memo = {}
call_count = 0

def fib_memo(n):
    global memo
    global call_count
    call_count += 1

    if n in memo:
        return memo[n]

    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
    
    return memo[n]

call_count = 0
print(fib_memo(10))
print(call_count)

call_count = 0
print(fib_memo(20))
print(call_count)

call_count = 0
print(fib_memo(35))
print(call_count)
print()

## 방법 B 인풋에다가 memo = {}를 넣는다.
def fib_memo_v2(n, memo = {}):
    global call_count
    call_count += 1

    if n in memo:
        return memo[n]

    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fib_memo_v2(n-1, memo) + fib_memo_v2(n-2, memo)
    
    return memo[n]

call_count = 0
print(fib_memo_v2(10, memo = {}))
print(call_count)

call_count = 0
print(fib_memo_v2(20, memo = {}))
print(call_count)

call_count = 0
print(fib_memo_v2(35, memo = {}))
print(call_count)
print()






# 경우 1 (memo={})   : 📦 📦 📦 📦 📦   ← 매번 새 상자, 아무도 공유 안 함
# 경우 2 (memo)       : 📦 ─┬─ 📦 ─┬─ 📦  ← 한 호출 트리 안에서만 같은 상자 공유
#                           └────── 📦
# 경우 3 (생략)       : 📦📦📦📦📦📦📦📦   ← 전부 다 똑같은 "그 하나의 숨겨진 상자"
#                      (모든 📦가 사실 같은 상자!)

## 경우 2의 추가 설명
# fib_memo_v2(10, memo={})  →  📦[상자P] 생성
#     └─ 재귀(9,8,7...)는 전부 상자P를 그대로 전달받아 공유 (경우 2)
#     └─ 상자P 안에 0~10 값이 다 채워짐

# fib_memo_v2(20, memo={})  →  📦[상자Q] 생성 (상자P와 완전 무관, 새 출발)
#     └─ 재귀(19,18...)는 전부 상자Q를 공유 (경우 2)
#     └─ 상자Q는 텅 빈 상태에서 0~20을 전부 새로 채워야 함 ← 상자P의 혜택 못 받음!

