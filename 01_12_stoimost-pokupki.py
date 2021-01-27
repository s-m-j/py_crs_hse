a = int(input())  # стоимость пирожка рубли
b = int(input())  # стоимость пирожка копейки
n = int(input())  # сколько пирожков

total_cost = (a * 100 + b) * n
r = total_cost // 100
k = total_cost % 100
print(r, k)
