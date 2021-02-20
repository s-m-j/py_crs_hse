a1 = int(input())
b1 = int(input())
c1 = int(input())

a2 = int(input())
b2 = int(input())
c2 = int(input())

a1n = max(a1, b1, c1)
c1n = min(a1, b1, c1)
b1n = (a1 + b1 + c1) - a1n - c1n

a2n = max(a2, b2, c2)
c2n = min(a2, b2, c2)
b2n = (a2 + b2 + c2) - a2n - c2n

if (a1n == a2n) and (b1n == b2n) and (c1n == c2n):
    print('Boxes are equal')
else:
    if (a1n <= a2n) and (b1n <= b2n) and (c1n <= c2n):
        print('The first box is smaller than the second one')
    else:
        if (a1n >= a2n) and (b1n >= b2n) and (c1n >= c2n):
            print('The first box is larger than the second one')
        else:
            print('Boxes are incomparable')
