"""
площадь треугольника по 3 сторонам:

p - полупериметр, (ф + и + с) / 2

s  sqrt(p * (p-a) * (p - b) * (p - c))
"""
a = float(input())
b = float(input())
c = float(input())

p = (a + b + c) / 2

s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print('{0:.6f}'.format(s))
