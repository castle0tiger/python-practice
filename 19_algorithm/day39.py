##피보나치 수열 실행 및 테스트
call_count = 0 # 함수 실행 회수 확인 변수

def fib(n):
    global call_count   # ← "나는 바깥의 call_count를 쓸 거야"라고 알려줌
    call_count += 1     # ← 이제 바깥 변수가 진짜로 늘어남

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fib(n-1) + fib(n-2)


print(fib(0))   # → 0
print(fib(1))   # → 1
print(fib(5))   # → 5    (0,1,1,2,3,5)
print(fib(10))  # → 55
print("")

call_count = 0
print(fib(10))
print(call_count)    # fib(10) 혼자만의 호출 수 (177이 나와야 함)

call_count = 0
print(fib(20))
print(call_count)    # fib(20) 혼자만의 호출 수 (21891이 나와야 함)