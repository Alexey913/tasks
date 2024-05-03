# B. Анаграмма?
# https://contest.yandex.ru/contest/59541/problems/B/

# Задано две строки, нужно проверить, является ли одна
# анаграммой другой. Анаграммой называется строка,
# полученная из другой перестановкой букв.


from collections import defaultdict

word_1 = input()
word_2 = input()

chars = defaultdict(int)
for i in word_1:
    chars[i] += 1

for i in word_2:
    if not i in chars or chars[i] == 0:
        print('NO')
        break
    else:
        chars[i] -= 1
else:
    print('YES')