from collections import defaultdict

def calcBinomials(N):
    nonlocal binom
    N += 1
    binom = [[0]*N for _ in range(N)]
    for n in range(N):
        binom[n][0] = binom[n][n] = 1
        for k in range(1, n):
            binom[n][k] = binom[n-1][k] + binom[n-1][k-1]

n = int(input())
a = list(map(int, input().split()))
S, res = sum(a), 0
dp = [defaultdict(lambda: 0) for _ in range(S+1)]
dp[0][0] = 1

cnt = {_:a.count(_) for _ in a}
for x in a:
    for i in range(len(dp)-1-x, -1, -1):
        for k, v in list(dp[i].items()):
            dp[i+x][k+1] += v

calcBinomials(n)
for x, c in list(cnt.items()):
    for i in range(1, c+1):
        if dp[x*i][i] == binom[c][i] or dp[S - x*i][n-i] == binom[c][c-i]:
            res = max(res, i)
if len(cnt) <= 2: res = n
print(res)