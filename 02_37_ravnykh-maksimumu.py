now = int(input())
mx = now

i = 0
cnt = 0

while now != 0:
    i += 1
    if now == mx:
        cnt += 1
    else:
        if now > mx:
            mx = now
            cnt = 1
    now = int(input())
print(cnt)
