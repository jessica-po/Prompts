import sys
import math

def solve():
    k, n = list(map(int, input().split()))
    D = {}
    for line in sys.stdin:
        s, a = line.split()
        if s in D:
            D[s].append(int(a))
        else:
            D[s] = [int(a)]

    res = 0
    center = 0
    for s in D:
        revs = s[::-1]
        if not revs in D: continue
        D[revs].sort()
        D[s].sort()

        if s == revs:
            while len(D[s]) > 1 and D[s][-2] + D[s][-1] > 0:
                center = max(center, -D[s][-2])
                res += D[s].pop()
                res += D[s].pop()

            if len(D[s]) > 0:
                center = max(center, D[s][-1])
        else:
            while (len(D[s]) > 0 and len(D[revs]) > 0 and
                   D[s][-1] + D[revs][-1] > 0):
                res += D[s].pop()
                res += D[revs].pop()

    return res + center

print(solve())