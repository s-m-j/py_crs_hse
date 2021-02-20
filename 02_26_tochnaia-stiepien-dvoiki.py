n = int(input())

i = 1
p = 1

if n == 1:
    print('YES')
else:
    while (i <= n):
        p = p * 2
        if (p == n):
            print('YES')
            break
        i = i + 1
    else:
        print('NO')
