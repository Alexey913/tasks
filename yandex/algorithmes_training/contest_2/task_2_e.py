n = int(input())
berries = [list(map(int, input().split())) + [i] for i in range(n)]
down_step_berries = []
up_step_berries = []
max_high_down_berry = 0
for berry in berries:
    if berry[0] <= berry[1]:
        if berry[0] > max_high_down_berry:
            max_high_down_berry = berry[0]
            down_step_berries.insert(0, berry)
        else:
            down_step_berries.append(berry)
    else:
        if up_step_berries:
            for i in up_step_berries:
                if berry[0] < i[0] or berry[0] == i[0] and berry[1] >= i[1]:
                    up_step_berries.insert(up_step_berries.index(i) + 1, berry)
                    break
        else:
            up_step_berries.append(berry)
# print(up_step_berries)
print(down_step_berries)
sum_dist = 0
max_high = 0
for i in up_step_berries:
    sum_dist += i[0]
    if sum_dist > max_high:
        max_high = sum_dist
    sum_dist -= i[1]
    print(sum_dist, i)
if max_high < sum_dist + down_step_berries[0][0]:
    max_high = sum_dist + down_step_berries[0][0]
print(max_high)
for i in up_step_berries + down_step_berries:
    print(i[2] + 1, end=' ')

# n = int(input())
# berries = [list(map(int, input().split())) + [i] for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if berries[j][0] - berries[j][1] < berries[i][0] - berries[i][1]:
#             berries[i], berries[j] = berries[j], berries[i]
# for i in range(n-1):
#     for j in range(n-1):
#         if berries[j][0] - berries[j][1] + berries[j+1][1] < berries[i][0] - berries[i][1] + berries[i+1][0]:
#             berries[i], berries[j] = berries[j], berries[i]
# sum_dist = 0
# max_high = 0
# for i in berries:
#     sum_dist += i[0]
#     if sum_dist > max_high:
#         max_high = sum_dist
#     sum_dist -= i[1]
# print(max_high)
# for i in berries:
#     print(i[2] + 1, end=' ')


# n = int(input())
# berries = [list(map(int, input().split())) + [i] for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if berries[j][0] - berries[j][1] < berries[i][0] - berries[i][1]:
#             berries[i], berries[j] = berries[j], berries[i]
# print(berries)
# sum_dist = 0
# max_high = 0
# for i in berries:
#     sum_dist += i[0]
#     if sum_dist > max_high:
#         max_high = sum_dist
#     sum_dist -= i[1]
# for i in range(n):
#     for j in range(n - 1):
#         if berries[j][0] - berries[j][1] < berries[i][0] - berries[i][1]:
#             berries[i], berries[j] = berries[j], berries[i]
# print(max_high)
# for i in berries:
#     print(i[2] + 1, end=' ')


# n = int(input())
# berries = [list(map(int, input().split())) + [i] for i in range(n)]
# for i in range(n-1):
#     for j in range(n-1):
#         if berries[j][0] - berries[j][1] + berries[j+1][1] < berries[i][0] - berries[i][1] + berries[i+1][0]:
#             berries[i], berries[j] = berries[j], berries[i]
            
# sum_dist = 0
# max_high = 0
# for i in berries:
#     sum_dist += i[0]
#     if sum_dist > max_high:
#         max_high = sum_dist
#     sum_dist -= i[1]
# print(max_high)
# for i in berries:
#     print(i[2] + 1, end=' ')