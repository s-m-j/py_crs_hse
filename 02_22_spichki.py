l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())

nr1 = 1
nr2 = 2
nr3 = 3

if l2 < l1:
    (l1, l2) = (l2, l1)
    (r1, r2) = (r2, r1)
    (nr1, nr2) = (nr2, nr1)
if l3 < l2:
    (l2, l3) = (l3, l2)
    (r2, r3) = (r3, r2)
    (nr2, nr3) = (nr3, nr2)
if l2 < l1:
    (l1, l2) = (l2, l1)
    (r1, r2) = (r2, r1)
    (nr1, nr2) = (nr2, nr1)
# длины спичек
d1 = r1 - l1
d2 = r2 - l2
d3 = r3 - l3
# промежутки
c1 = l2 - r1
c2 = l3 - r2
# пересекаются
if (l2 <= r1 and l3 <= r2) or r1 >= l3:
    print(0)
# не хватает длинны
elif d1 < c2 and d3 < c1:
    print(-1)
elif (nr1 < nr3 and d1 >= c2 > 0) or (nr1 < nr3 and c2 <= 0 and c1 > 0):
    print(nr1)
elif d3 >= c1 > 0:
    print(nr3)
elif (nr3 < nr1 and d3 >= c1 > 0) or (nr3 < nr1 and c1 <= 0 and c2 > 0):
    print(nr3)
elif (d1 >= c2 > 0) or (c2 <= 0 and d1 >= c1 > 0):
    print(nr1)
