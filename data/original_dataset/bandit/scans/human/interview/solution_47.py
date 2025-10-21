N, X = list(map(int, input().split()))
A = [int(a) for a in input().split()]

dp = [[0]*4 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][0] = max(dp[i-1][0] + A[i-1], 0)
    dp[i][1] = max(dp[i-1][1] + A[i-1] * X, dp[i][0])
    dp[i][2] = max(dp[i-1][2] + A[i-1], dp[i][1])
    dp[i][3] = max(dp[i-1][3], dp[i][2])

print(dp[N][3])