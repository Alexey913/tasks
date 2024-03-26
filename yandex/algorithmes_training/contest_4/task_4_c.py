# def prefix_sum(nums: list, start:int, l: int, s: int):
#     pref = 0
#     for i in range(start, start + l):
#         if pref < s:
#             pref += nums[i]
#         else:
#             return -1
#     return pref


def find_number(nums: list, l: int, s: int) -> int:
    start = l - 1
    end = len(nums) - l + 1
    if s < min_regiment or s > sum_regiment or l > len(nums):
        return -1
    if s == sum_regiment:
        return 1
    while end <= len(nums) + 1 - l and start >= l - 1:
        mid = (start + end + 1) // 2
        # if mid >= l:
        cur_sum = nums[mid + l - 1] - nums[mid-1]
        # else:
        #     cur_sum = pref_army[mid]
        print(f'{start=}')
        print(f'{end=}')
        print(f'{mid=}')
        print(f'{cur_sum=}')
        if cur_sum == s:
            return mid + 1
        if cur_sum != s and start == end:
            return -1 
        if cur_sum < s and start != end:
            end = mid + 1
        elif cur_sum > s and start != end:
            start = mid
# 1 3 5 7  9  10 10
# 1 4 9 16 25 35 45


# sum(2, l) = 5 + 7+ 9 + 10 = 31 = p(2 + l - 1) - p(2-1)
# sum(3, 3) = 7 + 9 + 10 = 26 = p(3 + 3 - 1) - p(3-1)



n, m = map(int, input().split())
army = list(map(int, input().split()))
pref_army = [army[0]]
for i in range(1, n):
    pref_army.append(army[i] + pref_army[i-1])
min_regiment = army[0]
sum_regiment = pref_army[-1]
result = []
print(f'{army=}')
print(f'{pref_army=}')
for _ in range(m):
    l, s = map(int, input().split())
    result.append(find_number(pref_army, l, s))
for i in result:
    print(i)



# ---------------------------------------------



# def find_number(nums: list, l: int, s: int) -> int:
#     if s < min_regiment or s > sum_regiment or l > len(nums):
#         return -1
#     if s == sum_regiment:
#         return 1
#     start = len(nums) - l
#     while start >= 0:
#         if sum(nums[start: start+l]) == s:
#             return start + 1
#         if sum(nums[start: start+l]) > s and start != 0:
#             start = (start) // 2
#         elif sum(army[start:start+l]) < s and start != 0:
#             start = (start + len(nums)) // 2
#         else:
#             return -1


# n, m = map(int, input().split())
# army = list(map(int, input().split()))
# min_regiment = min(army)
# sum_regiment = sum(army)
# result = []
# for _ in range(m):
#     l, s = map(int, input().split())
#     result.append(find_number(army, l, s))
# for i in result:
#     print(i)


# ---------------------------------------------

# def prefix_sum(nums: list, start:int, l: int):
#     pref = 0
#     for i in range(start, start + l):
#         pref += nums[i]
#     return pref

# def find_number(nums: list, l: int, s: int) -> int:
#     if s < min_regiment or s > sum_regiment or l > len(nums):
#         return -1
#     if s == sum_regiment:
#         return 1
#     start = len(nums) - l
#     while start >= 0:
#         if prefix_sum(nums, start, l) == s:
#             return start + 1
#         if prefix_sum(nums, start, l) > s and start != 0:
#             start = (start) // 2
#         elif prefix_sum(nums, start, l) < s and start != 0:
#             start = (start + len(nums)) // 2
#         else:
#             return -1


# n, m = map(int, input().split())
# army = list(map(int, input().split()))
# min_regiment = min(army)
# sum_regiment = sum(army)
# result = []
# for _ in range(m):
#     l, s = map(int, input().split())
#     result.append(find_number(army, l, s))
# for i in result:
#     print(i)