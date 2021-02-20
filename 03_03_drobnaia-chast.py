"""
Дробная часть вещественного ПОЛОЖИТЕЛЬНОГО числа
"""
from math import floor

f = float(input())

print('{0:g}'.format(f - floor(f)))
