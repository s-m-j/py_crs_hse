a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())

n1 = (a1 % 2) == (a2 % 2)
n2 = (b1 % 2) == (b2 % 2)

if n1 == n2:
    print('YES')
else:
    print('NO')
