# You are given an array of positive integers nums of length n.
# A polygon is a closed plane figure that has at
# least 3 sides. The longest side of a polygon
# is smaller than the sum of its other sides.

# Conversely, if you have k (k >= 3) positive real
# numbers a1, a2, a3, ..., ak
# where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak,
# then there always exists a polygon
# with k sides whose lengths are a1, a2, a3, ..., ak.

# The perimeter of a polygon is the sum of lengths of its sides.

# Return the largest possible perimeter of a polygon
# whose sides can be formed from nums,
# or -1 if it is not possible to create a polygon.

from typing import List
from itertools import combinations


def largestPerimeter(nums: List[int]) -> int:
    while nums:
        if max(nums) >= sum(nums) - max(nums):
            nums.remove(max(nums))
        else:
            return sum(nums)
    return -1

# nums = [1,12,1,2,5,50,3]
# nums = [5, 5, 5]
nums = [5,5,50]
print(largestPerimeter(nums))