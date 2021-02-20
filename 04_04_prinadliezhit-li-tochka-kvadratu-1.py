def IsPointInSquare(x, y):
    return((x >= -1) and (x <= 1) and (y >= -1) and (y <= 1))

if IsPointInSquare(float(input()), float(input())):
    print('YES')
else:
    print('NO')
