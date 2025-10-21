n, k = map(int, input().split())
l = [(0, 0) for i in range(k)]
for i in range(k):
    start, end = map(int, input().split())
    l[i] = start, end

dp = [0 for i in range(n+1)]
prefixSum = [0 for i in range(n+1)]

dp[1] = 1
prefixSum[1] = 1

for i in range(2, n + 1):
    for j in range(k):
        start, end = l[j]
        i_s = max(i - start, 0)
        i_e = max(i - end -1, 0)    
        dp[i] += prefixSum[i_s] - prefixSum[i_e]
        dp[i] %= 998244353
    prefixSum[i] = prefixSum[i-1] + dp[i]
    prefixSum[i] %= 998244353

print(dp[n])