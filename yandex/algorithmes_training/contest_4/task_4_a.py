# A. Быстрый поиск в массиве
# https://contest.yandex.ru/contest/59542/problems/


# Дан массив из N целых чисел. Все числа от −10^9 до 10^9.
# Нужно уметь отвечать на запросы вида “Cколько чисел имеют
# значения от L до R?”.


def search_down(down: int, numbers: list[int]) -> int:
    l = 0
    r = len(numbers) - 1
    while r > l:
        mid = (l + r) // 2
        if numbers[mid] < down:
            l = mid + 1
        else:
            r = mid
    return l


def search_up(up: int, numbers: list[int]) -> int:
    l = 0
    r = len(numbers) - 1
    while r > l:
        mid = (l + r + 1) // 2
        if numbers[mid] <= up:
            l = mid
        else:
            r = mid - 1
    return l


def find_len_between_limits(down: int, up: int, numbers: list[int]) -> int:
    if down > up:
        down, up = up, down
    if min_num > up or max_num < down:
        return 0
    if min_num >= down:
        down_index = 0
    else:
        down_index = search_down(down, numbers)
    if max_num <= up:
        up_index = len(numbers) - 1
    else:
        up_index = search_up(up, numbers)
    return up_index - down_index + 1


result = []
with open('input.txt', 'r') as f:
    n = int(f.readline())
    nums = sorted(list(map(int, f.readline().split())))
    min_num = min(nums)
    max_num = max(nums)
    k = int(f.readline())
    for _ in range(k):
        result.append(find_len_between_limits(*map(int, f.readline().split()), nums))
f.close()
print(*result)