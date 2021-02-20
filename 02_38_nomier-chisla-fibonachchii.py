# Числа Фиббоначчи
n = int(input())
fp = 0
fn = 1

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    i = 2
    while fn <= n:
        fp, fn = (fn, fp + fn)
        if fn == n:
            print(i)
            break
        i += 1
    else:
        print(-1)
