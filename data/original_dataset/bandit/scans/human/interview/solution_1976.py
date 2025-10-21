import sys
from operator import itemgetter

n, m, k, q = list(map(int, input().split()))
query = sorted((list(map(int, line.split()))
                for line in sys.stdin), key=itemgetter(2))
times = [q[2] for q in query]


def solve(ti):
    imos = [[0]*(m+1) for _ in range(n+1)]
    for i in range(ti):
        imos[query[i][0]][query[i][1]] += 1

    for i in range(n+1):
        for j in range(m):
            imos[i][j+1] += imos[i][j]
    for j in range(m+1):
        for i in range(n):
            imos[i+1][j] += imos[i][j]
    for i in range(k, n+1):
        for j in range(k, m+1):
            if imos[i][j] - imos[i-k][j] - imos[i][j-k] + imos[i-k][j-k] == k*k:
                return True
    return False


inf = len(times)+1
ok, ng = inf, 0
while abs(ok - ng) > 1:
    mid = (ok + ng) >> 1
    if mid >= k*k and solve(mid):
        ok = mid
    else:
        ng = mid

print(times[ok-1] if ok != inf else -1)