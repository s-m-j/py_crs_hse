x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

b1 = x1 > 0
b2 = x2 > 0
b3 = y1 > 0
b4 = y2 > 0

a = (b1 and b2) or (not(b1) and not(b2))
b = (b3 and b4) or (not(b3) and not(b4))

if a and b:
    print('YES')
else:
    print('NO')
