n,m=map(int,input().split())
a=list(map(int,input().split()))
dp=[0]+[-1]*(9*n)
l=[0,2,5,5,4,5,6,3,7,6]
for i in range(n):
  for j in a:
    if dp[i]>=0:
      dp[i+l[j]]=max(dp[i+l[j]],dp[i]*10+j)
print(dp[n])