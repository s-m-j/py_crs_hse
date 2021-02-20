import math
a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if d < 0:
    print(0)
elif d == 0:
    if a == b == c == 0:
        print(3)
    else:
        if a == 0:
            print(0)
        else:
            print(1, -b / (2 * a))
elif d > 0:
    if a == 0:
        print(1, -c / b)
    else:
        x1 = ((-b - math.sqrt(d)) / (2 * a))
        x2 = ((-b + math.sqrt(d)) / (2 * a))
        print(2, min(x1, x2), max(x1, x2))
