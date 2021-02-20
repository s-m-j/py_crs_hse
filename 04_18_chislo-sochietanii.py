def c(n, k):
    if k == 0:
        return 1
    if k == 1:
        return n
    if n == k:
        return 1
    return c(n - 1, k) + c(n - 1, k - 1)


print(c(int(input()), int(input())))
