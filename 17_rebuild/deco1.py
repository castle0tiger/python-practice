def register(func):
    print(func.__name__, "← 이 함수가 나한테 배달됐다!")
    return func

@register
def hello():
    print("안녕!")

@register
def bye():
    print("잘가!")

print("--- 여기까지가 파일 읽기 ---")
hello()
