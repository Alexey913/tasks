# J. Форматирование документа
# https://contest.yandex.ru/contest/59539/problems/J/


# Условие = .task_1_j_readme.txt


with open('input.txt', 'r', encoding='utf-8') as f:
    w, h, c = map(int, f.readline().split())
    for line in f:
        print(line[:-1])
    print(h)