## 재귀로 글자 뒤집기
def reverse_recursive(text):
    if text == "":
        return ""
    return reverse_recursive(text[1:]) + text[0]

print("재귀로 글자 뒤집기")        
print(reverse_recursive("hello"))
print(reverse_recursive("abc"))
print(reverse_recursive(""))


## 반복문 for문으로 글자 뒤집기
def reverse_text_for(text):
    reverse_text = ""

    for t in text:
        reverse_text = t + reverse_text

    return reverse_text

print("반복문 for문으로 글자 뒤집기")     
print(reverse_text_for("hello"))
print(reverse_text_for("abc"))
print(reverse_text_for(""))


## slicing으로 글자 뒤집기
def reverse_text_slicing(text):
    return text[::-1]

print("slicing으로 글자 뒤집기")     
print(reverse_text_slicing("hello"))
print(reverse_text_slicing("abc"))
print(reverse_text_slicing(""))