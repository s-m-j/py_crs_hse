# максимальное число идущих подряд равных
n = int(input())

cnt = 1
cnt_max = 1
cur = -1

while n != 0:
    if cur == n:
        cnt += 1
    else:
        cur = n
        cnt = 1
    if cnt > cnt_max:
        cnt_max = cnt
    n = int(input())
print(cnt_max)
