from collections import defaultdict

word_1 = input()
word_2 = input()

chars = defaultdict(int)
for i in word_1:
    chars[i] += 1

for i in word_2:
    if not i in chars or chars[i] == 0:
        print('NO')
        break
    else:
        chars[i] -= 1
else:
    print('YES')