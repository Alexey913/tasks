from collections import defaultdict


dictionary = input().split()
words = input().split()
result = {}

for word in words:
    for d in dictionary:
        if word.startswith(d) and len(result.setdefault(word, d)) > len(d):
            result[word] = d
    print(result.setdefault(word, word), end =' ')