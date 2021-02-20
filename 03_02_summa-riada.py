"""
по введенному N посчитать сумму ряда
(1 / 1²)+(1 / 2²)+(1 / 3²)+...+(1 / n²)
"""
n = int(input())
s = 0

while n > 0:
    s = s + (1 / (n ** 2))
    n = n - 1

print('{0:.6f}'.format(s))
