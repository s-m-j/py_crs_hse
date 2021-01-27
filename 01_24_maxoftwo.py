"""
максимальное из 2 чисел
"""
a = int(input())
b = int(input())

print(a + b - (a + b - abs(a - b))//2)
