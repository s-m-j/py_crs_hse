def IsPointInCircle(x, y, xc=-1, yc=1, r=2):
    c = (xc - x) ** 2 + (yc - y) ** 2
    return(c <= r ** 2)


def IsPointNotInCircle(x, y, xc=-1, yc=1, r=2):
    c = ((xc - x) ** 2) + ((yc - y) ** 2) * (1 / 2)
    return(c >= r)


def IsAboveOne(x, Y):
    return(y >= 2 * x + 2)


def IsBelovOne(x, Y):
    return(y <= 2 * x + 2)


def IsAboveTwo(x, Y):
    return(y >= -x)


def IsBelovTwo(x, Y):
    return(y <= -x)


x = float(input())
y = float(input())


if IsPointInCircle(x, y) and IsAboveOne(x, y) and IsAboveTwo(x, y):
    print('YES')
elif IsPointNotInCircle(x, y) and IsBelovOne(x, y) and IsBelovTwo(x, y):
    print('YES')
else:
    print('NO')
