# количество палиндромов
n = int(input())
i = 1
cnt = 0
cur = 0

while i <= n:
    s0 = str(i)
    s = ''
    cur = i
    while cur != 0:
        a = cur // 10
        b = cur % 10
        s = s + str(b)
        cur = a
    if s0 == s:
        cnt += 1
    i += 1
print(cnt)
