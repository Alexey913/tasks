def find_limits(start_line):
    if start_line[0] == '#':
            cut_point_1 = 0
    if start_line[-1] == '#':
        cut_point_2 = n - 1
    for j in range(1, len(start_line)):
        if start_line[j] == '#' and start_line[j-1] == '.':
            cut_point_1 = j
        if start_line[j] == '.' and start_line[j-1] == '#':
            cut_point_2 = j - 1
    return cut_point_1, cut_point_2

def find_cut_point(start_line):
    for j in range(len(start_line)):
        # print(f'{start_line[j]=}')
        if start_line[j] == '#' and start_line[j+1] == '.':
            cut_point = j + 1
            break
    return cut_point

m, n = map(int, input().split())
elements = []
start_1_1 = start_1_2 = -1
start_2_1 = start_2_2 = -1
end_1_1 = end_1_2 = 0
ende_2_1 = end_2_2 = 0
count_weigth = count_heigth = 0
answer = 'YES'
start = -1
cut_point = -1
cut_point_1 = -1
cut_point_2 = -1
for i in range(m):
    line = input()
    if list(filter(str.strip, line.split('.'))) and start == -1:
        start = i
    elements.append(line)
# print(f'{start=}')
if start == -1:
    answer = 'NO'
elif m == 1 and n == 1:
        answer = 'NO'
else:
    start_line = elements[start]
    count_figures = len(list(filter(str.strip, start_line.split('.'))))
    # print(f'{count_figures=}')
    if count_figures > 2:
        answer = 'NO'
    elif count_figures == 2:
        cut_point = find_cut_point(start_line)
        # print(f'{cut_point=}')
        stop_lines = 0
        for i in range(start, len(elements)):
            # print(f'{i}----------------')
            # print(f'{elements[i]}')
            # print(f'{start_line=}')
            # print(f'{stop_lines=}')
            # print(f'{elements[i][:cut_point]==start_line[:cut_point]=}')
            # print(f'{elements[i][cut_point:]=}')
            if elements[i] != start_line:
                stop_lines += 1
                if stop_lines < 2:
                    if not '#' in elements[i]:
                        start_line = elements[i]
                        # print(f'{elements[i]=} .....')
                        # print(f'{start_line=}')
                    elif elements[i][:cut_point] == start_line[:cut_point] and not '#' in elements[i][cut_point:]:
                        start_line = elements[i][:cut_point] + '.' * len(start_line[cut_point:])

                        # print(f'{elements[i]=} 2 half')
                        # print(f'{start_line=}')
                    elif elements[i][cut_point:] == start_line[cut_point:] and not '#' in elements[i][:cut_point]:
                        start_line = '.' * len(start_line[:cut_point]) + elements[i][cut_point:]
                        # print(f'{elements[i]=} 1 half')
                        # print(f'{start_line=}')
                        
                elif stop_lines >= 2:
                    answer = 'NO'
                    # print(answer)
                    break
            elements[i] = elements[i][:cut_point].replace('#', 'a') + elements[i][cut_point:].replace('#', 'b')
    
    
    
    elif count_figures == 1:
        cut_point_1, cut_point_2 = find_limits(start_line)
        # print(f'{cut_point_1=}')
        # print(f'{cut_point_2=}')
        stop_lines = 0
        for i in range(start, len(elements)):
            # print(f'{i}----------------')
            # print(f'{elements[i]}')
            # print(f'{start_line=}')
            # print(f'{stop_lines=}')
            # print(f'{elements[i][:cut_point]==start_line[:cut_point]=}')
            # print(f'{elements[i][cut_point:]=}')
            if elements[i] != start_line:
                stop_lines += 1
                if stop_lines == 3:
                    answer = 'NO'
                    break
                elif stop_lines == 2:
                    if elements[i] != '.' * n:
                        answer = 'NO'
                        break
                    else:
                        start_line = elements[i]
                else:
                    new_len = len(list(filter(str.strip, elements[i].split('.'))))
                    if new_len == 2:
                        cut_point = find_cut_point(start_line)
                        if stop_lines != 2:
                            if elements[i][:cut_point] == start_line[:cut_point] and not '#' in start_line[cut_point:]:
                                start_line = elements[i]
                                # print(f'{elements[i]=} 2 half')
                                # print(f'{start_line=}')
                            elif elements[i][cut_point:] == start_line[cut_point:] and not '#' in start_line[:cut_point]:
                                start_line = elements[i]
                                # print(f'{elements[i]=} 1 half')
                                # print(f'{start_line=}')
                        else:
                            answer = 'NO'
                            # print(answer)
                            break
                    elif new_len == 1:
                        cur_start, cur_end = find_limits(elements[i])
                        # if cur_start == cut_point_1 or cur_end == cut_point_2:                
            elements[i] = elements[i].replace('#', 'b')
print(answer)
for i in elements:
    print(i)