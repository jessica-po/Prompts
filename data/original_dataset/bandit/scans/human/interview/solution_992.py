import numpy as np
n,s=map(int,input().split())
a=list(map(int,input().split()))
mod=998244353
dp=np.zeros([n+1,s+1],int)
dp[0][0]=1
for i in range(1,n+1):
  dp[i][:]=dp[i-1][:]*2
  dp[i][a[i-1]:]+=dp[i-1][:-a[i-1]]
  dp[i][:]%=mod
print(dp[n][s])