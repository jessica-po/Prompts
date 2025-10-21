import math

n = int(input())
xy = [list(map(float, input().split())) for _ in range(n)]

ret = 100000000
def update(px, py):
    nonlocal ret
    r = 0
    for p in range(n):
        r = max(r, math.hypot(px - xy[p][0], py - xy[p][1]))
    ret = min(ret, r)

for i in range(n):
    x1 = xy[i][0]
    y1 = xy[i][1]
    for j in range(i + 1, n):
        x2 = xy[j][0]
        y2 = xy[j][1]
        update((x1 + x2) / 2, (y1 + y2) / 2)
        for k in range(j + 1, n):
            x3 = xy[k][0]
            y3 = xy[k][1]

            d = 2 * (y1 - y3) * (x1 - x2) - 2 * (y1 - y2) * (x1 - x3)
            if d != 0:
                px = ((y1 - y3) * (y1 ** 2 - y2 ** 2 + x1 ** 2 - x2 ** 2) - (y1 - y2) * (y1 ** 2 - y3 ** 2 + x1 ** 2 - x3 ** 2)) / d
                py = ((x1 - x3) * (x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2) - (x1 - x2) * (x1 ** 2 - x3 ** 2 + y1 ** 2 - y3 ** 2)) / -d
                update(px, py)

print(ret)