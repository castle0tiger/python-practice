## day2 : 조건문 (if/else)

# Step 2: if/else 기본
# score = 40
# if score >= 60 :
#     print("합격입니다!")
# else :
#     print( "불합격입니다.")


## day2 : 조건문 elif

# score = 50
# if score >= 90:
#     print("A등급")
# elif score >= 80:
#     print("B등급")
# elif score >= 70:
#     print("C등급")
# else:
#     print("D등급")

## day2 : 조건문 and/or

# score = 50          
# attendance = 70

# if score >= 60 and attendance >= 75:
#     print("합격입니다!")
# else:
#     print("불합격입니다.")


## day2 : 실전 미니 과제 _ 1

# score = 50
# is_member = True
 
# if score >= 70 and is_member :
#     print("특별 합격")
# elif score >= 70 and not is_member : 
#     print("일반 합격")
# else:
#     print("불합격")


## day2 : 실전 미니 과제 _ 2

username = str("admin")
password = int(1234)

if username == "admin" and password == 1234:
    print("로그인 성공")
elif username == "admin" and not password == 1234:
    print("비밀번호 오류")
else : 
    print("존재하지 않는 계정")