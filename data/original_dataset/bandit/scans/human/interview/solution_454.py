import numpy as np


def solve(n, k):
    if k % 2 == 1:
        return 0
    k //= 2

    MOD = 10 ** 9 + 7

    dp = np.zeros((1, k + 1), dtype=np.int64)
    dp[0, 0] = 1
    for i in range(1, n + 1):
        max_d = min(i + 1, n - i + 1, k + 1)
        ndp = np.zeros((max_d, k + 1), dtype=np.int64)
        for d, ks in enumerate(dp):
            base = ks[:k - d + 1]
            if d > 0:
                ndp[d - 1, d:] += base * d ** 2
            if max_d > d:
                ndp[d, d:] += base * (2 * d + 1)
            if max_d > d + 1:
                ndp[d + 1, d:] += base
        dp = ndp % MOD

    return dp[0, k]


n, k = list(map(int, input().split()))
print((solve(n, k)))