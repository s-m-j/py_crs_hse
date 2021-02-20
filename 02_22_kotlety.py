k, m, n = (int(input()), int(input()), int(input()))

if k > n:
    print(2 * m)
else:
    if n % k == 0:
        print((n * 2 // k) * m)
    else:
        # print(2 * m * (n // k) + 1)
        # print(((n * 2 // k) + 1) * m)
        n = n * 2
        y1 = n // k
        y2 = n % k
        if y2 != 0:
            y2 = 1
        print((y1 + y2) * m)
