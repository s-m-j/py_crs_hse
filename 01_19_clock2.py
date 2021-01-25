n = int(input())
sc = n % 60
mn = (n // 60) % 24
hr = (n // 3600) % 24
print(str(hr // 10) + str(hr % 10), str(mn // 10) + str(mn % 10),
str(sc // 10) + str(sc % 10))
