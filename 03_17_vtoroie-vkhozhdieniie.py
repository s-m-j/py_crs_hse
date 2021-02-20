s = input()
i1 = s.find('f')
if i1 == -1:
    print(-2)
else:
    print(s.find('f', i1 + 1))
