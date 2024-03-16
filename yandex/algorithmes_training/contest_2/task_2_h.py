def find_max(characters, exclude):
    max_pow = [1, [0,0]]
    for i in range(len(characters)):
        if i != exclude[0]:
            for j in range(len(characters[0])):
                if j != exclude[1]:
                    if characters[i][j] > max_pow[0]:
                        max_pow = [characters[i][j], [i, j]]
    return max_pow

def find_max_row(characters, max_pow):
    max_row = []
    for i in range(len(characters)):
        if max_pow[0] in characters[i]:
            new = sorted(characters[i], reverse=True)
            if new > max_row:
                max_row = new
                max_el = [max_row[0], [i, characters[i].index(max_row[0])]]
    return max_el

def find_max_col(characters, max_pow):
    max_col = []
    for i in range(len(characters[0])):
        temp = []
        for j in range(len(characters)):
            temp.append(characters[j][i])
        if max_pow[0] in temp:
            new = sorted(temp, reverse=True)
            if new > max_col:
                max_col = new
                max_el =[max_col[0], [j, i]]
    return max_el



n, m = map(int, input().split())
characters = [list(map(int, input().split())) for _ in range(n)]
max_pow = find_max(characters, [-1, -1])
max_without_row = find_max(characters, [max_pow[1][0], -1])
max_without_col = find_max(characters, [-1, max_pow[1][1]])
if max_without_col[0] >= max_without_row[0]:
    max_pow = find_max_row(characters, max_pow)
    row = max_pow[1][0]
    max_pow = find_max(characters, [row, -1])
    col = max_pow[1][1]
else:
    max_pow = find_max_col(characters, max_pow)
    col = max_pow[1][1]
    max_pow = find_max(characters, [-1, col])
    row = max_pow[1][0]
print(row + 1, col + 1)