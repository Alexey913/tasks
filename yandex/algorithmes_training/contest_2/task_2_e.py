n = int(input())
berries = [list(map(int, input().split())) + [i] for i in range(n)]
for i in range(n):
    for j in range(n):
        if berries[j][0] - berries[j][1] < berries[i][0] - berries[i][1]:
            berries[i], berries[j] = berries[j], berries[i]
sum_dist = 0
for i in berries[:-1]:
    sum_dist += (i[0] - i[1])
sum_dist += berries[-1][0]
print(sum_dist)
