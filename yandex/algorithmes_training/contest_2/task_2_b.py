n, k = map(int, input().split())
price = list(map(int, input().split()))
max_cash = 0
for i in range(n):
    for j in range(i+1, min(i + k + 1, n)):
        if price[j] - price[i] > max_cash:
            max_cash = price[j] - price[i]
print(max_cash)