n, s, m, k = map(int, input().split())
a = list(map(int, input().split()))
nt = [-1 for i in range(n+1)]
for i in range(s):
	l, r  = map(int, input().split())
	l-=1
	for j in range(l, r):
		nt[j] = max(nt[j], r)

dp = [[0 for i in range(m+1)] for i in range(n+1)]
sum = [0 for i in range(n+1)]
def solve(mid):
	for i in range(n+1):
		for j in range(m+1):
			dp[i][j] = 0
	for i in range(n):
		if a[i] <= mid:
			sum[i+1] = 1
		else:
			sum[i+1] = 0
		sum[i+1] += sum[i]
	for i in range(0, n+1):
		for j in range(m+1):
			if i > 0:
				dp[i][j] = max(dp[i][j], dp[i-1][j])
			if nt[i] != -1 and j < m:
				dp[nt[i]][j+1] = max(dp[nt[i]][j+1], dp[i][j] + sum[nt[i]] - sum[i])
	return dp[n][m]

lo, hi, ans = 1, 10**9, -1
while lo <= hi:
	mid = (lo+hi)//2
	if(solve(mid) >= k):
		ans = mid
		hi = mid-1
	else:
		lo = mid+1

print(ans)