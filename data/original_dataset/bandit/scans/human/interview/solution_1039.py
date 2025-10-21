from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def MAP1()  : return map(lambda x:int(x)-1,input().split())
def LIST()  : return list(MAP())

def solve():
    N = INT()
    adj = [[] for _ in range(N)]
    for i in range(N-1):
        a, b, c = MAP()
        adj[a-1].append([b-1, c])
        adj[b-1].append([a-1, c])

    Q, K = MAP()
    K -= 1

    d = [inf]*N
    d[K] = 0
    que = []
    heappush(que, K)

    while que:
        v = heappop(que)
        for b, c in adj[v]:
            if d[b] > d[v] + c:
                d[b] = d[v] + c
                heappush(que, b)

    for i in range(Q):
        x, y = MAP()
        print(d[x-1]+d[y-1])

def __starting_point():
    solve()
__starting_point()