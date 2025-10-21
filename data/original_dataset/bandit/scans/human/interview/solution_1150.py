def f(x, y, a, b, n):
    return a + (x - a) * cos[n] - (y - b) * sin[n], b + (x - a) * sin[n] + (y - b) * cos[n]


def check(p):
    d = {}
    for i in range(len(p) - 1):
        for j in range(i + 1, len(p)):
            dist = (p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2
            d[dist] = d.get(dist, 0) + 1
    if len(d) != 2:
        return 0
    a, b = sorted(d)
    return 2 * a == b and d[a] == 4 and d[b] == 2


cos, sin, variants = [1, 0, -1, 0], [0, 1, 0, -1], [[x, y, z, a] for x in range(4) for y in range(4) for z in range(4) for a in range(4)]
for t in range(int(input())):
    moles, ans = [list(map(int, input().split())) for x in range(4)], 13
    for a in variants:
        if check([f(moles[i][0], moles[i][1], moles[i][2], moles[i][3], a[i]) for i in range(4)]):
            ans = min(ans, sum(a))
    print(ans if ans != 13 else -1)