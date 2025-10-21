import sys
from collections import deque

input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    edge=[[] for i in range(n)]
    for i in range(n-1):
        u,v=list(map(int,input().split()))
        edge[u-1].append(v-1)
        edge[v-1].append(u-1)
    m=int(input())
    p=list(map(int,input().split()))

    size=[1 for i in range(n)]
    parent=[-1 for i in range(n)]
    res=[]
    deq=deque([(0,-1)])
    while deq:
        v,pv=deq.popleft()
        res.append(v)
        for nv in edge[v]:
            if nv!=pv:
                parent[nv]=v
                deq.append((nv,v))

    res=res[::-1]
    for v in res:
        for nv in edge[v]:
            if nv!=parent[v]:
                size[v]+=size[nv]

    coef=[]
    for v in res:
        for nv in edge[v]:
            if nv!=parent[v]:
                c=size[nv]*(n-size[nv])
                coef.append(c)
    mod=10**9+7
    #print(coef)
    #print(p)
    #print(size)
    if m<n-1:
        res=0
        coef.sort(reverse=True)
        p.sort(reverse=True)
        for i in range(m):
            res+=coef[i]*p[i]
            res%=mod
        for i in range(m,n-1):
            res+=coef[i]
            res%=mod
        print(res)
    else:
        res=0
        coef.sort()
        p.sort()
        for i in range(n-2):
            res+=coef[i]*p[i]
            res%=mod
        tmp=coef[-1]
        for i in range(n-2,m):
            tmp*=p[i]
            tmp%=mod
        res=(res+tmp)%mod
        print(res)