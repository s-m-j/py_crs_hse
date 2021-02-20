flg = 0


def rec():
    global flg
    n = int(input())
    if n != 0:
        rec()
        if round(n ** (1 / 2)) ** 2 == n:
            print(n, end=' ')
            flg += 1


rec()
if flg == 0:
    print(flg)
