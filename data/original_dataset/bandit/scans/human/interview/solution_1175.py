MOD = 10**9 + 7
l, r = map(int, input().split())

def func(x, y):
	if y == 0:
		return 1
	dp = [[0 for _ in range(6)] for _ in range(61)]
	dp[60][0] = 1
	for i in range(59, -1, -1):
		if (y>>i) & 1 == 0 and (x>>i) & 1 == 0:
			dp[i][0] = dp[i+1][0]
			dp[i][1] = dp[i+1][1]
			dp[i][2] = dp[i+1][2]
			dp[i][3] = (dp[i+1][3]*2) % MOD
			dp[i][4] = dp[i+1][4]
			dp[i][5] = (dp[i+1][1] + dp[i+1][3] + dp[i+1][5]*3) % MOD
		elif (y>>i) & 1 == 1 and (x>>i) & 1 == 1:
			dp[i][0] = 0
			dp[i][1] = 0
			dp[i][2] = (dp[i+1][0] + dp[i+1][2]) % MOD
			dp[i][3] = (dp[i+1][1] + dp[i+1][3]) % MOD
			dp[i][4] = (dp[i+1][4]*2) % MOD
			dp[i][5] = (dp[i+1][4] + dp[i+1][5]*3) % MOD
		elif (y>>i) & 1 == 1 and (x>>i) & 1 == 0:
			dp[i][0] = 0
			dp[i][1] = (dp[i+1][0] + dp[i+1][1]) % MOD
			dp[i][2] = dp[i+1][2]
			dp[i][3] = (dp[i+1][2] + dp[i+1][3]*2) % MOD
			dp[i][4] = (dp[i+1][0] + dp[i+1][2] + dp[i+1][4]*2) % MOD
			dp[i][5] = (dp[i+1][1] + dp[i+1][3] + dp[i+1][4] + dp[i+1][5]*3) % MOD
		elif (y>>i) & 1 == 0 and (x>>i) & 1 == 1:
			dp[i][0] = 0
			dp[i][1] = 0
			dp[i][2] = 0
			dp[i][3] = (dp[i+1][1] + dp[i+1][3]) % MOD
			dp[i][4] = dp[i+1][4]
			dp[i][5] = (dp[i+1][5]*3) % MOD

	return (sum(dp[0]))%MOD

print(func(l, r))