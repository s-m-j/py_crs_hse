# Первая упаковка
l1, w1, h1 = int(input()), int(input()), int(input())
# Вторая упаковка
l2, w2, h2 = int(input()), int(input()), int(input())
# Контейнер
lc, wc, hc = int(input()), int(input()), int(input())

# Если коробки одна на другой (по высоте помещаются) то нужно проверить
# что каждая помещается или динна в длинну илибо ширина в длинну
if (h1 + h2 <= hc) \
        and ((l1 <= lc and w1 <= wc) or (l1 <= wc and w1 <= lc)) \
        and ((l2 <= lc and w2 <= wc) or (l2 <= wc and w2 <= lc)):
    print('YES')
# Иначе проверим что контейнеры по одному помещаются по высоте
elif max(h1, h2) <= hc and \
        ((l1 + l2 <= wc and max(w1, w2) <= lc) or
         (w1 + w2 <= wc and max(l1, l2) <= lc) or
         (l1 + w1 <= wc and max(l2, w2) <= lc) or
         (l1 + w2 <= wc and max(l2, w1) <= lc) or
         (l2 + w2 <= wc and max(l1, w1) <= lc) or
         (l2 + w1 <= wc and max(l1, w2) <= lc) or
         # И наоборот по одной вдоль контейнера и по две поперек:
         (l1 + l2 <= lc and max(w1, w2) <= wc) or
         (l1 + w1 <= lc and max(l2, w2) <= wc) or
         (l1 + w2 <= lc and max(l2, w1) <= wc) or
         (l2 + w2 <= lc and max(l1, w1) <= wc) or
         (l2 + w1 <= lc and max(l1, w2) <= wc) or
         (w1 + w2 <= lc and max(l1, l2) <= wc)):
        print('YES')
else:
    print('NO')
