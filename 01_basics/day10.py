# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def check_pass(self):
#         if self.score >= 60:
#             return "합격"
#         else:
#             return "불합격"

#     def get_grade(self):
#         if self.score >= 90:
#             return "A"
#         elif self.score >= 80:
#             return "B"
#         elif self.score >= 70:
#             return "c"
#         else:
#             return "F"

# students = [
#     Student("홍길동", 85),
#     Student("김철수", 45),
#     Student("이영희", 92)
# ]

# for student in students:
#     print(f"{student.name} : {student.score}점 : {student.get_grade()}등급 : {student.check_pass()}")



## 미니 실습 과제

# class Car:
#      def __init__(self, brand):
#          self.brand = brand
#          self.speed = 0

#      def accelerate(self, amount):
#         self.speed = self.speed + amount

#      def brake(self, amount):
#         if self.speed > amount:
#             self.speed = self.speed - amount
#         else:
#             self.speed = 0

#      def status(self):
#          print(f"현재 브랜드: {self.brand}, 속도: {self.speed}km/h" )

# car = Car("현대")
# car.accelerate(50)
# car.accelerate(30)
# car.brake(20)
# car.status()


## 미니 실습 과제 2

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
        else:
            print("잔액 부족")
    
    def status(self):
        print(f"예금주: {self.owner}, 잔액: {self.balance}원")

account = BankAccount("홍길동")
account.deposit(100000)
account.withdraw(30000)
account.withdraw(80000)
account.status()
