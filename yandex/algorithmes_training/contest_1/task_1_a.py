# A. Покраска деревьев
# https://contest.yandex.ru/contest/59539/problems/A/


# Вася и Маша участвуют в субботнике и красят стволы деревьев в белый цвет.
# Деревья растут вдоль улицы через равные промежутки в 1 метр.
# Одно из деревьев обозначено числом ноль,
# деревья по одну сторону занумерованы положительными числами 1,2 и т.д.,
# а в другую — отрицательными −1,−2 и т.д.
# Ведро с краской для Васи установили возле дерева P, а для Маши — возле дерева Q.
# Ведра с краской очень тяжелые и Вася с Машей не могут их переставить,
# поэтому они окунают кисть в ведро и уже с этой кистью идут красить дерево.
# Краска на кисти из ведра Васи засыхает,
# когда он удаляется от ведра более чем на V метров, а из ведра Маши — на M метров.
# Определите, сколько деревьев может быть покрашено.


p, v = map(int, input().split())
q, m = map(int, input().split())

# time_1 = datetime.datetime.now()
min_high = min(p + v, q + m)
max_high = max(p + v, q + m)
min_low = min(p - v, q - m)
max_low = max(p - v, q - m)
if max_low <= min_high:
    result = max_high - min_low + 1
else:
    result = 2 * m + 2 * v + 2
print(result)
# print(datetime.datetime.now() - time_1)

# print([i for i in range(p-v, p+v+1)])
# print([j for j in range(q-m, q+m+1)])
# time_2 = datetime.datetime.now()
# result = len(set([i for i in range(p-v, p+v+1)] + [j for j in range(q-m, q+m+1)]))
# print(result)
# print(datetime.datetime.now() - time_2)