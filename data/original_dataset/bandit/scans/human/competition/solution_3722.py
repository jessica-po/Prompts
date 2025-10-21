from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 13
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().rstrip().split()
def S(): return sys.stdin.readline().rstrip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007

#aかbのどちらかは無限に増やせる
n=I()
c1=S()
c2=S()
c3=S()
c4=S()

if n<=3:
    print((1))
    return

if c2=="A":
    if c1=="A":
        print((1))
    else:
        dp = [[0] * 2 for _ in range(n - 3)]
        dp[0][0] = 1
        dp[0][1] = 1
        for i in range(1, n - 3):
            dp[i][0] = sum(dp[i - 1]) % mod
            dp[i][1] = dp[i - 1][0]
        if c3=="A":
            print((sum(dp[-1]) % mod))
        else:
            print((pow(2,n-3,mod)))
else:
    if c4=="B":
        print((1))
    else:
        dp = [[0] * 2 for _ in range(n - 3)]
        dp[0][0] = 1
        dp[0][1] = 1
        for i in range(1, n - 3):
            dp[i][0] = sum(dp[i - 1]) % mod
            dp[i][1] = dp[i - 1][0]
        if c3=="B":
            print((sum(dp[-1]) % mod))
        else:
            print((pow(2,n -3,mod)))