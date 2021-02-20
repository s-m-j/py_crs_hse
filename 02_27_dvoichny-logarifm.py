n = int(input())

i = 1
p = 1

while (p * 2 < n):
    p = p * 2
    i = i + 1
if (n == 1):
    print(0)
else:
    print(i)
