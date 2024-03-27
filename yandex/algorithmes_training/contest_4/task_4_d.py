from itertools import zip_longest

def find_line(line, report, max_word):
    if max_word > line:
        len_roll = max_word + 1
    else:
        width = 0
        len_roll = 1
        for i in range(len(report)):
            if width + report[i] < line:
                width += report[i] + 1
            elif width + report[i] == line:
                width = 0
                if i != len(report) - 1:
                    len_roll += 1
            elif width + report[i] > line:
                width = report[i] + 1
                len_roll += 1
            print(f'{i=}. {width=}')
            print(f'{len_roll=}')
        print(f'{line=}: {len_roll=}')
    return len_roll



def search_length_paper(part_1:list, part_2:list, w: int):
    max_a = max(part_1)
    max_b = max(part_2)
    current_max = max(len(part_1), len(part_2))
    start = max_a
    end = w - max_b
    # if w == 1:
    #     return max(current_max)
    while start <= end:
        # print(f'{start=} {end=}')
        mid = (start + end) // 2
        len_a = find_line(mid, part_1, max_a)
        len_b = find_line(w - mid, part_2, max_b)
        if start == end:
            return min(current_max, max(len_a, len_b))
        if len_a < len_b:
            end = mid
            if len_b < current_max:
                current_max = len_b
        elif len_a > len_b:
            start = mid + 1
            if len_a < current_max:
                current_max = len_a
        else:
            return min(current_max, len_a)
        # print(current_max)
    return current_max
            

w, n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(search_length_paper(a, b, w))
