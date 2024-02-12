# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for k, v in enumerate(nums):
        #     j = target - v
        #     lim = k + 1
        #     if j in nums[lim:]:
        #         return [k, nums.index(j, lim)]
        dict_value={}
        for k, v in enumerate(nums):
            if v in dict_value:
                return dict_value[v], k
            dict_value[target-v] = k