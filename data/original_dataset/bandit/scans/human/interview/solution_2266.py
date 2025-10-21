import os, sys, bisect, copy
from collections import defaultdict, Counter, deque
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
def input(): return sys.stdin.readline()
def mapi(arg=0): return map(int if arg==0 else str,input().split())
#------------------------------------------------------------------

n,k,d = mapi()
plc = list(mapi())
gr = defaultdict(list)
for i in range(1,n):
    u,v = mapi()
    gr[u].append([v,i])
    gr[v].append([u,i])
q = deque()
for i in plc:
    q.append((i,0))
vis = {}
res = [0]*(n+1)
while q:
    tmp,par = q.popleft()
    if tmp in vis:
        continue
    vis[tmp] = 1
    for item in gr[tmp]:
        if item[0] != par:
            if item[0] in vis:
                res[item[1]] = 1
            else:
                q.append((item[0],tmp))
cnt = 0
ans = []
for i in range(1,n+1):
    if res[i]==1:
        cnt+=1
        ans.append(i)
print(cnt)
print(*ans)