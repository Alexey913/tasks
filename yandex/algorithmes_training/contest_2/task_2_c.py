n = int, input()
ropes = list(map(int, input().split()))
max_len = max(ropes)
sum_ropes = sum(ropes) - max_len
if sum_ropes < max_len:
    print(max_len - sum_ropes)
elif sum_ropes > max_len:
    print(sum_ropes + max_len)
else:
    print(max_len * 2)