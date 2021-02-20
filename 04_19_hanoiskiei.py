def htower(n, s, f):
    if n == 1:
        print(n, s, f)
    else:
        tmp = 6 - s - f
        htower(n - 1, s, tmp)
        print(n, s, f)
        htower(n - 1, tmp, f)

htower(int(input()), 1, 3)
