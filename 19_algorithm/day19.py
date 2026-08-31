def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)

print(sum_to_n(5))
print(sum_to_n(3))
print(sum_to_n(1))

# 단, 여기서 n은 자연수라 가정한다.
# sum_to_n:  base case가 n == 1
# → sum_to_n(0)이나 sum_to_n(-1)을 넣으면? 
# 1을 만날 때까지 못 멈추고 음수로 무한 추락 💥 (0, -1, -2...)
# → "빈 입력"을 처리 못 함