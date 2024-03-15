# n = int(input())
# numbers = list(map(int, input().split()))
# a, b, k = map(int, input().split())
# max_win = 0
# v_for_count = min(a + len(numbers) * (k + 1), b)
# for v in range(a, v_for_count + 1): 
#     print(f'{v=}')
#     steps_for_stop = v // k
#     if not v % k:
#         steps_for_stop -= 1
#     max_win_right = numbers[steps_for_stop % (len(numbers))]
#     max_win_left = numbers[- steps_for_stop % (len(numbers))]
#     current_max_win = max(max_win_left, max_win_right)
#     if current_max_win > max_win:
#         max_win = current_max_win
# print(max_win)



n = int(input())
numbers = list(map(int, input().split()))
a, b, k = map(int, input().split())
max_win = 0
max_posible_win = max(numbers)
max_count_turn = len(numbers) * k
for v in range(a, b+1, k): 
    steps_for_stop = v // k
    if not v % k:
        steps_for_stop -= 1
    max_win_right = numbers[steps_for_stop % (len(numbers))]
    max_win_left = numbers[-steps_for_stop % (len(numbers))]
    current_max_win = max(max_win_left, max_win_right)
    if current_max_win > max_win:
        max_win = current_max_win
        if max_win == max_posible_win or v - a >= max_count_turn:
            break
print(max_win)


# n = int(input())
# numbers = list(map(int, input().split()))
# a, b, k = map(int, input().split())
# max_win = 0
# for i in range(len(numbers)):
#     if i:
#         v_min = i * k + 1
#     else:
#         v_min = k
#     print(f'{v_min=}')
#     if a % (len(numbers) * k) <= v_min <= b % (len(numbers) * k):
#         if numbers[i] > max_win:
#             max_win = numbers[i]
#         if numbers[0-i] > max_win:
#             max_win = numbers[0-i]
# # for i in range(-len(numbers), 0):
# #     v_min = abs(i * k) + 1
# #     if a % (len(numbers) * k) <= v_min <= b % (len(numbers) * k):
# #         if numbers[i] > max_win:
# #             max_win = numbers[i]
# print(max_win)