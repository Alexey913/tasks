# def sort_coordinate(data):
#     if len(data) < 2:
#         return data
#     else:
#         pivot = data[len(data) // 2]
#         print(pivot)
#         less = [i for i in data if i[0] <= pivot[0]]
#         print(less)
#         more = [i for i in data if i[0] > pivot[0]]
#         print(more)
#         return sort_coordinate(less) + pivot + sort_coordinate(more)
    
    

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