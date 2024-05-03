with (
    open('dataset_3363_4.txt', 'r', encoding='utf-8') as f_r,
    open('datares_3363_4.txt', 'w', encoding='utf-8') as f_w
):
    input_data = {}
    for line in f_r:
        l = line.split(';')
        input_data[l[0]] = [int(l[1]), int(l[2]), int(l[3])]
    mat = phy = rus = 0
    for v in input_data.values():
        f_w.write(str((v[0] + v[1] + v[2]) / 3) + '\n')
        mat += v[0]
        phy += v[1]
        rus += v[2]
    f_w.write(f'{mat / len(input_data)} {phy / len(input_data)} {rus / len(input_data)}')