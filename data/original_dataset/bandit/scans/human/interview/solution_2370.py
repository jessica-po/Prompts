from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

import numpy as np

n = int(input())
a = np.array([list(map(int, input().split())) for _ in range(n)])

g = csr_matrix(a)
dist = floyd_warshall(g)

if (dist == a).all():
    sm = a.sum()

    INF = 10 ** 18 + 1
    for i in range(n):
        a[i, i] = INF

    for u in range(n):
        for v in range(n):
            if u == v:
                continue

            mn = np.min(a[u] + a[v])
            if mn == a[u, v]:
                sm -= a[u, v]

    ans = sm // 2
    print(ans)

else:
    print((-1))