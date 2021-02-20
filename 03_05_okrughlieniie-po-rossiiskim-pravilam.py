"""
Округление положительного по русским правилам
0.5 -> в большоую сторону
"""
from math import floor, ceil

f = float(input())

if f - floor(f) >= 0.5:
    print(int(ceil(f)))
else:
    print(int(floor(f)))
