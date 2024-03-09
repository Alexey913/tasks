quantity = int(input())
result = []
nums = []
for i in range(quantity):
    nums.append(list(map(int, input().split())))
for n in nums:
    max_ = max(n)
    min_ = min(n)
    # n.sort()
    # while n[1] > 0:
    #     n[0] += 1
    #     n[1] -= 1
    #     n[2] -= 1
    #     n.sort()
    if n[2] > 1:
        print('No')
    else:
        print('Yes')
# for res in result:
#     print(res)