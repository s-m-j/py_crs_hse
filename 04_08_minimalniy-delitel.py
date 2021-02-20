def MinDivisor(n):
    i = 2
    while i <= n ** (1 / 2):
        if n % i == 0:
            return i
        i += 1
    return n


print(MinDivisor(int(input())))
