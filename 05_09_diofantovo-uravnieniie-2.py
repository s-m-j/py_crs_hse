a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

nn = 0

for x in range(0, 1001):
    if x != e:
        # print((a * (x ** 3) + b * (x ** 2) + c * x + d)/(x - e))
        if (a * (x ** 3) + b * (x ** 2) + c * x + d)/(x - e) == 0:
            nn += 1

print(nn)
