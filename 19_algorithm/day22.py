def is_palindrome(text):
    if len(text) <= 1:
        return True

    elif text[0] != text[-1]:
        return False
    
    else:
       return is_palindrome(text[1:-1])

print(f"racecar -> {is_palindrome('racecar')}")
print(f"level -> {is_palindrome('level')}")
print(f"hello -> {is_palindrome('hello')}")
print(f"a -> {is_palindrome('a')}")
print(f" -> {is_palindrome('')}")