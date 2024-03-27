# def find_width_road(nums: list) -> int:



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

