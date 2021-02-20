a1 = int(input())
b1 = int(input())
c1 = int(input())

a2 = int(input())
b2 = int(input())
c2 = int(input())

x1 = (a1 // a2) * (b1 // b2) * (c1 // c2)
x2 = (a1 // b2) * (b1 // a2) * (c1 // c2)
x3 = (a1 // c2) * (b1 // b2) * (c1 // a2)
x4 = (a1 // c2) * (b1 // a2) * (c1 // b2)
x5 = (a1 // a2) * (b1 // c2) * (c1 // b2)
x6 = (a1 // b2) * (b1 // c2) * (c1 // a2)

print(max(x1, x2, x3, x4, x5, x6))
