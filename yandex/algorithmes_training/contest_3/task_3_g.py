from collections import defaultdict


n = int(input())
coord = set()
for _ in range(n):
    coord.add(tuple(map(int, input().split())))
result = defaultdict(list)
# for i in coord:
#     for p in range(n):
#         if 