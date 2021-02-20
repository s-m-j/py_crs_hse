n = int(input())

i = 1
p = 1
s = '1'

while (p * 2 <= n):
    p = p * 2
    s = s + ' ' + str(p)
    i = i + 1
print(s)
