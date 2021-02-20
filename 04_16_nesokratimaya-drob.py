def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def ReduceFraction(n, m):
    return n // gcd(n, m), m // gcd(n, m)


p = int(input())
q = int(input())

print(*ReduceFraction(p, q))
