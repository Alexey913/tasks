# a = float(input())
# b = float(input())
# match input():
#     case '+':
#         print(a + b)
#     case '-':
#         print(a - b)
#     case '*':
#         print(a * b)
#     case '/':
#         if b == 0:
#             print("Деление на 0!")
#         else:
#             print(a / b)
#     case 'mod':
#         if b == 0:
#             print("Деление на 0!")
#         else:
#             print(a % b)
#     case 'div':
#         if b == 0:
#             print("Деление на 0!")
#         else:
#             print(a // b)
#     case 'pow':
#         print(a ** b)


# ------------------------------

# shape = input()
# a = int(input())
# if shape == 'прямоугольник':
#     b = int(input())
#     s = a * b
# if shape == 'круг':
#     s = 3.14 * a * a
# if shape == 'треугольник':
#     b = int(input())
#     c = int(input())
#     p = (a + b + c) / 2
#     s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(s)

# ------------------------------

# s = input()
# print((s.lower().count('c') + s.lower().count('g')) / len(s) * 100)

# ------------------------------

# s = [int(i) for i in input().split()]
# result = []
# if len(s) <= 1:
#     result = s
# else:
#     result = [s[-1] + s[1]]
#     for i in range(1, len(s) - 1):
#         result.append(s[i-1] + s[i+1])
#     result.append(s[0] + s[-2])
# print(*result)

# ---------------------------------

s = [int(i) for i in input().split()]
result = []
for i in s:
    if s.count(i) > 1 and not i in result:
        result.append(i)
print(*result)

