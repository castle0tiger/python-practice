## 함수 정의 def 사용


# def greet(name):
#     print(name+"님, 안녕하세요!")

# greet("캐슬타이거")
# greet("홍길동")


## 함수 정의 def 사용 _ 2

# def add(a, b):
#     return a + b

# result = add(100, 200)
# print(result)


## 함수 + 조건문 조합

# def check_pass(score):
#    if score >= 60:
#        return "합격"
#    else:
#        return "불합격"
    
# print(check_pass(85))
# print(check_pass(40))


## 실전 미니 과제

# def bmi(weight, height):
#     return weight / (height * height)

# print(round(bmi(71, 1.67), 1))


## 실전 미니 과제 2 

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
for i in range(1, 11):
    if is_even(i):
        print(i, "짝수")
    else :
        print(i, "홀수")