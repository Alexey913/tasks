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
                            if chm[i][m] != 'R' and chm[i][m] != 'B' and chm[i][m] != '0':
                                chm[i][m] = 't'
                    elif k > j:
                        for m in range(k, 8):
                            if chm[i][m] != 'R' and chm[i][m] != 'B'and chm[i][m] != '0':
                                chm[i][m] = 't'
            for k in range(8):
                if chm[i][k] == '*':
                    chm[i][k] = '0'
                if chm[i][k] == 't':
                    chm[i][k] = '*'

            for k in range(8):
                if chm[k][j] == 'R' or chm[k][j] == 'B':
                    if k < i:
                        for m in range(0, k):
                            if chm[m][j] != 'R' and chm[m][j] != 'B' and chm[m][j] != '0':
                                chm[m][j] = 't'
                    elif k > i:
                        for m in range(k, 8):
                            if chm[m][j] != 'R' and chm[m][j] != 'B' and chm[m][j] != '0':
                                chm[m][j] = 't'
            for k in range(8):
                if chm[k][j] == '*':
                    chm[k][j] = '0'
                if chm[k][j] == 't':
                    chm[k][j] = '*'
        
        if chm[i][j] == 'B':
            for k in range(1, 8):
                if k + i <= 7 and k + j <= 7:
                    if chm[i+k][j+k] == 'B' or chm[i+k][j+k] == 'R':
                        for m in range(k, 8):
                            if m + i <= 7 and m + j <= 7:
                                if chm[i+m][j+m] != 'R' and chm[i+m][j+m] != 'B' and chm[i+m][j+m] != '0':
                                    chm[i+m][j+m] = 't'
                    elif chm[i+k][j+k] != 'B' and chm[i+k][j+k] != 'R' and chm[i+k][j+k] != 't':
                        chm[i+k][j+k] = '0'
            for k in range(1, 8):
                if k + i <= 7 and k + j <= 7:
                    if chm[i+k][j+k] == 't':
                        chm[i+k][j+k] = '*'

            for k in range(1, 8):
                if i - k >= 0 and j + k <= 7:
                    if chm[i-k][j+k] == 'B' or chm[i-k][j+k] == 'R':
                        for m in range(k, 8):
                            if i - m >= 0 and j + m <= 7:
                                if chm[i-m][j+m] != 'R' and chm[i-m][j+m] != 'B' and chm[i-m][j+m] != '0':
                                    chm[i-m][j+m] = 't'
                    elif chm[i-k][j+k] != 'B' and chm[i-k][j+k] != 'R' and chm[i-k][j+k] != 't':
                        chm[i-k][j+k] = '0'
            for k in range(1, 8):
                if i - k >= 0 and j + k <= 7:
                    if chm[i-k][j+k] == 't':
                        chm[i-k][j+k] = '*'       

            for k in range(1, 8):
                if k + i <= 7 and j - k >= 0:
                    if chm[i+k][j-k] == 'B' or chm[i+k][j-k] == 'R':
                        for m in range(k, 8):
                            if m + i <= 7 and j - m >= 0:
                                if chm[i+m][j-m] != 'R' and chm[i+m][j-m] != 'B' and chm[i+m][j-m] != '0':
                                    chm[i+m][j-m] = 't'
                    elif chm[i+k][j-k] != 'B' and chm[i+k][j-k] != 'R' and chm[i+k][j-k] != 't':
                        chm[i+k][j-k] = '0'
            for k in range(1, 8):
                if k + i <= 7 and j - k >= 0:
                    if chm[i+k][j-k] == 't':
                        chm[i+k][j-k] = '*'

            for k in range(1, 8):                             
                if i - k >= 0 and j - k >= 0:
                    if chm[i-k][j-k] == 'B' or chm[i-k][j-k] == 'R':
                        for m in range(k, 8):
                            if i - m >= 0 and j - m >= 0:
                                if chm[i-m][j-m] != 'R' and chm[i-m][j-m] != 'B' and chm[i-m][j-m] != '0':
                                    chm[i-m][j-m] = 't'
                    elif chm[i-k][j-k] != 'B' and chm[i-k][j-k] != 'R' and chm[i-k][j-k] != 't':
                        chm[i-k][j-k] = '0'
            for k in range(1, 8):                             
                if i - k >= 0 and j - k >= 0:
                    if chm[i-k][j-k] == 't':
                        chm[i-k][j-k] = '*'
count_free = 0                    
for el in chm:
    for val in el:
        if val == '*':
            count_free += 1
print(count_free)