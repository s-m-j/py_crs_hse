def phib(n):
    if n <= 2:
        return 1
    else:
        return phib(n - 1) + phib(n - 2)


print(phib(int(input())))
