import sys
from collections import defaultdict

# 再帰制限を緩和するおまじない
sys.setrecursionlimit(10**6)

def sum(n):return n*(n+1)//2

# 部分木のサイズと、「色iを封鎖したときに到達できない頂点の個数」を持つ辞書を返す
def dfs(v,p):
    ret=defaultdict(int)
    size=1
    for vv in g[v]:
        if vv==p:
            continue
        ss,d=dfs(vv,v)
        size+=ss
        ans[c[v]]+=sum(ss-d[c[v]])
        
        # マージテク
        if len(ret)<len(d):
            ret,d=d,ret
        for vvv in d:
            ret[vvv]+=d[vvv]
    ret[c[v]]=size
    return size,ret

n=int(input())
c=list(map(int,input().split()))
g=[[] for _ in range(n+1)]
ans=[0]*(n+1)
for _ in range(n-1):
    s,t=list(map(int, input().split()))
    s-=1
    t-=1
    g[s].append(t)
    g[t].append(s)
_,ret=dfs(0,-1)
for i in range(1,n+1):
    print((sum(n)-ans[i]-sum(n-ret[i])))