# C. Петя, Маша и верёвочки
# https://contest.yandex.ru/contest/59540/problems/C/

# На столе лежали две одинаковые верёвочки целой положительной
# длины.
# Петя разрезал одну из верёвочек на N частей, каждая
# из которых имеет целую положительную длину, так что
# на столе стало N+1 верёвочек. Затем в комнату зашла Маша
# и взяла одну из лежащих на столе верёвочек.
# По длинам оставшихся на столе N верёвочек определите,
# какую наименьшую длину может иметь верёвочка, взятая Машей.


n = int, input()
ropes = list(map(int, input().split()))
max_len = max(ropes)
sum_ropes = sum(ropes) - max_len
if sum_ropes < max_len:
    print(max_len - sum_ropes)
elif sum_ropes > max_len:
    print(sum_ropes + max_len)
else:
    print(max_len * 2)