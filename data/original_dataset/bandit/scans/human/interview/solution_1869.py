from sys import stdin

n = int(stdin.readline())
a = list(map(int,stdin.readline().split()))
a = [0] + a

ans = n

dp = [float("inf")] * (n+1)
dp[0] = 0
for i in range(1,n+1):

    nmin = float("inf")
    for j in range(i-1,-1,-1):
        if a[j] <= nmin:
            dp[i] = min(dp[i] , dp[j] + max(0,a[i]-a[j]) + (i-j-1) )
        nmin = min(nmin,a[j])

#print (dp)
for i in range(n+1):
    ans = min(ans , dp[i] + n-i)
print (ans)