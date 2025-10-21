3

import sys

# 1 <= n, d <= 1000, 1 <= k <= 10**9
n, k, d = list(map(int, sys.stdin.readline().split()))

no_sol = False
solution = [[1 for j in range(n)] for i in range(d)]


def schedule(i, j, level):
    nonlocal no_sol
    if level >= d:
        no_sol = True
        return
    count = j - i
    chunk = count // k
    extra = count % k
    r = i
    for t in range(min(k, count)):
        size = chunk + (1 if t < extra else 0)
        for z in range(size):
            solution[level][r+z] = t+1
        if size > 1:
            schedule(r, r + size, level + 1)
        r += size

if k == 1:
    if n > 1:
        no_sol = True
else:
    schedule(0, n, 0)

if no_sol:
    print(-1)
else:
    for l in solution:
        print(' '.join(str(x) for x in l))