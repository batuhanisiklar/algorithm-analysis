def min_coins(coins, amount):
    coins.sort(reverse=True)  # Büyükten küçüğe sırala
    result = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)

    return result


# Örnek kullanım
coins = [20, 19, 5, 1]
amount = 24
print("Kullanılan paralar:", min_coins(coins, amount))
