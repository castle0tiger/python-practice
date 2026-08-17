def recursive_sum(numbers):
    if not numbers:
        return 0
    
    return numbers[0] + recursive_sum(numbers[1:])

print(recursive_sum([1, 2, 3, 4]))
print(recursive_sum([5, 10]))
print(recursive_sum([7]))
print(recursive_sum([]))