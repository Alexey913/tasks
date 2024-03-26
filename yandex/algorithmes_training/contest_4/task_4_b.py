def search(count_cell):
    if count_cell == 0 or count_cell == 1:
        return count_cell
    l = 0
    r = count_cell
    while r > l:
        mid = (l + r) // 2
        # формулы вывел, сложив все члены, вынес за скобки количество клеток большоего корабля,
        # умножаем на формулу суммы и вычитаем сумму треугольных чисел + пробелы: формула суммы - 1
        # nes_cells = (mid ** 2 * (mid + 1)) / 2 - (mid ** 3 - mid) / 3 + mid * (mid + 1) / 2 - 1
        # упрощаем формулу, умножаем на 6, чтобы избежать деления
        nes_cells_6 = mid * (mid ** 2 + 6 * mid + 5) - 6
        if nes_cells_6 > count_cell * 6:
            r = mid
        else:
            l = mid + 1
    return l - 1

n = int(input())
print(search(n))


# def check_ships(max_ship):
#     count = 0
#     for i in range(max_ship):
#         count += (max_ship - i) * (i + 1) + i
#     return count + max_ship - 1


# def check_ships(max_ship):
#     count = 0
#     for i in range(max_ship // 2):
#         count += 2 * (max_ship - i) * (i + 1) + max_ship
#     if max_ship % 2 != 0:
#         count += (max_ship - max_ship // 2) ** 2 + max_ship // 2 + 1
#     print(count)
#     return count + 1

# n = int(input())
# print(search(n))
# print(check_ships(5))
