INF = 10 ** 18
MX_SZ = 112
dp = [[[INF for k in range (MX_SZ)] for j in range (MX_SZ)] for i in range (MX_SZ)]
best = [[[(INF, INF) for k in range (MX_SZ)] for j in range (MX_SZ)] for i in range (MX_SZ)]

def read():
    return [int(x) for x in input().split()]

n, m, k_res = read()
arr = read()
cost = []
for i in range (n):
    cost.append(read())
dp[0][0][MX_SZ - 1] = 0 #[trees painted][group amount][last color]
best[0][0][0] = (0, MX_SZ - 1)
#print(best[0][0][0][1])
#return
for i in range (1, n + 1):
    clr = arr[i - 1]
    if clr == 0:
        for j in range (1, k_res + 1):
            for k in range (1, m + 1):
                dp[i][j][k] = dp[i - 1][j][k] + cost[i - 1][k - 1]
                if k == best[i - 1][j - 1][0][1]:
                    dp[i][j][k] = min(dp[i][j][k], best[i - 1][j - 1][1][0] + cost[i - 1][k - 1])
                else:
                    dp[i][j][k] = min(dp[i][j][k], best[i - 1][j - 1][0][0] + cost[i - 1][k - 1])
                if dp[i][j][k] < best[i][j][0][0]:
                    best[i][j][1] = best[i][j][0]
                    best[i][j][0] = (dp[i][j][k], k)
                elif dp[i][j][k] < best[i][j][1][0]:
                    best[i][j][1] = (dp[i][j][k], k)
    else:
        for j in range (1, n + 1):
            dp[i][j][clr] = dp[i - 1][j][clr]
            if clr == best[i - 1][j - 1][0][1]:
                dp[i][j][clr] = min(dp[i][j][clr], best[i - 1][j - 1][1][0])
            else:
                dp[i][j][clr] = min(dp[i][j][clr], best[i - 1][j - 1][0][0])
            best[i][j][0] = (dp[i][j][clr], clr)
ans = INF
for k in range (1, m + 1):
    if dp[n][k_res][k] < ans:
        ans = dp[n][k_res][k]
if ans == INF:
    ans = -1
print(ans)