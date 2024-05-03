# H. Наилучший запрет
# https://contest.yandex.ru/contest/59540/problems/H/

# Константин и Михаил играют в настольную игру «Ярость Эльфов».
# В игре есть n рас и m классов персонажей. Каждый персонаж
# характеризуется своими расой и классом. Для каждой расы и
# каждого класса существует ровно один персонаж такой расы и
# такого класса. Сила персонажа i-й расы и j-го класса равна
# a(i j), и обоим игрокам это прекрасно известно.
# Сейчас Константин будет выбирать себе персонажа. Перед этим
# Михаил может запретить одну расу и один класс, чтобы
# Константин не мог выбирать персонажей, у которых такая раса
# или такой класс. Конечно же, Михаил старается, чтобы
# Константину достался как можно более слабый персонаж,
# а Константин, напротив, выбирает персонажа посильнее.
# Какие расу и класс следует запретить Михаилу?


def find_max(characters, exclude):
    max_pow = [1, [0,0]]
    for i in range(len(characters)):
        if i != exclude[0]:
            for j in range(len(characters[0])):
                if j != exclude[1]:
                    if characters[i][j] > max_pow[0]:
                        max_pow = [characters[i][j], [i, j]]
    return max_pow

def find_max_row(characters, max_pow, exclude):
    max_row = []
    for i in range(len(characters)):
        if i != exclude[0]:
            if max_pow[0] in characters[i]:
                new = sorted(characters[i], reverse=True)
                if new > max_row:
                    max_row = new
                    max_el = [max_row[0], [i, characters[i].index(max_row[0])]]
    return max_el

def find_max_col(characters, max_pow, exclude):
    max_col = []
    for i in range(len(characters[0])):
        temp = []
        if i != exclude[1]:
            for j in range(len(characters)):
                if j != exclude[0]:
                    temp.append(characters[j][i])
            if max_pow[0] in temp:
                new = sorted(temp, reverse=True)
                if new > max_col:
                    max_col = new
                    max_el = [max_col[0], [j, i]]
    return max_el



n, m = map(int, input().split())
characters = [list(map(int, input().split())) for _ in range(n)]
# Максимальный элемент
max_pow_common = find_max(characters, [-1, -1])

# Максимальный элемент с учетом нескольких максимумов по строкам
max_pow = find_max_row(characters, max_pow_common, [-1, -1])
row_1 = max_pow[1][0]
# Вычисление максимума без строки
max_pow = find_max(characters, [row_1, -1])
# Максимальный элемент с учетом нескольких максимумов по столбцам
max_pow = find_max_col(characters, max_pow, [row_1, -1])
col_1 = max_pow[1][1]
# Оставшийся максимум
max_pow = find_max(characters, [row_1, col_1])
max_1 = max_pow[0]


# Максимальный элемент с учетом нескольких максимумов по столбцам
max_pow = find_max_col(characters, max_pow_common, [-1, -1])
col_2 = max_pow[1][1]
# Вычисление максимума без столбца
max_pow = find_max(characters, [-1, col_2])
# Максимальный элемент с учетом нескольких максимумов по столбцам
max_pow = find_max_row(characters, max_pow, [-1, col_2])
row_2 = max_pow[1][0]
# Оставшийся максимум
max_pow = find_max(characters, [row_2, col_2])
max_2 = max_pow[0]
if max_2 > max_1:
    print(row_1 + 1, col_1 + 1)
else:
    print(row_2 + 1, col_2 + 1)