"""
Возводить в степень можно гораздо быстрее, чем за n умножений!
Для этого нужно воспользоваться следующими рекуррентными соотношениями:
aⁿ = (a²)ⁿ/² при четном n, aⁿ=a⋅aⁿ⁻¹ при нечетном n.
"""


def pow(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b % 2 == 0:
        return pow((a * a), (b // 2))
    else:
        return a * pow(a, b - 1)


print(pow(float(input()), int(input())))
