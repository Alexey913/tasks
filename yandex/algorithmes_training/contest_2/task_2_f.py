# F. Колесо Фортуны
# https://contest.yandex.ru/contest/59540/problems/F/

# Условие - ./task_2_f_readme.txt


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