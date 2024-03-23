# dictionary = input().split()
# words = input().split()
# result = {}

# for word in words:
#     for d in dictionary:
#         if word.startswith(d) and len(result.setdefault(word, d)) > len(d):
#             result[word] = d
#     print(result.setdefault(word, word), end =' ')


# from collections import defaultdict


# dictionary = input().split()
# words = input().split()
# result = defaultdict(list)

# for i in dictionary:
#     result[i[0]].append(i)

# for word in words:
#     if word[0] in result:
#         for i in result[word[0]]:
#             if word.startswith(i) and len(i) < len(word):
#                 word = i
#     print(word, end = ' ') 


# from collections import defaultdict


# dictionary = set(input().split())
# words = input().split()
# result = defaultdict(list)

# for i in dictionary:
#     result[i[0]].append(i)

# for word in words:
#     if word[0] in result:
#         for i in range(1, min(101, len(word))):
#             if word[:i] in result[word[0]]:
#                 word = word[:i]
#                 break
#     print(word, end = ' ')


dictionary = set(input().split())
words = input().split()
result = []


for word in words:
    for i in range(1, min(101, len(word))):
        if word[:i] in dictionary:
            result.append(word[:i])
            break
    else:
        result.append(word)
print(*result)