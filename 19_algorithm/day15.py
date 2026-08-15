def max_items(weights, target):
    sorted_weights = sorted(weights)
    total = 0
    count = 0

    for w in sorted_weights:
       if w < target and total + w <= target:
           total += w
           count += 1
       elif w < target and total + w > target:
           return count
       else:
          return count


print(f"[2, 5, 1, 8, 3], 10 -> {max_items([2, 5, 1, 8, 3], 10)}")
print(f"[4, 4, 4], 10 -> {max_items([4, 4, 4], 10)}")
print(f"[100], 10 -> {max_items([100], 10)}")