# You are given a 0-indexed integer array nums of size n,
# and a 0-indexed integer array pattern of size m consisting
# of integers -1, 0, and 1.

# A subarray nums[i..j] of size m + 1 is said to matchthe pattern
# if the following conditions hold for each element pattern[k]:

# nums[i + k + 1] > nums[i + k] if pattern[k] == 1.
# nums[i + k + 1] == nums[i + k] if pattern[k] == 0.
# nums[i + k + 1] < nums[i + k] if pattern[k] == -1.
# Return the count of subarrays in nums that match the pattern.

 

def check_pattern(nums, pattern):
    for i in range(1, len(nums)):
        if (pattern[i-1] == 1 and nums[i] <= nums[i-1]) or (
            pattern[i-1] == 0 and nums[i] != nums[i-1]) or (
            pattern[i-1] == -1 and nums[i] >= nums[i-1]):
            return False
    return True

nums = [1, 2, 3, 4, 5, 6]
pattern = [1, 1]

result = 0
start = 0
step = len(pattern)
while step < len(nums):
    if check_pattern(nums[start:step + 1], pattern):
        result += 1
    start += 1
    step += 1
print(result)