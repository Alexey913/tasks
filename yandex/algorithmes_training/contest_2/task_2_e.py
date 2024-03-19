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



indexes_down = []
indexes_up = []
last_high_index = first_down_index = 0
up_max_down = up_max_high = down_max_up = 0
sum_dist = max_high = 0
with open('input.txt', 'r') as f:
    n = int(f.readline())
    for i in range(n):
        berry_up, berry_down = map(int, f.readline().split())
        # print(f'{berry_up, berry_down}')
        if berry_up < berry_down:
            if berry_up > down_max_up:
                # print(f'{max_high_down_berry=}, {berry_up=}')
                down_max_up = berry_up
                if first_down_index != 0:
                    indexes_down.append(first_down_index)
                first_down_index = i + 1
            else:
                indexes_down.append(i + 1)
        else:
            if berry_down > up_max_down:
                sum_dist += up_max_high
                if sum_dist > max_high:
                    max_high = sum_dist
                sum_dist -= up_max_down
                up_max_down = berry_down
                up_max_high = berry_up
                if last_high_index != 0:
                    indexes_up.append(last_high_index)
                last_high_index = i + 1
            else:
                sum_dist += berry_up
                if sum_dist > max_high:
                    max_high = sum_dist
                sum_dist -= berry_down
                indexes_up.append(i + 1)
        # print(f'{max_high=}, {sum_dist=}, {indexes_up=}, {indexes_down=}')
sum_dist += up_max_high
if sum_dist > max_high:
    max_high = sum_dist
sum_dist -= up_max_down
# print(f'{max_high=}, {max_high_down_berry=}, {sum_dist=}')
if first_down_index:
    indexes_down.insert(0, first_down_index)
    if max_high < sum_dist + down_max_up:
        max_high = sum_dist + down_max_up

if last_high_index:
    indexes_up.append(last_high_index)
print(max_high)
print(" ".join(map(str, indexes_up + indexes_down)))



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