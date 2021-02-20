n = int(input())

ost = n % 10

if (ost == 1) and (n != 11):
    print(n, 'korova')
else:
    if (n > 10) and (n < 20):
        print(n, 'korov')
    else:
        if (ost > 1) and (ost < 5):
            print(n, 'korovy')
        else:
            print(n, 'korov')
