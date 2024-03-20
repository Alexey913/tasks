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