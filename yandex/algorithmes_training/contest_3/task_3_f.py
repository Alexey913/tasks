from collections import defaultdict


dictionary = input().split()
words = {i: '' for i in input().split()}
result = defaultdict(str)

for word in words:
    for d in dictionary:
        if word.startswith(d) and len(d) < len(result[word]):
            result[word] = d
        else:
            result[word] = word
print(result)