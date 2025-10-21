from collections import *
from itertools import *
from bisect import *
from heapq import *

import math
from fractions import gcd
import sys
#input = sys.stdin.readline

import copy

N,M=list(map(int,input().split()))
UV=[list(map(int,input().split())) for i in range(M)]
S,T=list(map(int,input().split()))

data=[[] for i in range(N+1)]
for u,v in UV:
    data[u].append(v)

visited={S}
visited1=set()
visited2=set()
stack=deque([[S,0]])
while stack:
    a,m=stack.popleft()
    for p in data[a]:
        z=(m+1)

        if z%3==0:
            if p in visited:
                continue
            elif p == T:
                print((z//3))
                return
            else:
                visited.add(p)
        if z%3==1:
            if p in visited1:
                continue
            else:
                visited1.add(p)
        if z%3==2:
            if p in visited2:
                continue
            else:
                visited2.add(p)
        stack.append([p,z])

print((-1))