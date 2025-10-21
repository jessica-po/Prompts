import numpy as np
from sys import stdin

'''
Reference: https://codeforces.com/blog/entry/75046#comment-591494 (1-based index)

(0-based index)

For a sequence A[l]..A[k]..A[r] with sum S contributes l * (N - r) to answer.
    0, 1, 2, ..., l....k....r, ..., N - 2, N - 1
    x  x  x   x   x         v   v     v      v
There are l `x` and (N - r) `v`.

Enumerate all possible sequence is impossible. 
Consider all sequeuces with sum S and **ends** at specific r:
    A[l1]...A[r] -> l1 * (N - r)
    A[l2]...A[r] -> l2 * (N - r)
    A[l3]...A[r] -> l3 * (N - r)
    .
    .
    .
which contributes (l1 + l2 + ... + lm) * (N - r) in total.

We can find *sum of left index for all valid sequence* for each r using DP.

    dp[i][s] = the sum of left index for all sequence that
                    1. ends at i
                    2. has sum s
    
    dp[i][:A[i]] = 0  since any sequence ends at i has sum >= A[i]

    dp[i][A[i]] = i + 1
    dp[i][s] = sum(dp[j][s - A[i]] for j in range(i))

    Take A = [2, 3, 4] for example, sequences that end at A[2] are:
    
                   [4] -> dp[2][4] = 3
             [2,    4] ↘
                [3, 4] -> dp[2][s] = dp[2][s - 4] for all s
             [2, 3, 4] ↗
    
    The answer is sum(dp[r][S] * (N - r) for r in range(N))

So the naive implementation is:

    dp = np.zeros((N, max(S, A.max()) + 1), dtype=np.int64)
    for i, a in enumerate(A):
        dp[i, a] = i + 1
        for s in range(a + 1, S + 1):
            dp[i, s] = dp[:i, s - a].sum() % M  # here can be optimized
    
    ans = 0
    for i in range(N):
        ans += (N - i) * dp[i, S]
        ans = ans % M

has time O(N * S * N) which results in TLE.

Using another array to store the cumsum (prefix sum) of dp solves the problem:
'''

N, S = list(map(int, input().split()))
A = np.int32(input().split())
M = 998244353
V = max(A.max(), S)

ans = 0
dp = np.zeros((N, V + 1), dtype=np.int64)
cs = np.zeros(V + 1, dtype=np.int64)
for i, a in enumerate(A):
    dp[i, a] = i + 1
    dp[i, a + 1 : S + 1] = cs[np.arange(a + 1, S + 1) - a]
    cs = (cs + dp[i]) % M
    ans = (ans + (N - i) * dp[i, S]) % M
print(ans)