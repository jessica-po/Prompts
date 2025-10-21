#!/usr/bin/env python3

import sys
input=sys.stdin.readline

class BIT:
  def __init__(self,n):
    self.n=n+1
    self.BIT=[0]*self.n
  def add(self,i,x):
    idx=i
    while idx<self.n:
      self.BIT[idx]+=x
      idx+=(idx&-idx)
  def _sum(self,i):
    if i==-1:
        return -1
    ret=0
    idx=i
    while idx>0:
      ret+=self.BIT[idx]
      idx-=(idx&-idx)
    return ret
  def sum(self,l,r):
    return self._sum(r)-self._sum(l-1)
  def value(self,i):
    return self._sum(i)-self._sum(i-1)

bound=10**6
n,m=map(int,input().split())
yoko_edges=[list(map(int,input().split())) for _ in range(n)]
yoko_edges=sorted(yoko_edges,reverse=True,key=lambda x:x[0])
ue_tate_edges=[[] for _ in range(bound+1)]
sita_tate_edges=[[] for _ in range(bound+1)]
tate_edges=BIT(bound)
tate_edges.add(bound,1)
ans=1
for _ in range(m):
    x,l,r=map(int,input().split())
    if l==0 and r==bound:
        tate_edges.add(x,1)
        ans+=1
    elif l==0:
        sita_tate_edges[r].append(x)
    elif r==bound:
        ue_tate_edges[l].append(x)
        tate_edges.add(x,1)
prev=bound-1
for y,l,r in yoko_edges:
    while prev>=y:
        for x in sita_tate_edges[prev]:
            tate_edges.add(x,1)
        for x in ue_tate_edges[prev+1]:
            tate_edges.add(x,-1)
        prev-=1
    ans+=tate_edges.sum(l,r)-1
print(ans)