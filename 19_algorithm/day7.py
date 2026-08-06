def first_unique_v1(text):
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

    if result:               #리스트에 요소 존재 유무 조사
        return result[0]
    else:
        return None

print(f"leetcode ->  {first_unique_v1('leetcode')}")
print(f"aabbcc ->  {first_unique_v1('aabbcc')}")
print(f"abcabd ->  {first_unique_v1('abcabd')}")
print()


## 실무 피드백 _ 코드 효율화 

def first_unique_v2(text):
    counts = {}

    for t in text:
        if t in counts:
            counts[t] += 1
        else:
            counts[t] = 1

    for t in text:
        if counts[t] == 1:
            return t
    return None


print(f"leetcode ->  {first_unique_v2('leetcode')}")
print(f"aabbcc ->  {first_unique_v2('aabbcc')}")
print(f"abcabd ->  {first_unique_v2('abcabd')}")