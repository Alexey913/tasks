# F. Велодорожки
# https://contest.yandex.ru/contest/59542/problems/F/

# Мэр одного города очень любит следить за тенденциями и
# воспроизводить их в своём городе. До него дошла новость о
# популярности велодорожек. Теперь он хочет проложить
# велодорожки в своём городе и сделать это лучше, чем в других
# городах! Поэтому он решил сделать велодорожки даже на 
# лавной площади города.
# Главная площадь представляет собой прямоугольник шириной w
# и высотой h, замощённый квадратными плитками со стороной 1.
# Мэр хочет, чтобы было проложено две велодорожки одинаковой
# ширины: одна горизонтальная и одна вертикальная.
# К сожалению, ремонт на площади проводился достаточно давно
# и на некоторых плитках уже появились трещины. Мэр хочет
# проложить велодорожки так, чтобы после этого на площади
# остались только целые плитки. При строительстве велодорожек
# плитки на их месте убираются. Можно только убирать плитки
# с площади и нельзя менять местами или добавлять новые.
# Чтобы потратить меньше денег, мэр хочет сделать велодорожки
# наименьшей возможной ширины, при этом ширина дорожек должна
# быть целым числом. Определите, какой должна быть ширина
# велодорожек.


w, h, n = map(int, input().split())
xx = []
yy = []
coord = []
for _ in range(n):
    x, y = map(int, input().split())
    coord.append([x, y])
    xx.append(x)
    yy.append(y)

coord_x = sorted(coord, key=lambda x: x[0])
coord_y = sorted(coord, key=lambda y: y[1])
xx.sort()
yy.sort()
print(xx)
print(yy)
print(coord_x)
print(coord_y)

