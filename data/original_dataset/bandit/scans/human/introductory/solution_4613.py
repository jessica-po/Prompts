import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())
def NIJIGEN(H): return [list(input()) for i in range(H)]
def dfs(j):
  if j not in finish:
    finish.add(j)
    for k in L[j]:
      dfs(k)
N,M=MAP()
s=list()
L=[[] for _ in range(N)]
for i in range(M):
  a,b=MAP()
  a-=1
  b-=1
  L[a].append(b)
  L[b].append(a)
  s.append([a,b])
ans=0
for i in range(M):
  a,b=s[i]
  L[a].remove(b)
  L[b].remove(a)
  finish=set()
  dfs(a)
  if len(finish)!=N:
    ans+=1
  L[a].append(b)
  L[b].append(a)
print(ans)