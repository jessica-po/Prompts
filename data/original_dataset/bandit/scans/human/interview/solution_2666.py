try:
 n,k = map(int,input().split())
 x = [int(input()) for _ in range(n)]
 k = k//2
 dp = [0]*(k+1)
 for i in range(k+1):
  dp[i] = [0]*n
 #print(dp)
 for i in range(1,k+1):
  #print("*",dp[i-1][0])
  diff = (-1)*x[0]
  for j in range(1,n):
   diff = max(dp[i-1][j]-x[j],diff)
   dp[i][j] = max(dp[i][j-1],diff+x[j])
 print(dp[k][n-1])
except:
 pass