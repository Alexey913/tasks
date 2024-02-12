# Write a function to find the longest common prefix
# string amongst an array of strings.

# If there is no common prefix, return an empty string "".

strs = ["flower","flow","flight"]

check = strs[0]

while check:
    if len(list(filter(lambda x: x.startswith(check), strs))) == len(strs):
        print(check)
        break
    check = check[:-1]
    