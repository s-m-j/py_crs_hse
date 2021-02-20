now = int(input())
prev = now

i = 0
cnt = 0

while now != 0:
    i += 1
    if now > prev:
        cnt += 1
    prev = now
    now = int(input())
print(cnt)
