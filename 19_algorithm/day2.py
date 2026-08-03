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


print("count_vowels_v1(text) 테스트")
print(f"hello의 모음: {count_vowels_v1("hello")}")
print(f"programming의 모음: {count_vowels_v1("programming")}")
print(f"xyz의 모음: {count_vowels_v1("xyz")}")

print("\n")

print("count_vowels_v2(text) 테스트")
print(f"hello의 모음: {count_vowels_v2("hello")}")
print(f"programming의 모음: {count_vowels_v2("programming")}")
print(f"xyz의 모음: {count_vowels_v2("xyz")}")