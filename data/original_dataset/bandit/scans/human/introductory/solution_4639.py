#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
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
    t = I()
    for _ in range(t):
        n,k = LI()
        f = 1
        p = 1
        while f <= k:
            f += p
            p += 1
        f -= p
        p -= 2
        k -= f
        p = n-p
        k = n-k
        ans = "a"*(p-2)+"b"+"a"*(k-p+1)+"b"+"a"*(n-k-1)
        print(ans)
    return

#Solve
def __starting_point():
    solve()

__starting_point()