# 4 задание
# https://edu.tinkoff.ru/selection/76378fbd-1998-48fa-944e-eb736d321f11/exam/244?task=4

# У Кости есть бумажка, на которой написано n чисел.
# Также у него есть возможность не больше, чем k раз,
# взять любое число с бумажки, после чего закрасить одну
# из старых цифр, а на ее месте написать новую произвольную цифру.
# На какое максимальное значение Костя сможет
# увеличить сумму всех чисел на листочке?

def change_number(num: int) -> int:
    new_num = ''
    temp = str(num)
    for i in range(len(temp)):
        if temp[i] == '9':
            new_num += temp[i]
        else:
            new_num += '9'
            break
    new_num += temp[i+1:]
    return int(new_num)

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
start_sum = sum(numbers)
print(start_sum)
for _ in range(k):
    numbers.sort(key=lambda x: change_number(x) - x)
    numbers[-1] = change_number(numbers[-1])
    print(numbers)
print(sum(numbers) - start_sum)


# def change_number(num: int) -> int:
#     new_num = ''
#     temp = str(num)
#     for i in range(len(temp)):
#         if temp[i] == '9':
#             new_num += temp[i]
#         else:
#             new_num += '9'
#             break
#     new_num += temp[i+1:]
#     return int(new_num)

# n, k = map(int, input().split())
# numbers = list(map(int, input().split()))
# start_sum = sum(numbers)
# numbers.sort(key=lambda x: change_number(x) - x, reverse=True)
# for i in range(k):
#     if i < n:
#         numbers[i] = change_number(numbers[i])
# new_sum = sum(numbers)
# print(new_sum - start_sum)