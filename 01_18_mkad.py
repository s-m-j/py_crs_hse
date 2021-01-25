v = int(input())
t = int(input())

n = (109 + (v * t % 109)) % 109
print(n)
