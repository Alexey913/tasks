# Given an array nums. We define a running sum
# of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return_nums = [nums[0]]
        for i in range(1, len(nums)):
            return_nums.append(nums[i] + return_nums[i-1])
        return return_nums