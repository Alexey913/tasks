quan = int(input())
input_list = []
for i in range(quan):
    input_list.append(input())
for empl in input_list:
    temp_list = empl.split(',')
    first = len(set("".join(temp_list[:3])))
    second_temp = "".join(temp_list[-3:-1])
    second = sum(int(i) for i in second_temp)
    third = ord(temp_list[0][0].lower()) - ord('a') + 1
    code = hex(first + second * 64 + third * 256)[2:].title()
    if len(code) < 3:
        code = (3 - len(code)) * '0' + code
    else:
        code = code[-3:]
    print(code, end=" ")