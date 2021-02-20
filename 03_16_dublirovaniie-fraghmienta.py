s = input()
i1 = s.find('h')
s1 = s[:i1 + 1]

i2 = len(s) - 1 - s[::-1].find('h')
s3 = s[i2:]

s2 = s[i1 + 1:i2:]
s2 *= 2

print(s1 + s2 + s3)
