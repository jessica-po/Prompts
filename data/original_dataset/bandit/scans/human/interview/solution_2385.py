import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def ZIP(n): return list(zip(*(MAP() for _ in range(n))))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
lim = N+10  # 必要そうな階乗の限界を入れる
fact = [1] * (lim+1)
fact_inv = [1] * (lim+1)
for n in range(1, lim+1):
    fact[n] = (fact[n-1] * n) % mod
fact_inv[lim] = pow(fact[lim], mod-2, mod)
for n in range(lim, 0, -1):
    fact_inv[n-1] = (n * fact_inv[n]) % mod

tree = [[] for _ in range(N+1)]  # 1-indexed
for _ in range(N-1):
	a, b = MAP()
	tree[a].append(b)
	tree[b].append(a)

root = 1
parent = [0]*(N+1)
order = []
stack = [root]
while stack:
    x = stack.pop()
    order.append(x)
    for y in tree[x]:
        if y == parent[x]:
            continue
        parent[y] = x
        stack.append(y)

size_d = [0]*(N+1)
dp_d = [1]*(N+1)

for v in order[::-1]:  # 根に遠いほうから(down方向のボトムアップ)
    dp_d[v] *= fact[size_d[v]]
    dp_d[v] %= mod
    p = parent[v]
    s = size_d[v] + 1
    size_d[p] += s
    dp_d[p] *= fact_inv[s] * dp_d[v]
    dp_d[p] %= mod

size_u = [N-1-x for x in size_d]
dp_u = [1]*(N+1)

def merge(p1, p2):
    den_inv1, v1 = p1
    den_inv2, v2 = p2
    return den_inv1*den_inv2%mod, v1*v2%mod

for v in order:
    p = parent[v]
    arr = [(fact_inv[size_d[node]+1], dp_d[node]) if node != p else (fact_inv[size_u[v]], dp_u[v]) for node in tree[v]]
    left = [(1, 1)] + list(accumulate(arr, merge))[:-1]
    right = list(accumulate(arr[::-1], merge))[-2::-1] + [(1, 1)]
    contrib = [merge(x, y) for x, y in zip(left, right)]
    for node, c in zip(tree[v], contrib):
        if node != p:
            dp_u[node] = (c[0]*c[1]*fact[size_u[node]-1])%mod
# print(dp_u)
for xd, xu, sd, su in zip(dp_d[1:], dp_u[1:], size_d[1:], size_u[1:]):
    x = xd * xu * fact[sd + su] * fact_inv[sd] * fact_inv[su] % mod
    print(x)