a = int(input())
b = int(input())
c = int(input())

dummy = a % 2 + b % 2

if dummy == 1:
    print('YES')
else:
    if ((dummy == 0) and (c % 2 == 1)) or ((dummy == 2) and (c % 2 == 0)):
        print('YES')
    else:
        print('NO')
