import requests

with open('stepik\course_1\dataset_3378_2.txt', 'r') as f:
    url = f.readline().strip()

r = requests.get(url)
print(len(r.text.splitlines()))