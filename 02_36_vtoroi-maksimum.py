now = int(input())
mx = 0
mx2 = 0

i = 0
cnt = 0

while now != 0:
    i += 1
    if now >= mx:
        cnt += 1
        mx2 = mx
        mx = now
    else:
        if now > mx2:
            mx2 = now
    now = int(input())
print(mx2)
