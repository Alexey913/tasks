from math import ceil
from decimal import Decimal

n = int(input())

s = (-1 + Decimal(1 + 8 * n) ** Decimal(0.5)) / 2
block = ceil(s)
start_elem = (block - 1) * (block) // 2 + 1
up = n - start_elem + 1
down = block - (n - start_elem)
if block % 2 == 0:
    down, up = up, down


print(f'{up}/{down}')