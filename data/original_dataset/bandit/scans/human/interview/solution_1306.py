mod = 10**9 + 7
n, h = map(int, input().split())
a = list(map(int, input().split()))
dp = [[0 for j in range(h + 1)] for i in range (n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
	need = h - a[i - 1]
	if need < 0:
		break
	if need == 0:
		dp[i][0] = dp[i - 1][0]
	else:
		dp[i][need] = (dp[i - 1][need] + dp[i - 1][need - 1]) % mod
		dp[i][need - 1] = (dp[i][need] * need) % mod
print(dp[n][0])