# 3 задание
# https://edu.tinkoff.ru/selection/76378fbd-1998-48fa-944e-eb736d321f11/exam/244?task=3

# У Кати насыщенный день на работе. Ей надо передать n разных договоров коллегам.
# Все встречи происходят на разных этажах, а между этажами можно перемещаться
# только по лестничным пролетам — считается, что это улучшает физическую форму
# сотрудников. Прохождение каждого пролета занимает ровно 1 минуту.
# Сейчас Катя на парковочном этаже, планирует свой маршрут. Коллег можно
# посетить в любом порядке, но один из них покинет офис через t минут.
# С парковочного этажа лестницы нет — только лифт, на котором можно подняться
# на любой этаж.
# В итоге план Кати следующий:
# 1. Подняться на лифте на произвольный этаж. Считается, что лифт поднимается на
# любой этаж за 0 минут.
# 2. Передать всем коллегам договоры, перемещаясь между этажами по лестнице.
# Считается, что договоры на этаже передаются мгновенно. 
# 3. В первые t минут передать договор тому коллеге, который планирует уйти.
# 4. Пройти минимальное количество лестничных пролетов.
# Помогите Кате выполнить все пункты ее плана.


# n, t = map(int, input().split())
# floors = list(map(int, input().split()))
# staff_out = int(input())

# sum_time = time_to_out_staff_down = 0
# result_time = 0
# for i in range(1, len(floors)):
#     if i-1 == t:
#         time_to_out_staff_down = sum_time
#     sum_time += floors[i] - floors[i-1]
# time_to_out_staff_up = sum_time - time_to_out_staff_down

# if time_to_out_staff_down <= t or time_to_out_staff_up <= t:
#     result_time = sum_time
# elif time_to_out_staff_down <= time_to_out_staff_up:
#     result_time = time_to_out_staff_down * 2 + time_to_out_staff_up
# else:
#     result_time = time_to_out_staff_up * 2 + time_to_out_staff_down
# print(result_time)

n, t = map(int, input().split())
floors = list(map(int, input().split()))
staff_out = int(input())

max_floor = floors[-1]
min_floor = floors[0]
staff_out_floor = floors[staff_out-1]
if staff_out_floor - min_floor <= t or max_floor - staff_out_floor <= t:
    result_time = max_floor - min_floor
else:
    first_way = staff_out_floor - 2 * min_floor + max_floor
    second_way = 2 * max_floor - staff_out_floor - min_floor
    result_time = min(first_way, second_way)
print(result_time)