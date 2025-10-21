R = lambda: map(int, input().split())
n = int(input())
dp = [0] * (10**6 + 1)
for x in R():
    dp[x] = 1
for i in range(10**6, -1, -1):
    if dp[i]:
        for x in range(i + i, 10**6 + 1, i):
            if dp[x]:
                dp[i] = max(dp[i], dp[x] + 1)
print(max(dp))