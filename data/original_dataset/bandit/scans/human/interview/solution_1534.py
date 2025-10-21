s=input()
dp=[[0,0,0] for i in range(len(s))]
for i in range(len(s)):
    if s[i]=='a':
        dp[i][0]=dp[i-1][0]+1
        dp[i][1]=dp[i-1][1]
        dp[i][2]=max(dp[i-1][1]+1,dp[i-1][2]+1)
    else:
        dp[i][0]=dp[i-1][0]
        dp[i][1]=max(dp[i-1][0]+1,dp[i-1][1]+1)
        dp[i][2]=dp[i-1][2]
e=len(s)-1
print(max(dp[e][0],dp[e][1],dp[e][2]))