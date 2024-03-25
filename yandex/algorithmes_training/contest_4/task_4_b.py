def search(count_cell):
    if count_cell == 0:
        return 0
    if count_cell < 6:
        return 1
    l = 0
    r = count_cell
    while r > l:
        mid = (l + r) // 2
        
        if check_ships(mid) > count_cell:
            r = mid
        else:
            l = mid + 1
    return l - 1


# def check_ships(max_ship):
#     count = 0
#     for i in range(max_ship):
#         count += (max_ship - i) * (i + 1) + i
#     return count + max_ship - 1


def check_ships(max_ship):
    count = 0
    for i in range(max_ship // 2):
        count += 2 * (max_ship - i) * (i + 1) + max_ship
    if max_ship % 2 != 0:
        count += (max_ship - max_ship // 2) ** 2 + max_ship // 2 + 1
    print(count)
    return count + 1

n = int(input())
print(search(n))
# print(check_ships(5))
