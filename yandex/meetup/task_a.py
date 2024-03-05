nums = list(map(int, input().split()))
nums.sort()
while nums[1] > 0:
    # print(nums)
    nums[0] += 1
    nums[1] -= 1
    nums[2] -= 1
    nums.sort()
    # print(nums)
if nums[2] > 1:
    print('NO')
else:
    print('YES')