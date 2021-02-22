n = int(input())

nn = 0
ss = n * (n + 1) // 2

for i in range(n - 1):
    nn += int(input())

print(ss - nn)
