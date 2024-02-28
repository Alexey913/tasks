n = int(input())
nums = []
step = 1
while n > 0:
    if nums.count(step) < step:
        nums.append(step)
        n -= 1
    else:
        step += 1
print("".join(map(str, nums)))