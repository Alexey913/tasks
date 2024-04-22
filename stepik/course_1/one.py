with (
    open('dataset_3363_2.txt', 'r', encoding='utf-8') as f_r,
    open('datares_3363_2.txt', 'w', encoding='utf-8') as f_w
):
    line = f_r.readline().strip()
    temp_s = ''
    temp_d = 0
    for s in line:
        if s.isalpha():
            f_w.write(temp_s * int(temp_d))
            temp_s = s
            temp_d = ''
        if s.isdigit():
            temp_d += s
    f_w.write(temp_s * int(temp_d))
