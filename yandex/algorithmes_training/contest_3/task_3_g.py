# G. Построить квадрат
# https://contest.yandex.ru/contest/59541/problems/G/

# Задано множество, состоящее из N различных точек на
# плоскости. Координаты всех точек — целые числа. Определите,
# какое минимальное количество точек нужно добавить во
# множество, чтобы нашлось четыре точки, лежащие в вершинах
# квадрата.


from collections import defaultdict


n = int(input())
coord = set()
for _ in range(n):
    coord.add(tuple(map(int, input().split())))
result = defaultdict(list)
# for i in coord:
#     for p in range(n):
#         if 