class ExpenseBook:
    def __init__ (self):
        self.expenselist = []

    def add(self, item, amount):
        self.expenselist.append({"항목": item, "금액": amount})

    def total(self):
        total_amount = 0

        for expense in self.expenselist:
            total_amount += expense["금액"]

        return total_amount

    def biggest(self):
        biggest_expense = self.expenselist[0]

        for expense in self.expenselist:
            if biggest_expense["금액"] < expense["금액"]:
                biggest_expense = expense
        return biggest_expense["항목"]
        
    def over(self, limit):
        limit_over = []

        for expense in self.expenselist:
            if expense["금액"] >= limit:
                limit_over.append(expense["항목"])
        return limit_over
    

day_expense = ExpenseBook()
day_expense.add("커피", 4500)
day_expense.add("식비", 12000)
day_expense.add("교통", 3000)

print(day_expense.total())
print(day_expense.biggest())
print(day_expense.over(4000))