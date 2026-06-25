# number = int("abc")
# print(number)

# try:
#     number = int("abc")
#    print(number)
# except ValueError:
#     print("숫자로 변환할 수 없습니다.")

# print("프로그램 계속 실행됩니다.")

# try:
#     number = int(input("숫자를 입력하세요: "))
#     result = 10 / number
#     print(f"결과 : {result}")
# except ValueError:
#     print("숫자만 입력하세요.")
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# finally:
#     print("입력 완료. ")

 
## 미니과제

data = ["10", "20", "abc", "30", "xyz", "40"]
total = 0

for item in data:
    try:
        number = int(item)
        total += int(item)
    except ValueError:
        print(f"{item} 변환 실패, 건너뜁니다.")

print(f"합계: {total}")