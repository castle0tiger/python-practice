def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)

print(sum_to_n(5))
print(sum_to_n(3))
print(sum_to_n(1))