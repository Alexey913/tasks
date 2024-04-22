# a = int(input())
# b = int(input())

# if a > b:
#     max_ = a
#     min_= b
# else:
#     max_ = a
#     min_ = b
# while max_ % min_ != 0:
#     r = max_ % min_
#     max_ = min_
#     min_ = r
# print(int(a * b / min_))

# ---------------------------

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print('\t', end = '')
# for i in range(c, d + 1):
#     print(i, '\t', end = '')
# print()
# for i in range(a, b + 1):
#     print(i, '\t', end ='')
#     for j in range(c, d + 1):
#         print(i * j, '\t', end='')
#     print()

# --------------------------

# a = int(input())
# b = int(input())

# if a % 3:
#     a = a - a % 3 + 3
# count = sum = 0
# for i in range(a, b + 1, 3):
#     count += 1
#     sum += i
# print(sum / count)

# --------------------------

# result = []
# while True:
#     result.append(int(input()))
#     if sum(result) == 0:
#         break
# print(sum([i * i for i in result]))

# --------------------------
# Печать всех элементов
# n = int(input())
# mem = 1
# count = 0
# temp_count = 1
# while count < n:
#     print(mem, end = ' ')
#     temp_count += 1
#     if mem < temp_count:
#         mem += 1
#         temp_count = 1
#     count += 1
    

# # Печать элемента с заданным номером
# n = int(input())
# mem = 0
# count = 1
# while count <= n:
#     mem += 1
#     count += mem
# print(mem)

# --------------------------
# lst = [int(i) for i in input().split()]
# x = int(input())
# result = []
# for i in range(len(lst)):
#     if lst[i] == x:
#         result.append(i)
# if result:
#     print(*result)
# else:
#     print('Отсутствует')


# --------------------------
# Напишите программу, на вход которой подаётся прямоугольная матрица
# в виде последовательности строк. После последней строки матрицы идёт
# строка, содержащая только строку "end" (без кавычек, см. Sample Input).
# Программа должна вывести матрицу того же размера, у которой каждый
# элемент в позиции i, j равен сумме элементов первой матрицы на позициях
# (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний
# элемент находится с противоположной стороны матрицы.
# В случае одной строки/столбца элемент сам себе является соседом
# по соответствующему направлению.

# arr = []
# while True:
#     el = input()
#     if el == 'end':
#         break
#     arr.append([int(i) for i in el.split()])
# weigth = len(arr)
# heigth = len(arr[0])
# result = []
# for i in range(weigth):
#     result.append([])
#     for j in range(heigth):
#         up = -1 if i == 0 else i - 1
#         down = 0 if i == weigth - 1 else i + 1
#         left = -1 if j == 0 else j - 1
#         right = 0 if j == heigth - 1 else j + 1

#         result[i].append(arr[up][j] + arr[down][j] + arr[i][left] + arr[i][right])
# for el in result:
#     print(*el)

# -------------------------------
# Заполнить массив по спирали
# Мое решение
# n = int(input())

# col = row = 0
# num = 0
# count = n / 2
# start_col = start_row = 0
# finish_col = finish_row = n - 1
# result = [[0] * n for _ in range(n)]
# print(result)
# while count > 0:
#     col = start_col
#     while row == start_row:
#         if col <= finish_col:
#             num += 1
#             result[row][col] = num
#             col += 1
#         else:
#             start_row += 1
#             col -= 1
#     row = start_row
#     while col == finish_col:
#         if row <= finish_row:
#             num += 1
#             result[row][col] = num
#             row += 1
#         else:
#             finish_col -= 1
#             row -= 1
#     col = finish_col
#     while row == finish_row:
#         if col >= start_col:
#             num += 1
#             result[row][col] = num
#             col -= 1
#         else:
#             finish_row -= 1
#             col += 1
#     row = finish_row
#     while col == start_col:
#         if row >= start_row:
#             num += 1
#             result[row][col] = num
#             row -= 1
#         else:
#             start_col += 1
#             row += 1
#     count -= 1
# for el in result:
#     print(*el)


# Подсмотренное решение
# используется тот факт, что сумма нмера столбца и строки либо больше n либо меньше
# в тот момент, когда n = сумме номеров строки и столбца - производим поворот
# направление поворота регулируем в зависимости от того, в какую сторону двигались
# направление движения - путем прибавления или вычитания i или j
# направление поворота- путем сравнения суммы i и j с n
# n=int(input())
# t=[[0]*n for i in range (n)]
# i,j=0,0
# for k in range(1, n*n+1):
#     t[i][j]=k
#     if i<=j+1 and i+j<n-1:
#         j+=1
#         for el in t:
#             print(*el)
#     elif i<j and i+j>=n-1:
#         i+=1
#     elif i>=j and i+j>n-1:
#         j-=1
#     elif i>j+1 and i+j<=n-1:
#         i-=1
# for i in range(n):
#     print(*t[i])

# -----------------------------

# def modify_list(l: list[int]):
#     count = 0
#     while count < len(l):
#         if l[count] % 2:
#             l.pop(count)
#         else:
#             l[count] //= 2
#             count += 1

# def modify_list(l):
    # l[:] = [i // 2 for i in l if not i % 2]

# ti = [5, 6, 3, 3, 2, 8, 7]
# modify_list(ti)
# print(ti)
