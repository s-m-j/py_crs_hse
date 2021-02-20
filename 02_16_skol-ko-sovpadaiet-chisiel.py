a = int(input())
b = int(input())
c = int(input())

n = 0

if a == b:
    n = n + 1
if a == c:
    n = n + 1
if b == c:
    n = n + 1
print(min(n * 2, 3))
