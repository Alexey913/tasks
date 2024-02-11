# C. Запрос к таблице
# Условие: https://contest.yandex.ru/contest/51022/problems/C/

def input_values(n, table, columns):
    for i in table:
        line = input().split(" ")
        for k, v in zip(columns, line):
            if not table[i] is None:
                table[i].append([k, int(v)])
            else:
                table[i] = [[k, int(v)]]
    return table


def input_conditions(q):
    conditions = []
    for _ in range(q):
        conditions.append(input())
    return conditions


def check_condition(table, condition):
    list_c = condition.split(" ")
    match list_c[1]:
        case '>':
            for i in table.values():
                flag = True
                for v in i:
                    if v[0] == list_c[0] and v[1] <= int(list_c[2]):
                        flag = False
                        break
                if flag == False:
                    for v in i:
                        v[1] = 0
        case '<':
            for i in table.values():
                flag = True
                for v in i:
                    if v[0] == [list_c[0]] and v[1] >= int(list_c[2]):
                        flag = False
                        break
                if flag == False:
                    for v in i:
                        v[1] = 0
    return table


n, m, q = map(int, input().split(" "))
columns = input().split(" ")[:m]
table = {}
for i in range(n):
    table.setdefault(i)
table = input_values(n, table, columns)
conds = input_conditions(q)
for condition in conds:
    table = check_condition(table, condition)
    summ = 0
for i in table.values():
    for v in i:
        summ += v[1]
print(summ)