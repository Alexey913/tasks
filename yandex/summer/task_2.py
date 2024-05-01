move_cur = ['<left>', '<right>', '<bspace>', '<delete>']

a = input()
b = input()
list_input = []
flag_command = False
temp = ''
for i in b:
    if i == '<':
        list_input.append(temp)
        temp = '<'
    elif i == '>':
        temp += i
        list_input.append(temp)
        temp = ''
    else:
        temp += i
if b[-1] != '>':
    list_input.append(temp)

cur_pos = 0
result = ''
for c in list_input:
    if not c in move_cur and c:
        result = result[:cur_pos] + c + result[cur_pos:]
        if len(c) == 1:
            cur_pos += 1
        else:
            cur_pos += len(c) - 1
    elif c == '<left>' and cur_pos != 0:
        cur_pos -= 1
    elif c == '<right>' and cur_pos != len(result) - 1:
        cur_pos += 1
    elif c == '<delete>' and cur_pos != len(result):
        result = result[:cur_pos] + result[cur_pos + 1:]
    elif c == '<bspace>' and cur_pos != 0:
        result = result[:cur_pos] + result[cur_pos + 1:]
if result == a:
    print('Yes')
else:
    print('No')
