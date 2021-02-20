def power(a, n):
    if n == 0:
        return 1
    if a == 0:
        return 0
    i = abs(n) - 1
    while i > 0:
        a *= x
        i -= 1
    if n < 0:
        return 1/a
    else:
        return a


x, s = float(input()), int(input())
print(power(x, s))
