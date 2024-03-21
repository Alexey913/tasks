# with open('input.txt', 'r') as f:
#     n, k = map(int, f.readline().split())
#     nums = list(map(int, f.readline().split()))
# for i in range(len(nums)):
#     if nums.count(nums[i]) > 1 and nums[i] in nums[i+1:i+k+1]:
#         print('YES')
#         break
# else:
#     print('NO')


from collections import defaultdict


with open('input.txt', 'r') as f:
    n, k = map(int, f.readline().split())
    nums = list(map(int, f.readline().split()))
    # nums = {k: v for k, v in enumerate(map(int, f.readline().split()))}
f.close()
check_nums = defaultdict(int)
for v in nums:
    check_nums[v] += 1
for i in range(n):
    if check_nums[nums[i]] > 1 and nums[i] in nums[i+1:i+k+1]:
        print('YES')
        break
else:
    print('NO')