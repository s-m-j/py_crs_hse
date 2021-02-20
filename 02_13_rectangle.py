a0 = int(input())
b0 = int(input())
c0 = int(input())

a = max(a0, b0, c0)
c = min(a0, b0, c0)
b = a0 + b0 + c0 - a - c

if (b + c) <= a:
    print('impossible')
else:
    if (a ** 2 == (b ** 2 + c ** 2)):
        print('rectangular')
    else:
        if (a ** 2 > (b ** 2 + c ** 2)):
            print('obtuse')
        else:
            print('acute')
