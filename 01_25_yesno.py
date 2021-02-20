a = int(input())
b = int(input())

n = 0 ** (a % b)

print('YES' * n, 'NO' * abs(n - 1), sep='')
