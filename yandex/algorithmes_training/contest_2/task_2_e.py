# from datetime import datetime as d
# from datetime import timedelta as t

# n = int(input())
# down_step_berries = {}
# up_step_berries = {}
# max_high_down_berry = 0
# max_down_up_berry = 0
# start_input = d.now()
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
# end_input = d.now()
# sum_dist = 0
# max_high = 0
# start_sort = d.now()
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
# end_sort = d.now()
# print(max_high)
# for i in up_step_berries | down_step_berries:
#     print(i, end=' ')
# finis = d.now()
# print()
# print(end_input - start_input)
# print(end_sort - start_sort)
# print(finis - end_sort)



# with open('input.txt', 'r') as f:
#     n = int(f.readline())
#     berries = [list(map(int, f.readline().split())) + [i] for i in range(n)]
# down_step_berries = []
# up_step_berries = []
# max_high_down_berry = 0
# max_down_up_berry = 0
# for berry in berries:
#     if berry[0] <= berry[1]:
#         if berry[0] > max_high_down_berry:
#             max_high_down_berry = berry[0]
#             down_step_berries.insert(0, berry)
#         else:
#             down_step_berries.append(berry)
#     else:
#         if berry[1] > max_down_up_berry:
#             max_down_up_berry = berry[1]
#             up_step_berries.append(berry)
#         else:
#             up_step_berries.insert(0, berry)

# sum_dist = 0
# max_high = 0
# for i in up_step_berries:
#     sum_dist += i[0]
#     if sum_dist > max_high:
#         max_high = sum_dist
#     sum_dist -= i[1]
# if down_step_berries and max_high < sum_dist + down_step_berries[0][0]:
#     max_high = sum_dist + down_step_berries[0][0]
# print(max_high)
# for i in up_step_berries + down_step_berries:
#     print(i[2] + 1, end=' ')



indexes_high = []
indexes_down = []
last_high_index = 0
max_high_down_berry = 0
max_down_up_berry = 0
max_high_up_berry = 0
sum_dist = 0
max_high = 0
with open('input.txt', 'r') as f:
    n = int(f.readline())
    for i in range(n):
        berry_up, berry_down = map(int, f.readline().split())
        if berry_up < berry_down:
            if berry_up > max_high_down_berry:
                print(f'{max_high_down_berry=}, {berry_up=}')
                max_high_down_berry = berry_up
                indexes_down.insert(0, i + 1)
            else:
                indexes_down.append(i + 1)
        else:
            if berry_down > max_down_up_berry:
                sum_dist += max_high_up_berry
                if sum_dist > max_high:
                    max_high = sum_dist
                sum_dist -= max_down_up_berry
                max_down_up_berry = berry_down
                max_high_up_berry = berry_up
                indexes_high.append(i + 1)
            else:
                sum_dist += berry_up
                if sum_dist > max_high:
                    max_high = sum_dist
                sum_dist -= berry_down
                indexes_high.insert(0, i + 1)

    sum_dist += max_high_up_berry
    if sum_dist > max_high:
        max_high = sum_dist
    sum_dist -= max_high_down_berry
if indexes_down and max_high < sum_dist + max_down_up_berry:
    max_high = sum_dist + max_down_up_berry
print(max_high)
for i in indexes_high + indexes_down:
    print(i, end=' ')



# down_step_berries = []
# up_step_berries = []
# max_high_down_berry = 0
# max_down_up_berry = 0
# with open('input.txt', 'r') as f:
#     n = int(f.readline())
#     for i in range(n):
#         berry = list(map(int, f.readline().split()))
#         if berry[0] <= berry[1]:
#             if berry[0] > max_high_down_berry:
#                 max_high_down_berry = berry[0]
#                 down_step_berries.insert(0, berry)
#             else:
#                 down_step_berries.append(berry)
#         else:
#             if berry[1] > max_down_up_berry:
#                 max_down_up_berry = berry[1]
#                 up_step_berries.append(berry)
#             else:
#                 up_step_berries.insert(0, berry)
# sum_dist = 0
# max_high = 0
# for i in up_step_berries:
#     sum_dist += i[0]
#     if sum_dist > max_high:
#         max_high = sum_dist
#     sum_dist -= i[1]
# if down_step_berries and max_high < sum_dist + down_step_berries[0][0]:
#     max_high = sum_dist + down_step_berries[0][0]
# print(max_high)
# for i in up_step_berries + down_step_berries:
#     print(i[2] + 1, end=' ')



# down_step_berries = {}
# up_step_berries = {}
# max_high_down_berry = 0
# max_down_up_berry = 0
# with open('input.txt', 'r') as f:
#     n = int(f.readline())
#     for i in range(1, n+1):
#         berry_up, berry_down = map(int, f.readline().split())
#         if berry_up <= berry_down:
#             if berry_up > max_high_down_berry:
#                 max_high_down_berry = berry_up
#                 down_step_berries = {i: (berry_up, berry_down)} | down_step_berries 
#             else:
#                 down_step_berries[i] = (berry_up, berry_down)
#         else:
#             if berry_down > max_down_up_berry:
#                 max_down_up_berry = berry_down
#                 up_step_berries[i] = (berry_up, berry_down)
#             else:
#                 up_step_berries = {i: (berry_up, berry_down)} | up_step_berries
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



# start = datetime.now()
# n = int(input())
# berries = [list(map(int, input().split())) + [i] for i in range(n)]
# down_step_berries = []
# up_step_berries = []
# max_high_down_berry = 0
# max_down_up_berry = 0
# start_input = datetime.now()
# for berry in berries:
#     if berry[0] <= berry[1]:
#         if berry[0] > max_high_down_berry:
#             max_high_down_berry = berry[0]
#             down_step_berries.insert(0, berry)
#         else:
#             down_step_berries.append(berry)
#     else:
#         if berry[1] > max_down_up_berry:
#             max_down_up_berry = berry[1]
#             up_step_berries.append(berry)
#         else:
#             up_step_berries.insert(0, berry)

# # print(up_step_berries)
# # print(down_step_berries)
# sum_dist = 0
# max_high = 0
# strat_del = datetime.now()
# for i in up_step_berries:
#     sum_dist += i[0]
#     if sum_dist > max_high:
#         max_high = sum_dist
#     sum_dist -= i[1]
#     # print(sum_dist, i)
# if down_step_berries and max_high < sum_dist + down_step_berries[0][0]:
#     max_high = sum_dist + down_step_berries[0][0]
# print(max_high)
# start_output = datetime.now()
# for i in up_step_berries + down_step_berries:
#     print(i[2] + 1, end=' ')
# finish = datetime.now()
# print(f'{start_input-start=}')
# print(f'{strat_del-start_input=}')
# print(f'{start_output-strat_del=}')
# print(f'{finish-start_output}')