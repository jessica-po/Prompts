from sys import stdin
n,m=list(map(int,stdin.readline().strip().split()))
s=[]
for i in range(n):
    s.append(list(map(ord,list(stdin.readline().strip()))))
    for j in range(m):
        s[-1][j]=s[-1][j]-97
ct=[tuple(map(int,stdin.readline().strip().split())) for i in range(n)]
mc=[[0 for i in range(22)] for j in range(22)]
c=[[0 for i in range(22)] for i in  range(22)]
maxmask=1<<n
maxx=10**8
dp=[maxx for i in range(maxmask)]
for i in range(n):
    for j in range(m):
        mx=0
        for k in range(n):
            if s[i][j]==s[k][j]:
                mc[i][j]|=(1<<k)
                c[i][j]+=ct[k][j]
                mx=max(mx,ct[k][j])
        c[i][j]-=mx
dp[0]=0
for i in range(1,maxmask):
    for j in range(n):
        if i & (1<<j):
            lb=j
            break
    mask=i
    for j in range(m):
        dp[mask]=min(dp[mask],dp[mask ^(1<<lb)]+ct[lb][j],dp[mask & (mask ^ mc[lb][j])]+c[lb][j])
print(dp[(1<<n)-1])