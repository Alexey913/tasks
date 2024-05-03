# I. Пираты Баренцева моря
# https://contest.yandex.ru/contest/59540/problems/I/


# Вася играет в настольную игру «Пираты Баренцева моря»,
# которая посвящена морским битвам. Игровое поле представляет
# собой квадрат из N×N клеток, на котором расположено N
# кораблей (каждый корабль занимает одну клетку).
# Вася решил воспользоваться линейной тактикой, для этого ему
# необходимо выстроить все N кораблей в одном столбце.
# За один ход можно передвинуть один корабль в одну из
# четырёх соседних по стороне клеток. Номер столбца, в
# котором будут выстроены корабли, не важен. Определите
# минимальное количество ходов, необходимых для построения
# кораблей в одном столбце. В начале и процессе игры никакие
# два корабля не могут находиться в одной клетке.


n = int(input())
ships = [list(map(int, input().split())) for _ in range(n)]
x = {i: 0 for i in range(1, n+1)}
y = {i: 0 for i in range(1, n+1)}
for ship in ships:
    x[ship[1]] += 1
    y[ship[0]] += 1
common_steps = 0
for k in y:
    if y[k] == 0:
        for i in range(1, len(y)-k+1):
            if y[k+i] != 0:
                y[k] += 1
                y[k+i] -= 1
                common_steps += i
                break
    else:
        step = 1
        while y[k] > 1:
            if y[k+step] == 0:
                y[k+step] = 1
                y[k] -= 1
                common_steps += step
            step += 1
step_line = []
for line in range(1, n+1):
    temp_steps = 0
    for k, v in x.items():
        temp_steps += abs(line - k) * v
    step_line.append(temp_steps)
print(common_steps + min(step_line))