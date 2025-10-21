n, m = list(map(int, input().split()))
p = [0] * n
e = []
for i in range(m):
    q, w = list(map(int, input().split()))
    p[w - 1] += 1
    p[q - 1] += 1
    e.append([min(q, w), max(q, w)])
dp = [1] * n
e.sort()
for i in range(m):
    dp[e[i][1] - 1] = max(dp[e[i][1] - 1], dp[e[i][0] - 1] + 1)
ans = 0
for i in range(n):
    ans = max(ans, dp[i] * p[i])
print(ans)