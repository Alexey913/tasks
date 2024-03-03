# Раунд плей-офф между двумя командами состоит из двух матчей.
# Каждая команда проводит по одному матчу «дома» и «в гостях».
# Выигрывает команда, забившая большее число мячей.
# Если же число забитых мячей совпадает, выигрывает команд,
# забившая больше мячей «в гостях». Если и это число мячей совпадает,
# матч переходит в дополнительный тайм или серию пенальти.

# Вам дан счёт первого матча, а также счёт текущей игры
# (которая ещё не завершилась). Помогите комментатору сообщить,
# сколько голов необходимо забить первой команде, чтобы победить,
# не переводя игру в дополнительное время.

g_1_1, g_2_1 = map(int, input().split(':'))
g_1_2, g_2_2 = map(int, input().split(':'))
is_home = int(input())
first_result = g_1_1 - g_2_1
second_result = g_1_2 - g_2_2
if first_result > 0:
    if second_result >= 0:
        result = 0
    else:
        result = first_result + second_result
        if is_home == 2:
            result += 1
elif first_result == 0:
    if second_result > 0:
        result = 0
    elif second_result == 0:
        result = 1
    else:
        result = - second_result
        if is_home == 2:
            result += 1
else:
    result = abs(first_result + second_result)
    if is_home == 2:
        result += 1

print(result)