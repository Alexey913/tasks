n, k, d = map(int, input().split())
count = d
while count > 0:
    if n % k == 0:
        n = str(n) + d * '0'
        break
    for i in range(10):
        if (n * 10 + i) % k == 0:
            n = n * 10 + i
            count -= 1
            break
    d -= 1
    if d != count:
        n = -1
        break
print(n)