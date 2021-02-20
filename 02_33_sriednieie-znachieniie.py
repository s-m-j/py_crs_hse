now = int(input())

i = 0
sm = 0

while now != 0:
    i += 1
    sm += now
    now = int(input())
print(sm / i)
