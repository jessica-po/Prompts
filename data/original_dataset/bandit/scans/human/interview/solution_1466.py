from collections import Counter, defaultdict
import heapq
from sys import stdin, stdout
raw_input = stdin.readline
xrange=range
n,m,k=list(map(int,input().split()))
k=min(n-1,k)
p=[0]*(n+1)
vis = [0]*(n+1)
d=[[] for i in range(n+1)]
ans=[]
dp={}
for i in range(m):
    u,v,w=list(map(int,input().split()))
    d[u].append((v,w))
    d[v].append((u,w))
    dp[(u,v)]=i+1
    dp[(v,u)]=i+1
q=[(0,1,1)]
c=0
while q:
    wt,x,par=heapq.heappop(q)
    if vis[x]:
        continue
    vis[x]=1
    c+=1
    if par!=x:
        
        ans.append(str(dp[(par,x)]))
    if c>k:
        break
    
    for i,w in d[x]:
        if not vis[i]:
            heapq.heappush(q,(wt+w,i,x))
print(len(ans))
print(' '.join(ans))