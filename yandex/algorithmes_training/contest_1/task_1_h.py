# H. Забег по стадиону
# https://contest.yandex.ru/contest/59539/problems/H/


# Стадион представляет собой окружность длиной L метров,
# на которой отмечена точка старта. По стадиону бегают Кирилл и Антон.
# У каждого мальчика есть своя точка старта (она представляет собой
# расстояние в метрах от старта, отсчитанное по часовой стрелке)
# и своя скорость в метрах в секунду (положительная скорость означает,
# что мальчик бежит по часовой стрелке, отрицательная — что бежит
# против часовой, а нулевая — что он стоит на месте).
# Вам нужно сказать, через какое минимальное время мальчики окажутся
# на одинаковом расстоянии от точки старта. Обратите внимание,
# что в этот момент они могли находиться в разных точках.
# Расстоянием от точки A до точки B называется минимальное из
# расстояний, которое нужно пробежать из точки A по или против часовой
# стрелки, чтобы оказаться в B.


l, x_1, v_1, x_2, v_2 = map(int, input().split())
center_1 = round(abs(x_1 - x_2) / 2, 10)
center_2 = round((l - center_1) / 2, 10)
if center_1 == 0 or center_2 == 0:
    total_time = 0
start_time = 0
end_time = 1
step = 1

while center_1 >= 0 and center_1 <= l or center_2 >= 0 and center_2 <= l:
    delta = end_time - start_time
    center_1 = round(abs(x_1 + v_1 * delta * step - (x_2 + v_2 * delta * step)), 10)
    center_2 = round((l - center_1) / 2, 10)
    start_time = end_time
    end_time += delta
    step += 1
    total_time += step
    print(center_1, center_2)
    print(start_time, end_time)