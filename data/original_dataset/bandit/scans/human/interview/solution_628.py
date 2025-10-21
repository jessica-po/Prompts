#!/usr/bin/env python3

[n, k] = list(map(int, input().strip().split()))
ais = list(map(int, input().strip().split()))
iais = [0 for _ in range(n + 1)]
for i in range(n):
	iais[i + 1] = iais[i] + ais[i]

def calc(k, split):
	res = 0
	for i in range(k):
		res &= iais[split[i + 1]] - iais[split[i]]
	return res

def check_mask(mask):
	dp = [[False for j in range(n + 1)] for i in range(k + 1)]

	for j in range(1, n - k + 1 + 1):
		dp[1][j] = (iais[j] & mask == mask)
	if not any(dp[1]):
		return False

	for i in range(2, k + 1):
		for j in range(i, n - (k - i) + 1):
			dp[i][j] = any(dp[i - 1][r] and ((iais[j] - iais[r]) & mask == mask) for r in range(i - 1, j - 1 + 1))
		if not any(dp[i]):
			return False

	return dp[k][n]


mask = 0
for i in range(55, -1, -1):
	if check_mask(mask | (1 << i)):
		mask |= 1 << i

print (mask)