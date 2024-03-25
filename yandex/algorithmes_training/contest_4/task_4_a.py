from datetime import datetime

def search_down(down: int, numbers: list[int]) -> int:
    l = 0
    r = len(numbers) - 1
    while r > l:
        mid = (l + r) // 2
        if numbers[mid] <= down:
            l = mid + 1
        else:
            r = mid
    return l


def search_up(up: int, numbers: list[int]) -> int:
    l = 0
    r = len(numbers) - 1
    while r > l:
        mid = (l + r + 1) // 2
        if numbers[mid] < up:
            l = mid
        else:
            r = mid - 1
    return l


def find_len_between_limits(down: int, up: int, numbers: list[int]) -> int:
    
    # print(f'{down=}')
    # print(f'{up=}')
    # print(numbers)
    if down == up:
        return numbers.count(down)
    if down > up:
        down, up = up, down
    if min_num >= down:
        down_index = 0
    else:
        down_index = search_down(down, numbers)
    if max_num <= up:
        up_index = len(numbers) - 1
    else:
        up_index = search_up(up, numbers)
    # print(f'{up_index=}')
    # print(f'{down_index=}')
    return up_index - down_index + 1


# n = int(input())
# nums = sorted(list(map(int, input().split())))
# k = int(input())
# result = []
# min_num = min(nums)
# max_num = max(nums)
# set_nums = set(nums)
# for _ in range(k):
#     result.append(find_len_between_limits(*map(int, input().split()), nums))
# print(*result)


start = datetime.now()
res = []
result = []
with open('input.txt', 'r') as f:
    n = int(f.readline())
    nums = sorted(list(map(int, f.readline().split())))
    set_nums = set(nums)
    min_num = min(nums)
    max_num = max(nums)
    k = int(f.readline())
    for _ in range(k):
        result.append(find_len_between_limits(*map(int, f.readline().split()), nums))
f.close()
print(result)
# for i in res:
#     print(*i)
#     x = find_len_between_limits(*i, nums)
#     print(f'{x=}')
#     result.append(x)
# print(*result)