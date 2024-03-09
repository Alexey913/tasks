# chm = []
# for _ in range(8):
#     chm.append(list("".join(input().split())))
# for i in range(8):
#     for j in range(8):
#         if chm[i][j] == 'R':
#             for k in range(8):
#                 if chm[i][k] != 'R' and chm[i][k] != 'B':
#                     chm[i][k] = '0'
#                 if chm[k][j] != 'R' and chm[k][j] != 'B':
#                     chm[k][j] = '0'
#         if chm[i][j] == 'B':
#             for k in range(8):
#                 if k + i <= 7 and k + j <= 7:
#                     if chm[i+k][j+k] != 'B' and chm[i+k][j+k] != 'R':
#                         chm[i+k][j+k] = '0'
#                 if i - k >= 0 and j + k <= 7:
#                     if chm[i-k][j+k] != 'B' and chm[i-k][j+k] != 'R':
#                         chm[i-k][j+k] = '0'
#                 if k + i <= 7 and j - k >= 0:
#                     if chm[i+k][j-k] != 'B' and chm[i+k][j-k] != 'R':
#                         chm[i+k][j-k] = '0'
#                 if i - k >= 0 and j - k >= 0:
#                     if chm[i-k][j-k] != 'B' and chm[i-k][j-k] != 'R':
#                         chm[i-k][j-k] = '0'
# count_free = 0                    
# for el in chm:
#     print(el)
#     for val in el:
#         if val == '*':
#             count_free += 1
# print(count_free)


chm = []
for _ in range(8):
    chm.append(list("".join(input().split())))
for i in range(8):
    for j in range(8):
        if chm[i][j] == 'R':
            for k in range(8):
                if chm[i][k] == 'R' or chm[i][k] == 'B':
                    if k < j:
                        for m in range(0, k):
                            if chm[i][m] != 'R' and chm[i][m] != 'B' and chm[i][m] != 't':
                                chm[i][m] = 't'
                    else:
                        for m in range(k+1, 8):
                            if chm[i][m] != 'R' and chm[i][m] != 'B' and chm[i][m] != 't':
                                chm[i][m] = 't'
                else:
                    chm[i][k] == '0'
                if chm[k][j] == 'R' or chm[k][j] == 'B':
                    if k < i:
                        for m in range(0, k):
                            if chm[m][j] != 'R' and chm[m][j] != 'B' and chm[m][j] != 't':
                                chm[m][j] = 't'
                    else:
                        for m in range(k+1, 8):
                            if chm[m][j] != 'R' and chm[m][j] != 'B' and chm[m][j] != 't':
                                chm[m][j] = 't'
                else:
                    chm[k][j] = '0'
        for string in chm:
            ['+' if el=='t' else el for el in string]
        # if chm[i][j] == 'B':
        #     for k in range(8):
        #         if k + i <= 7 and k + j <= 7:
        #             if chm[i+k][j+k] != 'B' and chm[i+k][j+k] != 'R':
        #                 chm[i+k][j+k] = '0'
        #             else:
        #                 for m in range(k, k + min(i, j)):
        #                     if chm[i+m][j+m] != 'B' and chm[i+m][j+m] != 'R':
        #                         chm[i+m][j+m] = '+'
        #         if i - k >= 0 and j + k <= 7:
        #             if chm[i-k][j+k] != 'B' and chm[i-k][j+k] != 'R' and chm[i-k][j+k] != '+':
        #                 chm[i-k][j+k] = '0'
        #             else:
        #                 for m in range(k, k + min(i, j)):
        #                     if chm[i-m][j+m] != 'B' and chm[i-m][j+m] != 'R':
        #                         chm[i-m][j+m] = '+'
        #         if k + i <= 7 and j - k >= 0:
        #             if chm[i+k][j-k] != 'B' and chm[i+k][j-k] != 'R' and chm[i+k][j-k] != '+':
        #                 chm[i+k][j-k] = '0'
        #             else:
        #                 for m in range(k, k + min(i, j)):
        #                     if chm[i+m][j-m] != 'B' and chm[i+m][j-m] != 'R':
        #                         chm[i-m][j+m] = '+'
        #         if i - k >= 0 and j - k >= 0:
        #             if chm[i-k][j-k] != 'B' and chm[i-k][j-k] != 'R' and chm[i-k][j-k] != '+':
        #                 chm[i-k][j-k] = '0'
        #             else:
        #                 for m in range(k, k + min(i, j)):
        #                     if chm[i-m][j-m] != 'B' and chm[i-m][j-m] != 'R':
        #                         chm[i-m][j-m] = '+'
count_free = 0                    
for el in chm:
    print(el)
    for val in el:
        if val == '*':
            count_free += 1
print(count_free)