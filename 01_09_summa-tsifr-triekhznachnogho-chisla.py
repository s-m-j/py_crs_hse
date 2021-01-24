n = int(input())
a = n // 100
b = (n - a * 100) // 10
c = (n - a * 100) % 10
print(a + b + c)
