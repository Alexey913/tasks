# F. Миша и математика
# https://contest.yandex.ru/contest/59539/problems/F/


# Миша сидел на занятиях математики в Высшей школе экономики
# и решал следующую задачу: дано n целых чисел и нужно расставить
# между ними знаки + и × так, чтобы результат полученного
# арифметического выражения был нечётным (например, между числами 
# 5, 7, 2, можно расставить арифметические знаки следующим образом: 
# 5×7+2=37). Так как примеры становились все больше и больше,
# а Миша срочно убегает в гости, от вас требуется написать
# программу решающую данную задачу.



# quantity = int(input())
# nums = list(map(int, input().split()))

# res = nums[0]
# answer = ''
# for i in range(1, len(nums)):
#     if res % 2 != 0 and nums[i] % 2 != 0:
#         answer += chr(120)
#         res *= nums[i]
#     else:
#         answer += chr(43)
#         res += nums[i]
# # if res % 2 == 0:
# #     result = -1
# print(answer)


quantity = int(input())
nums =  list(map(int, input().split()))
answer = chr(43) * (quantity - 1)
if sum(nums) % 2 == 0:
    for k, v in enumerate(nums):
        if v % 2 != 0:
            break
    answer = answer[:k] + chr(120) + answer[k+1:]
print(answer)