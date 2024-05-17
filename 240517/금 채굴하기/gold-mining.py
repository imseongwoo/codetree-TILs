n, m = list(map(int, input().split()))

gold = [
    list(map(int, input().split()))
    for _ in range(n)
]

bestHigh = 0


def howManyGold(x, y, k):
    totalGold = 0
    for i in range(n):
        for j in range(n):
            if abs(x - i) + abs(y - j) <= k:
                totalGold += gold[i][j]
    return totalGold


def digPrice(k):
    return k * k + (k + 1) * (k + 1)


for i in range(n):
    for j in range(n):
        for k in range(n):
            if (howManyGold(i, j, k) * m) >= digPrice(k) and bestHigh < howManyGold(i, j, k):
                bestHigh = howManyGold(i, j, k)

print(bestHigh)