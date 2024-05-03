# D. Шахматная доска
# https://contest.yandex.ru/contest/59540/problems/D/

# Из шахматной доски по границам клеток выпилили связную
# (не распадающуюся на части) фигуру без дыр.
# Требуется определить ее периметр.


n = int(input())
touches = [tuple(map(int, input().split())) for _ in range(n)]
exclude_sides = 0
checking_cell = []
for i in range(n):
    coord_1 = touches[i][0]
    coord_2 = touches[i][1]
    if (coord_1 + 1, coord_2) in touches:
        exclude_sides += 1
    if (coord_1, coord_2 + 1) in touches:
        exclude_sides += 1
    if (coord_1 - 1, coord_2) in touches:
        exclude_sides += 1
    if (coord_1, coord_2 - 1) in touches:
        exclude_sides += 1
print(len(touches) * 4 - exclude_sides)