s = input()
s2 = s.replace('h', 'H', s.count('h') - 1)
print(s2.replace('H', 'h', 1))
