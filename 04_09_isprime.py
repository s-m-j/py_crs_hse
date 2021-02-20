def IsPrime(n):
    i = 2
    while i <= n ** (1 / 2):
        if n % i == 0:
            return 'NO'
        i += 1
    return 'YES'


print(IsPrime(int(input())))
