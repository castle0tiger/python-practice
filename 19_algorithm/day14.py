#금액은 주어진 동전들로 항상 만들 수 있다고 가정
def min_coins(coins, target):
    sorted_coins = sorted(coins, reverse=True)
    count = 0
    portion = 0

    for coin in sorted_coins:
        if target % coin == 0:
            portion = target // coin
            count += portion
            return count
        else:
            portion = target // coin
            count += portion
            target = target - (coin * portion)

    return count

print(f"[500, 100, 50, 10], 1260 -> {min_coins([500, 100, 50, 10], 1260)}")
print(f"[500, 100, 50, 10], 3000 -> {min_coins([500, 100, 50, 10], 3000)}")
print(f"[500, 100, 50, 10], 890 -> {min_coins([500, 100, 50, 10], 890)}")