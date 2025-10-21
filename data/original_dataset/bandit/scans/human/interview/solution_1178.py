import numpy as np
INF = 10**15
def solve(n, k, h):
    dp = np.full((n+1, n+1), INF, dtype=int)
    dp[0, 0] = 0
    h = np.array([0] + h, dtype=int)
    for i, h_i in enumerate(h[1:], 1):
        t = np.maximum(h_i - h[:i], 0)
        dp[i,1:] = np.min(dp[:i,:-1]+t[:,None], axis=0)
    return np.min(dp[:, n-k])

n, k = map(int, input().split())
h = list(map(int, input().split()))
print(solve(n, k, h))