nums = list(map(int, input().split()))
# result = [n % 2 for n in nums]

result = []
res = nums[0]
for i in range(1, len(nums)):
    if res % 2 != 0 and nums[i] % 2 != 0:
        result.append('*')
        res *= nums[i]
    else:
        result.append('+')
        res += nums[i]
if res % 2 == 0:
    result = -1    
print(nums)
print(result)
print(res)