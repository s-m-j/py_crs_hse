"""
Схема Горнера

"""
n = int(input())
x = float(input())
i = 0
# ap = float(input())
p = 0.0
# p = ap * x
while i < n:
    an = float(input())
    # p = p + (an * x + ap) * x
    # p = (p * x + ap) * x
    p = (p + an) * x
    i += 1
p = p + float(input())

print('{0:.6f}'.format(p))
