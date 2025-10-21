#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    n,k,q = LI()
    a = LI()
    b = [[a[i],i] for i in range(n)]
    b.sort()
    ans = b[q-1][0]-b[0][0]
    l = [-1,n]
    for i in range(1,n):
        l.append(b[i-1][1])
        l.sort()
        if b[i-1][0] == b[i][0]:
            continue
        s = [a[l[i]+1:l[i+1]] for i in range(i+1)]
        c = []
        for si in s:
            si.sort()
            for j in range(len(si)-k+1):
                c.append(si[j])
        if len(c) < q:
            continue
        c.sort()
        m = c[q-1]-c[0]
        if m < ans:
            ans = m
    print(ans)
    return

#Solve
def __starting_point():
    solve()

__starting_point()