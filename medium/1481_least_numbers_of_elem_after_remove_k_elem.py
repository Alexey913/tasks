# Given an array of integers arr and an integer k.
# Find the least number of unique integers afte
# removing exactly k elements.


from typing import List
from collections import defaultdict


def findLeastNumOfUniqueInts(arr: List[int], k: int) -> int:
        numbers = defaultdict(int)
        for i in arr:
            numbers[i] += 1
        count_remove = 0
        for i in sorted(numbers.values()):
            if k >= i:
                k -= i
                count_remove += 1
            else:
                break
        return len(set(arr)) - count_remove
            

# arr = [4,3,1,1,3,3,2]
# k = 3
            
arr = [1]
k = 1

# arr  = [2,1,1,3,3,3]
# k = 3
print(findLeastNumOfUniqueInts(arr, k))