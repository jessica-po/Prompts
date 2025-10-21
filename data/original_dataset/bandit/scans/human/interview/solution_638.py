from sys import stdin
n,m=list(map(int,stdin.readline().strip().split()))
s=list(map(int,stdin.readline().strip().split()))
ans=[0 for i in range(n)]
sm=[0 for i in range(n)]
sm1=[0 for i in range(n)]
for i in range(n):
    if i==0:
        sm[i]=s[i]
    else:
        sm[i]=sm[i-1]+s[i]
for i in range(n-1,-1,-1):
    if i==n-1:
        sm1[i]=s[i]
    else:
        sm1[i]=sm1[i+1]+s[i]
for i in range(n):
    if sm[i]<=m:
        continue
    x=sm[i]
    s2=s[0:i]
    s2.sort()
    r=0
    while x>m:
        x-=s2[-1]
        s2.pop()
        r+=1
    ans[i]=r
print(*ans)