## max(a, b)를 사용
def max_recursive(numbers):
    if len(numbers) == 1:
        return numbers[0]
    return max(numbers[0], max_recursive(numbers[1:]))

print(max_recursive([3, 7, 1, 9, 4]))
print(max_recursive([5, 2]))
print(max_recursive([42]))


## if문으로 비교 
def max_recursive_v2(numbers):
    if len(numbers) == 1:
        return numbers[0]
    rest_max = max_recursive_v2(numbers[1:])

    if numbers[0] >= rest_max:
        return numbers[0]
    else:
        return rest_max

print("")
print(max_recursive([3, 7, 1, 9, 4]))
print(max_recursive([5, 2]))
print(max_recursive([42]))

