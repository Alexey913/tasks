from itertools import zip_longest

def find_line(line, report, max_word):
    if max_word > line:
        len_roll = float('inf')
    else:
        width = 1
        len_roll = 0
        for i in report:
            if width + i < line:
                width += i + 1
            elif width + i == line:
                width = 0
                len_roll += 1
            elif width + i > line:
                width = i
                len_roll += 1
    return len_roll



def search_length_paper(part_1:list, part_2:list, w: int):
    max_a = max(map(len, part_1))
    max_b = max(map(len, part_2))
    current_max = max(len(part_1), len(part_2))
    start = max_a
    end = w - max_b
    while start <= end:
        mid = (start + end) // 2
        len_a = find_line(mid, part_1, max_a)
        len_b = find_line(w - mid, part_2, max_b)

        if len_a < len_b:
            end = mid
            if len_b < current_max:
                current_max = len_b
        elif len_a > len_b:
            start = mid + 1
            if len_a < current_max:
                current_max = len_a
        else:
            return current_max
    return current_max
            
            



w, n, m = map(int, input().split())
a = input().split()
b = input().split()
print(search_length_paper(a, b, w))
