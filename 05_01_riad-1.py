a = int(input())
b = int(input())

if a == b:
    print(a)
else:
    for i in range(a, b + 1):
        print(i, end=' ')
