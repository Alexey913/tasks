x = int(input())
y = int(input())
p = int(input())

if x >= y:
    total = 1
elif 2 * y <= x:
    total = 2
else:
    my_sold = x
    health_bar = y
    enemy = 0
    total = 0
    while health_bar > 0 or enemy > 0:
        if enemy == 0:
            health_bar -= my_sold
        elif health_bar == 0:
            enemy 
print(total)