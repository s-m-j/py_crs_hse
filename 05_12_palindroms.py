a, b = int(input()), int(input())

for i in range(a, b + 1):
    s = str(i)
    if s == s[::-1]:
        print(i)
