drinks = [
    {"메뉴": "아메리카노", "가격": 3000, "판매량": 120},
    {"메뉴": "카페라떼", "가격": 4500, "판매량": 80},
    {"메뉴": "녹차", "가격": 4000, "판매량": 35},
    {"메뉴": "딸기스무디", "가격": 5500, "판매량": 25}
]

total_sales = 0

for d in drinks:
    total_sales += (d["가격"] * d["판매량"])
print(f"총매출: {total_sales}원")

cheapest_price = drinks[0]["가격"]
cheapest_menu = drinks[0]["메뉴"] 

for d in drinks:
    if d["가격"] < cheapest_price:
        cheapest_price = d["가격"]
        cheapest_menu = d["메뉴"]
print(f"최저가: {cheapest_menu} ({cheapest_price}원)")

for d in drinks:
    if d["가격"] <= 4500 and d["판매량"] >= 30:
        print(f"가성비 메뉴: {d['메뉴']}")