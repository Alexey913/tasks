from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))

nums = defaultdict(int)
for i in a:
    nums[i] += 1
if len(nums) == 1 or len(nums) == 2 and abs(a[0] - a[1]) < 2:
    answer = 0
elif len(nums) == 2:
    answer = min(nums.values())
else:
    delta = index = 0
    list_keys = sorted(list(nums))
    for i in range(1, len(list_keys)):
        if list_keys[i] - list_keys[i-1] == 1 and nums[list_keys[i]] + nums[list_keys[i-1]] > delta:
            delta = nums[list_keys[i]] + nums[list_keys[i-1]]
            index = i
    if index == 0:
        answer = sum(nums.values()) - max(nums.values())
    else:
        answer = sum(nums.values()) - (nums[list_keys[index]] + nums[list_keys[index-1]])
print(answer)