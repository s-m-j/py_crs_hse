n = int(input())

s = '1'
i = 2
while i ** 2 <= n:
    s = s + ' ' + str(i ** 2)
    i = i + 1
print(s)
