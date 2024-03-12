# quantity = int(input())
# nums = list(map(int, input().split()))

# res = nums[0]
# answer = ''
# for i in range(1, len(nums)):
#     if res % 2 != 0 and nums[i] % 2 != 0:
#         answer += chr(120)
#         res *= nums[i]
#     else:
#         answer += chr(43)
#         res += nums[i]
# # if res % 2 == 0:
# #     result = -1
# print(answer)
# # print(result)


quantity = int(input())
nums =  list(map(int, input().split()))
answer = chr(43) * (quantity - 1)
if sum(nums) % 2 == 0:
    for k, v in enumerate(nums):
        if v % 2 != 0:
            break
    answer = answer[:k] + chr(120) + answer[k+1:]
print(answer)