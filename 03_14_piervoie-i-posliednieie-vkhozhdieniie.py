s = input()
i1 = s.find('f')
i2 = s.rfind('f')
if i1 != -1:
    if i1 == i2:
        print(i1)
    else:
        print(str(i1), str(i2))
