# Given a 0-indexed m x n integer matrix matrix,
# create a new 0-indexed matrix called answer.
# Make answer equal to matrix, then replace each element
# with the value -1 with the maximum element
# in its respective column.

# Return the matrix answer.

def transpose(matrix):
    return [list(r) for r in zip(*matrix)]

matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
trans_m = transpose(matrix)
for i in trans_m:
    while -1 in i:
        i[i.index(-1)] = max(i)
print(matrix)
print(trans_m)
print(transpose(trans_m))