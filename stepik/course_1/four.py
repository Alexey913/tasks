import requests

with open('stepik\course_1\dataset_3378_3.txt', 'r') as f:
    new_adress = in_file = f.readline().strip()
    adress = '/'.join(new_adress.split('/')[:-1])
while not in_file.startswith('We'):
    in_file = requests.get(new_adress).text.strip()
    new_adress = adress + '/' + in_file
    print(in_file)
with open('stepik\course_1\datares_3378_3.txt', 'w', encoding='utf-8') as w:
    w.write(in_file)