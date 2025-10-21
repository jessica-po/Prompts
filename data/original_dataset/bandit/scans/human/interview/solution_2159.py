n=int(input())
a=list(map(int,input().split()))
r=[0]*(n+1)
for i in range(n):
    d={}
    v=-1
    for j in range(i,n):
        t=d.get(a[j],0)+1
        d[a[j]]=t
        if t>v or t==v and a[j]<m:
            v=t
            m=a[j]
        r[m]+=1
print(' '.join(map(str,r[1:])))