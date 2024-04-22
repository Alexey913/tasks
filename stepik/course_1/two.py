with open('dataset_3363_3.txt', 'r', encoding='utf-8') as f_r:
    input_data = []
    for line in f_r:
        input_data += line.split()
    print(input_data)
    max_repeat_word = ''
    count_repeat = 0
    for i in set(input_data):
        repeat = input_data.count(i)
        if repeat > count_repeat or repeat == count_repeat and i < max_repeat_word:
            max_repeat_word = i
            count_repeat = repeat
print(max_repeat_word, count_repeat)