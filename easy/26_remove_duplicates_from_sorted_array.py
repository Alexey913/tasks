# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique
# element appears only once. The relative order of the
# elements should be kept the same. Then return
# the number of unique elements in nums.

# Consider the number of unique elements of nums to be k,
# to get accepted, you need to do the following things:

# Change the array nums such that the first k elements
# of nums contain the unique elements in the order they were
# present in nums initially. The remaining elements of nums
# are not important as well as the size of nums.
# Return k.


from typing import List

def removeDuplicates(nums: List[int]) -> int:
    # set_nums = sorted(list(set(nums)))
    # length = len(set_nums)
    # for i in range(length):
    #     nums[i] = set_nums[i]
    # return length
    nums[:] = sorted(list(set(nums)))
    return len(nums)

# nums = [0,0,1,1,1,2,2,3,3,4]
nums = [-1,0,0,0,0,3,3]
print(removeDuplicates(nums))
print(nums)