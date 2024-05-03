# G. Ни больше ни меньше
# https://contest.yandex.ru/contest/59540/problems/G/

# Дан массив целых положительных чисел a длины n. Разбейте
# его на минимально возможное количество отрезков, чтобы
# каждое число было не меньше длины отрезка которому оно
# принадлежит. Длиной отрезка считается количество чисел в нем.
# Разбиение массива на отрезки считается корректным, если
# каждый элемент принадлежит ровно одному отрезку.


t = int(input())
result = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    temp_list = []
    count_el = 0
    min_el = max(a)
    for i in range(len(a)):
        if a[i] < min_el:
            min_el = a[i]
        if a[i] >= count_el + 1 and min_el >= count_el + 1:
            count_el += 1
        else:
            min_el = a[i]
            temp_list.append(count_el)
            count_el = 1
    temp_list.append(count_el)
    result.append(temp_list)
for i in result:
    print(len(i))
    print(*i, sep = ' ')