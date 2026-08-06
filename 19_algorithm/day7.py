def first_unique(text):
    counts = {}

    for t in text:
        if t in counts:
            counts[t] += 1
        else:
            counts[t] = 1

    result = []

    for t in text:
        if counts[t] == 1:
            result.append(t)

    if result:
        return result[0]
    else:
        return None

print(f"leetcode ->  {first_unique('leetcode')}")
print(f"aabbcc ->  {first_unique('aabbcc')}")
print(f"abcabd ->  {first_unique('abcabd')}")