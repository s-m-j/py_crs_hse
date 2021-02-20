"""
Деление цены в рублях и копейках на целое число рублей и копеек
"""
from math import floor

f = float(input())

print(int(floor(f)), int(round(f - floor(f), 2) * 100), sep=' ')
