def lagr(n, level):
    if level == 0:
        return "NO"
    sqrtn = int(n ** 0.5)
    if sqrtn * sqrtn == n:
        return str(sqrtn)
    while sqrtn > 0:
        if lagr(n - sqrtn * sqrtn, level - 1) != "NO":
            return str(sqrtn) + " " + lagr(n - sqrtn * sqrtn, level - 1)
        sqrtn -= 1
    return "NO"


n = int(input())
print(lagr(n, 4))
