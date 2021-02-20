i = 0


def rec():
    global i
    n = int(input())
    if n != 0:
        i += n
        rec()
    else:
        print(i)


rec()
