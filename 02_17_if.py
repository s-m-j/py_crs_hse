a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if d > e:
    (d, e) = (e, d)

a1 = max(a, b, c)
c1 = min(a, b, c)
b1 = a + b + c - a1 - c1

if (d >= c1) and (e >= b1):
    print('YES')
else:
    print('NO')
