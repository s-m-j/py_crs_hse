"""
линейное уравнение:

(a * x + b)  = 0

При a = 0 и b = 0, уравнение имеет бесконечное множество корней
При a = 0 и b != 0, уравнение корней не имеет
При a != 0 и b - любое число, уравнение имеет единственный корень
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 0:
    if b == 0:
        print('INF')
    else:
        print('NO')
else:
    if c * (-b / a) + d != 0 and (int(-b / a) == -b / a):
        print(int(-b / a))
    else:
        print('NO')
