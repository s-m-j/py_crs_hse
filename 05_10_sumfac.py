def fact(i):
    if i == 1:
        return 1
    return i * fact(i - 1)


n = int(input())
nn = 0

for i in range(1, n + 1):
    nn += fact(i)
print(nn)
