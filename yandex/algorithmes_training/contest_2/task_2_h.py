def find_max(characters, exclude):
    max_pow = [1, [0,0]]
    for i in range(len(characters)):
        if i != exclude[0]:
            for j in range(len(characters[0])):
                if j != exclude[1]:
                    if characters[i][j] > max_pow[0]:
                        max_pow = [characters[i][j], [i, j]]
    return max_pow

n, m = map(int, input().split())
characters = [list(map(int, input().split())) for _ in range(n)]
max_pow = find_max(characters, [-1, -1])
max_without_row = find_max(characters, [max_pow[1][0], -1])
max_without_col = find_max(characters, [-1, max_pow[1][1]])
if max_without_col[0] >= max_without_row[0]:
    row = max_pow[1][0]
    max_pow = find_max(characters, [row, -1])
    col = max_pow[1][1]
else:
    col = max_pow[1][1]
    max_pow = find_max(characters, [-1, col])
    row = max_pow[1][0]
print(row + 1, col + 1)