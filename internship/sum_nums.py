def sum_nums(nums: list[int]):
    if len(nums) == 1:
        return nums[0]
    # sum_ = nums.pop(nums[0])
    # return sum_ + sum_nums(nums)
    return nums[0] + sum_nums(nums[1:])

def count_elem(nums: list[int]):
    if not nums:
        return 0
    return 1 + count_elem(nums[1:])

def max_el(nums: list[int]):
    if len(nums) == 2:
        if nums[0] < nums[1]:
            return nums[1]
        else:
            return nums[0]
    sub_max = max_el(nums[1:])
    if sub_max > nums[0]:
        return sub_max
    else:
        return nums[0]

numbers = [1, 2, 200, 4, 5]
print(sum_nums(numbers))
print(count_elem(numbers))
print(max_el(numbers))