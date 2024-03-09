string = input()
minimum = ord(string[0])
maximum = ord(string[0])
min_index = 0
max_index = 0
delta_index = 0
for i in range(len(string)):
    cur = string[i]
    ord_cur = ord(cur)
    if ord_cur < minimum:
        minimum = ord_cur
        min_index = i
        delta_index = min_index - max_index
    if ord_cur > maximum:
        maximum = ord_cur
        max_index = i
        delta_index = max_index - min_index
    if ord_cur == minimum and abs(max_index - i) < delta_index:
        min_index = i
    if ord_cur == maximum and abs(i - min_index) < delta_index:
        max_index = i
print(string[min(min_index, max_index) : max(min_index, max_index)+1])