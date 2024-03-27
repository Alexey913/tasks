from math import ceil

n = int(input())

s = (-1 + (1 + 8 * n) ** 0.5) / 2
block = ceil(s)



print(block)