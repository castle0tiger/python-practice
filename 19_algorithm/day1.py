#1 — 문자열 뒤집기

def reverse_text(text):
    result = ''
    for c in text:
        result = c + result

    return result

t1 = reverse_text("hello")
t2 = reverse_text("파이썬")

print(t1)
print(t2)

#1 - 피드백
#실무에서는 [::-1]으로 간략하게 사용할 수 있다. 


def reverse_text_2(text):
    return text[::-1]

t3 = reverse_text_2("hello")
t4 = reverse_text_2("파이썬")

print("\n")
print(t3)
print(t4)
