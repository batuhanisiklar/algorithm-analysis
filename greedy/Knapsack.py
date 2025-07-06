def max_size(weight, amount):
    amount.sort(reverse=True)
    weight.sort(reverse=True)
    totalWeight = 0
    totalCost = 0

    for i in range(len(amount)):
        while totalWeight <= 1000:
            totalWeight += weight[i]
            totalCost += amount[i]
            weight.pop(i)
            amount.pop(i)
    return totalCost

# Örnek kullanım
weight = [200, 500, 700, 400, 100]
amount = [100, 300, 700, 500, 10]
print("Toplam Fiyat:", max_size(weight, amount))