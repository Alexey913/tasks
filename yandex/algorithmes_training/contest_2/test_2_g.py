t = int(input())
result = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    temp_list = []
    count_el = 0
    min_el = max(a)
    for i in range(len(a)):
        if a[i] < min_el:
            min_el = a[i]
        if a[i] >= count_el + 1 and min_el >= count_el + 1:
            count_el += 1
        else:
            min_el = a[i]
            temp_list.append(count_el)
            count_el = 1
    temp_list.append(count_el)
    result.append(temp_list)
for i in result:
    print(len(i))
    print(*i, sep = ' ')