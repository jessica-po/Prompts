import sys
from collections import Counter
from operator import itemgetter
from heapq import heappop, heappush

n, m, k = list(map(int, input().split()))
points = [list(map(int, line.split())) for line in sys.stdin]
pts_sorted_x = sorted(points)
pts_sorted_y = sorted(points, key=itemgetter(1, 0))
inf = 10**9+1
OK = (inf, inf)


def solve2(imos, t):
    acc, cur = 0, 0

    for k in sorted(imos.keys()):
        if t < k:
            break
        if acc <= 0 and cur+1 < k or acc + imos[k] <= 0:
            acc = 0
            break
        acc += imos[k]

    return acc <= 0


def add_imos(imos, x, y):
    imos[x] += y
    if imos[x] == 0:
        del imos[x]


def solve(t, px=-1, py=-1):
    set_x = {1, n}
    set_y = {1, m}

    for x, y in points:
        set_x.update((max(1, x-t), max(1, x-t-1), min(n, x+t), min(n, x+t+1)))
        set_y.update((max(1, y-t), max(1, y-t-1), min(m, y+t), min(m, y+t+1)))

    ans_x = ans_y = inf
    pi, imos, hq = 0, Counter(), []
    if px != -1:
        imos[py] += 1
        imos[py+t*2+1] -= 1

    for cx in sorted(set_x):
        while hq and hq[0][0] < cx:
            add_imos(imos, hq[0][1], -1)
            add_imos(imos, hq[0][2], +1)
            heappop(hq)
        while pi < k and pts_sorted_x[pi][0]-t <= cx <= pts_sorted_x[pi][0]+t:
            x, y = pts_sorted_x[pi]
            add_imos(imos, max(1, y-t), 1)
            add_imos(imos, y+t+1, -1)
            heappush(hq, (x+t, max(1, y-t), y+t+1))
            pi += 1

        if solve2(imos, m):
            ans_x = cx
            break

    pi = 0
    imos.clear()
    hq.clear()
    if px != -1:
        imos[px] += 1
        imos[px+t*2+1] -= 1

    for cy in sorted(set_y):
        while hq and hq[0][0] < cy:
            add_imos(imos, hq[0][1], -1)
            add_imos(imos, hq[0][2], +1)
            heappop(hq)
        while pi < k and pts_sorted_y[pi][1]-t <= cy <= pts_sorted_y[pi][1]+t:
            x, y = pts_sorted_y[pi]
            add_imos(imos, max(1, x-t), 1)
            add_imos(imos, x+t+1, -1)
            heappush(hq, (y+t, max(1, x-t), x+t+1))
            pi += 1

        if solve2(imos, n):
            ans_y = cy
            break

    return ans_x, ans_y


ok, ng = 10**9+1, -1
while abs(ok - ng) > 1:
    mid = (ok + ng) >> 1
    p = solve(mid)
    if p == OK:
        ok = mid
        continue

    if solve(mid, p[0], p[1]) == OK:
        ok = mid
    else:
        ng = mid

print(ok)