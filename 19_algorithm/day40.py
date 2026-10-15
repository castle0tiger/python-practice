memo = {}
call_count = 0

def fib_memo(n):
    global memo
    global call_count
    call_count += 1

    if n in memo:
        return memo[n]

    else:
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