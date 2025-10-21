n = int(input())
a = list(map(int, input().split()))

dp = [[False] * (n + 1) for i in range(n + 1)]

def solve(l, r):
    if dp[l][r]:
        return dp[l][r]
    if r - l == 1:
        dp[l][r] = (a[l], 1)
        return dp[l][r]
    tmp = 10 ** 9
    for i in range(l + 1, r):
        if solve(l, i)[0] == -1 or solve(i, r)[0] == -1:
            tmp = min(tmp, dp[l][i][1] + dp[i][r][1])
        elif solve(l, i) == solve(i, r):
            tmp = solve(l, i)[0] + 1
            dp[l][r] = (tmp, 1)
            return dp[l][r]
        else:
            tmp = min(tmp, 2)
    dp[l][r] = (-1, tmp)
    return dp[l][r]

solve(0, n)
print(dp[0][n][1])