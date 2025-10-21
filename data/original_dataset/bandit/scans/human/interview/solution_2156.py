from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

N = inp()
aa = inpl()
Q = inp()

tmp = 0
ruiseki = [0]
for a in aa:
    tmp += a
    ruiseki.append(tmp)

for q in range(Q):
    l,r = inpl()
    print((ruiseki[r]-ruiseki[l-1])//10)