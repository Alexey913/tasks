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
print(f'{start=}')
if start == -1:
    answer = 'NO'
elif m == 1 and n == 1:
        answer = 'NO'
else:
    start_line = elements[start]
    count_figures = len(list(filter(str.strip, start_line.split('.'))))
    print(f'{count_figures=}')
    if count_figures > 2:
        answer = 'NO'
    elif count_figures == 2:
        for j in range(len(start_line)):
            print(f'{start_line[j]=}')
            if start_line[j] == '#' and start_line[j+1] == '.':
                cut_point = j + 1
                break
        print(f'{cut_point=}')
        stop_lines = 0
        for i in range(start, len(elements)):
            print(f'{i}----------------')
            print(f'{elements[i]}')
            print(f'{start_line=}')
            print(f'{stop_lines=}')
            # print(f'{elements[i][:cut_point]==start_line[:cut_point]=}')
            # print(f'{elements[i][cut_point:]=}')
            if elements[i] != start_line:
                stop_lines += 1
                if stop_lines < 2:
                    if not '#' in elements[i]:
                        start_line = elements[i]
                        print(f'{elements[i]=} .....')
                        print(f'{start_line=}')
                    elif elements[i][:cut_point] == start_line[:cut_point] and not '#' in elements[i][cut_point:]:
                        start_line = elements[i][:cut_point] + '.' * len(start_line[cut_point:])

                        print(f'{elements[i]=} 2 half')
                        print(f'{start_line=}')
                    elif elements[i][cut_point:] == start_line[cut_point:] and not '#' in elements[i][:cut_point]:
                        start_line = '.' * len(start_line[:cut_point]) + elements[i][cut_point:]
                        print(f'{elements[i]=} 1 half')
                        print(f'{start_line=}')
                        
                elif stop_lines >= 2:
                    answer = 'NO'
                    print(answer)
                    break
            elements[i] = elements[i][:cut_point].replace('#', 'a') + elements[i][cut_point:].replace('#', 'b')
    
    
    
    elif count_figures == 1:
        if start_line[0] == '#':
            cut_point_1 = 0
        if start_line[-1] == '#':
            cut_point_2 = n - 1
        for j in range(1, len(start_line)):
            if start_line[j] == '#' and start_line[j-1] == '.':
                cut_point_1 = j
            if start_line[j] == '.' and start_line[j-1] == '#':
                cut_point_2 = j - 1
        print(f'{cut_point_1=}')
        print(f'{cut_point_2=}')
        stop_lines = 0
        for i in range(start, len(elements)):
            print(f'{i}----------------')
            print(f'{elements[i]}')
            print(f'{start_line=}')
            print(f'{stop_lines=}')
            # print(f'{elements[i][:cut_point]==start_line[:cut_point]=}')
            # print(f'{elements[i][cut_point:]=}')
            if elements[i] != start_line:
                stop_lines += 1
                if stop_lines < 2:
                    if not '#' in elements[i]:
                        start_line = elements[i]
                        print(f'{elements[i]=} .....')
                        print(f'{start_line=}')
                    elif elements[i][:cut_point] == start_line[:cut_point] and not '#' in elements[i][cut_point:]:
                        start_line = elements[i][:cut_point] + '.' * len(start_line[cut_point:])

                        print(f'{elements[i]=} 2 half')
                        print(f'{start_line=}')
                    elif elements[i][cut_point:] == start_line[cut_point:] and not '#' in elements[i][:cut_point]:
                        start_line = '.' * len(start_line[:cut_point]) + elements[i][cut_point:]
                        print(f'{elements[i]=} 1 half')
                        print(f'{start_line=}')
                        
                elif stop_lines >= 2:
                    answer = 'NO'
                    print(answer)
                    break
            elements[i] = elements[i][:cut_point].replace('#', 'a') + elements[i][cut_point:].replace('#', 'b')
print(elements)
                

                
            # if len(list(filter(str.strip, elements[i].split('.')))) > 2:
            #     answer = 'NO'
            #     break
            # if cut_lines == 0:
            #     if elements[i] == ['.' * len(elements[i])]:
            #         cut_lines += 1
            #     elif elements[i][:cut_point] == ['.' * len(elements[i][:cut_point])]:
            #         cut_lines += 1
            #         if elements[i][cut_point:] != start_line[cut_point:]:
            #             answer == 'NO'
            #             break
            #     elif elements[i][cut_point:] == ['.' * len(elements[i][cut_point:])]:
            #         st
            #         if elements[i][:cut_point] != start_line[:cut_point]:
            #             answer == 'NO'
            #             break
            # else:
            #     if elements[i] != 

            # elif
            # else:
            #     if elements[i][0] == '#':
            #         elements[i] = 'a' + elements[i][1:]
            #     if elements[i][-1] == '#':
            #         elements[i] = elements[i][0:-1] + 'b'
            #         insert_b = 0
            #     for j in range(1, len(elements[i])):
            #         if elements[i][j] == '#' and not insert_b:
            #             elements[i] = elements[i][:j] + 'a' + elements[i][j+1:]
            #         elif elements[i][j] == '.' and 'a' in elements[i][j]:
            #             insert_b = 1
            #         elif elements[i][j] == '#' and insert_b:
            #             elements[i] = elements[i][:j] + 'b' + elements[i][j+1:]
# print(f'{start_line=}')
# print(answer)
# print(elements)