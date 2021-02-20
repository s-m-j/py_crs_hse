n = int(input())
sc = n % 60
mn = (n // 60) % 60
hr = (n // 3600) % 24
print(
      str(hr),
      str(mn // 10) + str(mn % 10),
      str(sc // 10) + str(sc % 10),
      sep=':')
