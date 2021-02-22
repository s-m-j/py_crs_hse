for i in range(10, 100):
    a = i // 10
    b = i % 10
    if 2 * a * b == i:
        print(i, end=' ')
