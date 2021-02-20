now = int(input())

i = 0
cnt = 0

while now != 0:
    i += 1
    if now % 2 == 0:
        cnt += 1
    now = int(input())
print(cnt)
