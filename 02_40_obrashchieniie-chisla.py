# обращение числа
n = int(input())
# a = 1
s = ''

while n != 0:
    a = n // 10
    b = n % 10
    s = s + str(b)
    n = a
print(s)
