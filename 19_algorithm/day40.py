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