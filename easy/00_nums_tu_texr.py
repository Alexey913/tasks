# from math import ceil

# discharges = {0: ['','',''],
#               1: ['тысяч', 'и', 'а'],
#               2: ['миллион', 'а', 'ов'],
#               3: ['миллиард', 'а', 'ов'],
#               4: ['триллион', 'а', 'ов']}

# digits = {1: 'один',
#           2: 'два',
#           3: 'три',
#           4: 'четыре',
#           5: 'пять',
#           6: 'шесть',
#           7: 'семь',
#           8: 'восемь',
#           9: 'девять',
#           0: 'ноль'}

# decades = {
#           1: 'надцать',
#           2: 'двадцать',
#           3: 'тридцать',
#           4: 'сорок',
#           5: 'пятьдесят',
#           6: 'шестьдесят',
#           7: 'семьдесят',
#           8: 'восемьдесят',
#           9: 'девяносто'}

# hundreds = {
#           1: 'сто',
#           2: 'двести',
#           3: 'триста',
#           4: 'четыреста',
#           5: 'пятьсот',
#           6: 'шестьсот',
#           7: 'семьсот',
#           8: 'восемьсот',
#           9: 'девятсот'}

# num = int(input())
# str_num = str(num)
# count_discharges = ceil(len(str_num) / 3) - 1
# start_num = len(str_num) % 3
# while count_discharges >= 0:
#     if start_num == 1:
#         print(str_num[:1] + discharges[1][0])