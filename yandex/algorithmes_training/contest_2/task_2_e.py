# E. Амбициозная улитка
# https://contest.yandex.ru/contest/59540/problems/E/

# Домашний питомец мальчика Васи — улитка Петя.
# Петя обитает на бесконечном в обе стороны вертикальном столбе,
# который для удобства можно представить как числовую прямую.
# Изначально Петя находится в точке 0. Вася кормит Петю ягодами.
# У него есть n ягод, каждая в единственном экземпляре. Вася
# знает, что если утром он даст Пете ягоду с номером i, то
# поев и набравшись сил, за остаток дня Петя поднимется на a
# единиц вверх по столбу, но при этом за ночь, потяжелев,
# съедет на b единиц вниз. Параметры различных ягод могут
# совпадать.
# Пете стало интересно, а как оно там, наверху, и Вася взялся
# ему в этом помочь. Ближайшие n дней он будет кормить Петю
# ягодами из своего запаса таким образом, чтобы максимальная
# высота, на которой побывал Петя за эти n дней была
# максимальной. К сожалению, Вася не умеет программировать,
# поэтому он попросил вас о помощи. Найдите, максимальную
# высоту, на которой Петя сможет побывать за эти n дней и
# в каком порядке Вася должен давать Пете ягоды,
# чтобы Петя смог её достичь!


indexes_down = []
indexes_up = []
last_high_index = first_down_index = 0
up_max_down = up_max_high = down_max_up = 0
sum_dist = max_high = 0
with open('input.txt', 'r') as f:
    n = int(f.readline())
    for i in range(n):
        berry_up, berry_down = map(int, f.readline().split())
        if berry_up < berry_down:
            if berry_up > down_max_up:
                down_max_up = berry_up
                if first_down_index != 0:
                    indexes_down.append(first_down_index)
                first_down_index = i + 1
            else:
                indexes_down.append(i + 1)
        else:
            if berry_down > up_max_down:
                sum_dist += up_max_high
                if sum_dist > max_high:
                    max_high = sum_dist
                sum_dist -= up_max_down
                up_max_down = berry_down
                up_max_high = berry_up
                if last_high_index != 0:
                    indexes_up.append(last_high_index)
                last_high_index = i + 1
            else:
                sum_dist += berry_up
                if sum_dist > max_high:
                    max_high = sum_dist
                sum_dist -= berry_down
                indexes_up.append(i + 1)
sum_dist += up_max_high
if sum_dist > max_high:
    max_high = sum_dist
sum_dist -= up_max_down
if first_down_index:
    indexes_down.insert(0, first_down_index)
    if max_high < sum_dist + down_max_up:
        max_high = sum_dist + down_max_up

if last_high_index:
    indexes_up.append(last_high_index)
print(max_high)
print(" ".join(map(str, indexes_up + indexes_down)))