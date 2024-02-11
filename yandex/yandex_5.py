# Е. Близость
# Условие: https://contest.yandex.ru/contest/51022/problems/E/

quan = int(input())
arrays = []
for _ in range(quan):
    size = int(input())
    array = input().split(" ")[:size]
    arrays.append(array)
result = 0
for i in range(len(arrays)):
    for j in range(i+1, len(arrays)):
        for k in range(min(len(arrays[i]), len(arrays[j]))):
            if arrays[i][k] == arrays[j][k]:
                result += 1
print(result)
    

# min_arr = arrays[0]
# min_len = len(min_arr)
# for arr in arrays:
#     if len(arr) < min_len:
#         min_arr = arr
#         min_len = len(arr)
# print(arrays)
# result = min_len
# for arr in arrays:
#     temp = 0
#     for i in range(min_len):
#         if arr[i] == min_arr[i]:
#             temp += 1
#     if temp < result:
#         result = temp
# print(result)