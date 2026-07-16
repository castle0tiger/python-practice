class VendingMachine:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.sold_count = 0

    def buy(self, x):
        if self.price <= x:
            self.sold_count += 1
            print(f"음료 나옴! 거스름돈 {x - self.price}")

        else:
            print(f"돈이 부족합니다.")
    
    def report(self):
        print(f"판매대수: {self.sold_count}") 


d1 = VendingMachine("콜라", 1500)
d1.buy(1600)
d1.buy(1000)
d1.report()

d2 = VendingMachine("사이다", 1200)
d2.buy(1500)
d2.buy(1000)
d2.report()  