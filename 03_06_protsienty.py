"""
Проценты

"""
p, x, y = int(input()), int(input()), int(input())

# Сумма в копейках
a = int((100 + p) * (x * 100 + y) / 100)

print(int(a * 0.01), int(a % 100), sep=' ')
