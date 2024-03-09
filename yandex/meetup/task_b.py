from collections import defaultdict

commands = {'R':[1, 0], 'L':[-1, 0], 'U':[0, 1], 'D':[0, -1]}

size_1, size_2 = map(int, input().split())
quantity = int(input())
input_commands = input()
step = [0, 0]
# points = {0: step}
# for j, i in enumerate(input_commands, start=1):
#     step = [step[0] + commands[i][0], step[1] + commands[i][1]]
#     points[j] = step
# print(points)
# for v in points.va
points = [step]
for i in input_commands:
    step = [step[0] + commands[i][0], step[1] + commands[i][1]]
    points.append(step)
    minus = 0
    count_minus = 0
for i in points:
    if points.count(i) > 1:
        minus += points.count(i)
        count_minus += 1
quantity -= minus / count_minus
print(quantity)