def count_vowels_v1(text):
    result = 0
    for t in text:
        if t == 'a' or t == 'e' or t =='i' or t == 'o' or t == 'u':
            result += 1
    return result


def count_vowels_v2(text):
    result = 0
    for t in text:
        if t in 'aeiou':
            result += 1
    return result


v1_t1 = count_vowels_v1("hello")
v1_t2 = count_vowels_v1("programming")
v1_t3 = count_vowels_v1("xyz")

v2_t1 = count_vowels_v2("hello")
v2_t2 = count_vowels_v2("programming")
v2_t3 = count_vowels_v2("xyz")

print(v1_t1)
print(v1_t2)
print(v1_t3)

print("\n")

print(v2_t1)
print(v2_t2)
print(v2_t3)