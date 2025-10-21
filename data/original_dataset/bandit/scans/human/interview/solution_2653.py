import sys
sys.setrecursionlimit(10**7)
 
N, Q = list(map(int, input().split()))
root = [[] for _ in range(N)]
ans = [0]*N
 
for _ in range(N-1):
  a,b=list(map(int, input().split()))
  a,b=a-1,b-1
  root[a].append(b)
  root[b].append(a)

for _ in range(Q):
  p,x=list(map(int, input().split()))
  ans[p-1]+=x
  
visited=[False]*N
def dfs(v):
  visited[v] = True
  for go in root[v]:
    if visited[go]:
      continue
    ans[go] += ans[v]
    dfs(go)

dfs(0)
print((*ans))