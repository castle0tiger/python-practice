def nested_contains(numbers, target):
    for n in numbers:
        if isinstance(n, list):
            if nested_contains(n, target) == True:
                return True
        else:  
            if n == target:
                return True
    return False


print(nested_contains([1, 2, 3], 2))
print(nested_contains([1, [2, 3], 4], 3))
print(nested_contains([1, [2, [3, 4]], 5], 4))
print(nested_contains([1, [2, 3]], 9))
print(nested_contains([[1], [2, [3]]], 3))