strs = ["flower","flow","flight"]

check = strs[0]

while check:
    if len(list(filter(lambda x: x.startswith(check), strs))) == len(strs):
        print(check)
        break
    check = check[:-1]
    