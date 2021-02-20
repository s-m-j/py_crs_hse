"""
Проценты

"""
p, x, y, k = int(input()), int(input()), int(input()), int(input())

i = 0
while i < k:
    # Сумма в копейках
    a = int((100 + p) * (x * 100 + y) / 100)
    x = int(a * 0.01)
    y = int(a % 100)
    i += 1

print(int(a * 0.01), int(a % 100), sep=' ')
