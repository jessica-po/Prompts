import sys
input = sys.stdin.readline
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
mod=998244353
sol=1
i=n-1
j=m-1
while sol>0 and j>=0:
    goal=b[j]
    s=0
    r=False
    while i>=0 and a[i]>=goal:
        if r:
            s+=1
        else:
            if a[i]==goal:
                r=True
                s=1
        i-=1
    if j==0:
        s=min(s,1)
        if i>=0:
            s=0
    sol*=s
    sol%=mod
    j-=1
print(sol)