# C. Саруман
# https://contest.yandex.ru/contest/59542/problems/C/

# Как известно, Саруман Радужный очень любит порядок. Поэтому
# все полки его войска стоят друг за другом, причем каждый
# следующий полк содержит количество орков не меньше, чем
# предыдущий.
# Перед тем как напасть на Хельмову Падь, Саруман решил
# провести несколько вылазок для разведки. Чтобы его отряды
# никто не заметил, он решил каждый раз отправлять несколько
# подряд идущих полков так, чтобы суммарное количество орков
# в них было равно определенному числу. Так как это всего лишь
# разведка, каждый полк после вылазки возвращается на свое
# место. Задачу выбрать нужные полки он поручил Гриме Змеиному
# Языку. А Грима не поскупится на вознаграждение, если вы ему
# поможете.


def find_number(nums: list, l: int, s: int) -> int:
    start = 0
    end = len(nums) - l
    if s < min_regiment or s > sum_regiment or l > len(nums):
        return -1
    if s == sum_regiment:
        return 1
    cur_sum = -1
    mid = 0
    while start <= end:
        mid = (start + end) // 2
        if mid > 0:
            cur_sum = nums[mid + l - 1] - nums[mid-1]
        else:
            cur_sum = nums[mid + l - 1]
        if cur_sum == s:
            return mid + 1
        if cur_sum != s and start == end:
            return -1 
        if cur_sum < s and start != end:
            start = mid + 1
        elif cur_sum > s and start != end:
            end = mid

n, m = map(int, input().split())
army = list(map(int, input().split()))
pref_army = [army[0]]
for i in range(1, n):
    pref_army.append(army[i] + pref_army[i-1])
min_regiment = army[0]
sum_regiment = pref_army[-1]
result = []
for _ in range(m):
    l, s = map(int, input().split())
    result.append(find_number(pref_army, l, s))
for i in result:
    print(i)



# ---------------------------------------------



# def find_number(nums: list, l: int, s: int) -> int:
#     if s < min_regiment or s > sum_regiment or l > len(nums):
#         return -1
#     if s == sum_regiment:
#         return 1
#     start = len(nums) - l
#     while start >= 0:
#         if sum(nums[start: start+l]) == s:
#             return start + 1
#         if sum(nums[start: start+l]) > s and start != 0:
#             start = (start) // 2
#         elif sum(army[start:start+l]) < s and start != 0:
#             start = (start + len(nums)) // 2
#         else:
#             return -1


# n, m = map(int, input().split())
# army = list(map(int, input().split()))
# min_regiment = min(army)
# sum_regiment = sum(army)
# result = []
# for _ in range(m):
#     l, s = map(int, input().split())
#     result.append(find_number(army, l, s))
# for i in result:
#     print(i)


# ---------------------------------------------

# def prefix_sum(nums: list, start:int, l: int):
#     pref = 0
#     for i in range(start, start + l):
#         pref += nums[i]
#     return pref

# def find_number(nums: list, l: int, s: int) -> int:
#     if s < min_regiment or s > sum_regiment or l > len(nums):
#         return -1
#     if s == sum_regiment:
#         return 1
#     start = len(nums) - l
#     while start >= 0:
#         if prefix_sum(nums, start, l) == s:
#             return start + 1
#         if prefix_sum(nums, start, l) > s and start != 0:
#             start = (start) // 2
#         elif prefix_sum(nums, start, l) < s and start != 0:
#             start = (start + len(nums)) // 2
#         else:
#             return -1


# n, m = map(int, input().split())
# army = list(map(int, input().split()))
# min_regiment = min(army)
# sum_regiment = sum(army)
# result = []
# for _ in range(m):
#     l, s = map(int, input().split())
#     result.append(find_number(army, l, s))
# for i in result:
#     print(i)