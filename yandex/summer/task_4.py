n, k = map(int, input().split())
price = list(map(int, input().split()))
fish = [0] * len(price)
fish[0] = 1
min_cost = price[0]
min_index = 0
sum_price = 0
total_count = 0
for i in range(n):
    min_cost = price[i]
    min_index = i
    if total_count <= i:
        print(i+1)
        for j in range(i, min(i + k, n)):
            if price[j] < min_cost:
                min_cost = price[j]
                min_index = j
                fish[j] += 1
            else:
                fish[min_index] += 1
            total_count += 1
    sum_price += price[i] * fish[i]
print(sum_price)
print(*fish)