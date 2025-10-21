n = int(input())
xs = list(map(int, input().split()))
vs = list(map(int, input().split()))

l = 0
r = max(xs) - min(xs) + 1
for i in range(50):
    m = (r + l) / 2
    lev = 0
    prav = 1000000000
    for j in range(n):
        prav = min(prav, xs[j] + vs[j] * m)
        lev = max(lev, xs[j] - vs[j] * m)
        if prav < lev:
            break
    if prav < lev:
        l = m
    else:
        r = m
print((l + r) / 2)