from datetime import datetime

# n = int(input())
# down_step_berries = {}
# up_step_berries = {}
# max_high_down_berry = 0
# max_down_up_berry = 0
# s = datetime.now()
# for i in range(1, n+1):
#     berry_up, berry_down = map(int, input().split())
#     if berry_up <= berry_down:
#         if berry_up > max_high_down_berry:
#             max_high_down_berry = berry_up
#             down_step_berries = {i: (berry_up, berry_down)} | down_step_berries 
#         else:
#             down_step_berries[i] = (berry_up, berry_down)
#     else:
#         if berry_down > max_down_up_berry:
#             max_down_up_berry = berry_down
#             up_step_berries[i] = (berry_up, berry_down)
#         else:
#             up_step_berries = {i: (berry_up, berry_down)} | up_step_berries
# print(datetime.now() - s)
# sum_dist = 0
# max_high = 0
# if up_step_berries:
#     for v in up_step_berries.values():
#         sum_dist += v[0]
#         if sum_dist > max_high:
#             max_high = sum_dist
#         sum_dist -= v[1]
# if down_step_berries:
#     first_down = down_step_berries[list(down_step_berries.keys())[0]][0]
#     if down_step_berries and max_high < sum_dist + first_down:
#         max_high = sum_dist + first_down
# print(max_high)
# for i in up_step_berries | down_step_berries:
#     print(i, end=' ')



start = datetime.now()
n = int(input())
berries = [list(map(int, input().split())) + [i] for i in range(n)]
down_step_berries = []
up_step_berries = []
max_high_down_berry = 0
max_down_up_berry = 0
start_input = datetime.now()
for berry in berries:
    if berry[0] <= berry[1]:
        if berry[0] > max_high_down_berry:
            max_high_down_berry = berry[0]
            down_step_berries.insert(0, berry)
        else:
            down_step_berries.append(berry)
    else:
        if berry[1] > max_down_up_berry:
            max_down_up_berry = berry[1]
            up_step_berries.append(berry)
        else:
            up_step_berries.insert(0, berry)

# print(up_step_berries)
# print(down_step_berries)
sum_dist = 0
max_high = 0
strat_del = datetime.now()
for i in up_step_berries:
    sum_dist += i[0]
    if sum_dist > max_high:
        max_high = sum_dist
    sum_dist -= i[1]
    # print(sum_dist, i)
if down_step_berries and max_high < sum_dist + down_step_berries[0][0]:
    max_high = sum_dist + down_step_berries[0][0]
print(max_high)
start_output = datetime.now()
for i in up_step_berries + down_step_berries:
    print(i[2] + 1, end=' ')
finish = datetime.now()
print(f'{start_input-start=}')
print(f'{strat_del-start_input=}')
print(f'{start_output-strat_del=}')
print(f'{finish-start_output}')