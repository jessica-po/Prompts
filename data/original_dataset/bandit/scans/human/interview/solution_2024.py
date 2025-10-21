from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())
a = map(int, input().split())
mod = 998244353
d = defaultdict(int)
for x in a:
    d[x] += 1
d[0] = 0
b = list(d.items())
b.sort()
m = len(b)
ba = [0] * m
cn = [0] * (m + 1)
k = h = 0
for i, x in enumerate(b):
    while h < m and x[0] >= b[h][0] * 2:
        h += 1
    ba[i] = h - 1
    while k < m and x[0] * 2 > b[k][0]:
        k += 1
    cn[k] += x[1]
for i in range(m):
    cn[i+1] += cn[i]
dp = [0] * m
dp[0] = 1
b = [x[1] for x in b]
for i in range(n):
    ndp = [0] * m
    for j in range(1, m):
        if cn[j] >= i - 1:
            ndp[j] = dp[j] * (cn[j] - i + 1) % mod
        dp[j] += dp[j-1]
        if dp[j] >= mod:
            dp[j] -= mod
    for j in range(1, m):
        ndp[j] += dp[ba[j]] * b[j]
        ndp[j] %= mod
    dp = ndp
print(sum(dp) % mod)