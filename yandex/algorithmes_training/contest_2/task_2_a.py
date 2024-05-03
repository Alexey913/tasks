# A. Минимальный прямоугольник
# https://contest.yandex.ru/contest/59540/problems/

# На клетчатой плоскости закрашено K клеток.
# Требуется найти минимальный по площади прямоугольник,
# со сторонами, параллельными линиям сетки, покрывающий
# все закрашенные клетки.   
    

k = int(input())
coordinates = []
start_point = tuple(map(int, input().split()))
min_x = max_x = start_point[0]
min_y = max_y = start_point[1]
for _ in range(k-1):
    coordinates = tuple(map(int, input().split()))
    if coordinates[0] > max_x:
        max_x = coordinates[0]
    if coordinates[0] < min_x:
        min_x = coordinates[0]
    if coordinates[1] > max_y:
        max_y = coordinates[1]
    if coordinates[1] < min_y:
        min_y = coordinates[1]
print(min_x, min_y, max_x, max_y)