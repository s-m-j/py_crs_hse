"""
Программа принимает целое число представимое не
более чем четырьмя знаками
и выводит 1 если его десятичная запись симметрична,
то есть число прочитанное в обратном порядке равно
ему же, или любое другое число в противном случае
"""
n = int(input())
l = n // 100
r = n % 100
# print(l)
# print(r)

print((l // 10 + 10 * (l % 10)) - r + 1)
