# E. Два из трех
# https://contest.yandex.ru/contest/59541/problems/E/

# Вам даны три списка чисел. Найдите все числа, которые
# встречаются хотя бы в двух из трёх списков.


from collections import defaultdict


n_1 = int(input())
a_1 = set(map(int, input().split()))
n_2 = int(input())
a_2 = set(map(int, input().split()))
n_3 = int(input())
a_3 = set(map(int, input().split()))

nums = defaultdict(int)
for i in list(a_1) + list(a_2) + list(a_3):
    nums[i] += 1
result = [k for k, v in nums.items() if v > 1]
print(*sorted(result))