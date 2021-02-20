x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

n1 = (x1 % 2) == (y1 % 2)
n2 = (x2 % 2) == (y2 % 2)

if n1 == n2:
    if (y2 > y1) and ((y2 - y1) >= (x2 - x1)):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
