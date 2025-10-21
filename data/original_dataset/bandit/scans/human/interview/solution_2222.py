import sys
from collections import deque
sys.setrecursionlimit(20000000)
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
g = [[] for i in range(n)]
for i in range(n-1):
    g[b[i]-1].append(i+1)
ha = 0
for i in range(n):
    if len(g[i]) == 0:
        ha += 1
kyo = [1<<30] * n
def dfs(x,y):
  kyo[x] = y
  for i in g[x]:
    que.append([i,y+1])
que = deque()
que.append([0,0])
while que:
    aa,bb = que.popleft()
    dfs(aa,bb)
hukai = []
for i in range(n):
  hukai.append([kyo[i],i])
hukai.sort(key = lambda x:-x[0])
dp = [1<<30]*n
for j,i in hukai:
    if len(g[i]) == 0:
        dp[i] = 0
        continue
    sita = []
    for k in g[i]:
        sita.append(dp[k])
    if a[i] == 1:
        dp[i] = min(sita)
    else:
        dp[i] = sum(sita)+len(g[i])-1
ans = ha-dp[0]
print(ans)