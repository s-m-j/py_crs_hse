def distance(x1, y1, x2, y2):
    return((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)


def perimeter(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x1, y1, x3, y3)
    return(a + b + c)


x = perimeter(int(input()), int(input()),
              int(input()), int(input()), int(input()), int(input()))
print('{0:.6f}'.format(x))
