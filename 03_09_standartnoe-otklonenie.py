x = int(input())
n, s1, s2 = 0, 0, 0
while x != 0:
    s1 = s1 + x
    s2 = s2 + x ** 2
    n = n + 1
    x = int(input())
print(((s2 - s1 ** 2 / n) / (n - 1)) ** 0.5)
