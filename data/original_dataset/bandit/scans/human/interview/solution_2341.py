n,m=map(int,input().split())
L=[]
for i in ' '*n:L.append(input())
dp=[[0]*m for i in range(n)]
for i in range(n+m-1):
    rightmin=max(0,i-(n-1))
    leftmin=max(0,i-(m-1))
    left=i-rightmin
    jstart = max(0, i - (n - 1))
    for j in range(abs(left-leftmin)+1):
        jj=jstart+j
        ii=i-jj
        if jj<2 or ii<1 or ii==n-1:
            dp[ii][jj]=1
            continue
        if L[ii+1][jj-1]==L[ii][jj-1]==L[ii][jj-2]==L[ii-1][jj-1]==L[ii][jj]:
            dp[ii][jj]=min(dp[ii+1][jj-1],dp[ii][jj-1],dp[ii][jj-2],dp[ii-1][jj-1])+1
        else:dp[ii][jj]=1
ct=0
for i in dp:
    for j in i:
        ct+=j
print(ct)