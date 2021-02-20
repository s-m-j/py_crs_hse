# максимальное число идущих подряд равных
n = int(input())

cnt = 1
cnt_max = 1
sign = 1

while n != 0:
    prev = n
    n = int(input())
    if n > prev:
        if (sign == 1):
            cnt += 1
        else:
            sign = 1
            cnt = 2
    elif n == prev:
        sign = 0
        cnt = 1
    elif n == 0:
        sign = 0
    else:
        if (sign == -1):
            cnt += 1
        else:
            sign = -1
            cnt = 2
    if cnt > cnt_max:
        cnt_max = cnt
    # print('cnt=', cnt, ' cnt_max=', cnt_max, ' n=', n, ' sign=', sign)

print(cnt_max)
