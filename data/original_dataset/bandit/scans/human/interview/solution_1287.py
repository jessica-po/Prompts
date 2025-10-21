import sys

n = int(input())
prob = [list(map(float, input().split())) for _ in range(n)]
dp = [[0.0]*n for _ in range(1 << n)]
dp[1][0] = 1.0

for mask in range(3, 1 << n):
    for i in range(n):
        if not (mask & (1 << i)):
            continue
        for j in range(n):
            if i != j and mask & (1 << j):
                dp[mask][i] = max(
                    dp[mask][i],
                    dp[mask - (1 << j)][i] * prob[i][j]
                    + dp[mask - (1 << i)][j] * prob[j][i]
                )

print(max(dp[-1]))