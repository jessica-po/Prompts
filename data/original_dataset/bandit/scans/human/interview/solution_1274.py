import sys, math
from functools import lru_cache
import numpy as np
import heapq
from collections import defaultdict
sys.setrecursionlimit(10**9)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return list(map(int, input().split()))

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]


def lcm(a, b):
    return a*b//math.gcd(a, b)


def main():
    N, M = mi()
    A, B = i2(N)
    ans = 0

    d = defaultdict(list)
    for i in range(N):
        d[A[i]].append(B[i])

    h = []
    heapq.heapify(h)

    for i in range(1, M+1):
        for v in d[i]:
            heapq.heappush(h, -v)
        if h:
            ans -= heapq.heappop(h)
        else:
            continue

    print(ans)



def __starting_point():
    main()

__starting_point()