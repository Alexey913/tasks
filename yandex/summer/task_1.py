def check_nick(data: str) -> bool:
    return any(map(str.isdigit, data)) and\
           any(map(str.islower, data)) and\
           any(map(str.istitle, data))

nick = input()
if check_nick(nick) and len(nick) >= 8:
    print('YES')
else:
    print('NO')