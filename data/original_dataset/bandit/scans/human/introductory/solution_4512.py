# -*- coding: utf-8 -*-

import sys
from operator import add

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

class SegTree:
 
    def __init__(self, n, func, init):

        self.n = n
        self.func = func
        self.init = init

        n2 = 1
        while n2 < n:
            n2 <<= 1
        self.n2 = n2
        self.tree = [self.init] * (n2 << 1)
 
    def update(self, i, x):

        i += self.n2
        self.tree[i] = x
        while i > 1:
            self.tree[i >> 1] = x = self.func(x, self.tree[i ^ 1])
            i >>= 1
 
    def query(self, a, b):

        l = a + self.n2
        r = b + self.n2
        s = self.init
        while l < r:
            if r & 1:
                r -= 1
                s = self.func(s, self.tree[r])
            if l & 1:
                s = self.func(s, self.tree[l])
                l += 1
            l >>= 1
            r >>= 1
        return s

A = [ord(s)-97 for s in list(input())]
N = len(A)

st = [None] * 26
for i in range(26):
    st[i] = SegTree(N, add, 0)
for i, a in enumerate(A):
    st[a].update(i, 1)

for _ in range(INT()):
    a, b, c = input().split()
    if a == '1':
        b = int(b)
        cur = A[b-1]
        nxt = ord(c) - 97
        st[cur].update(b-1, 0)
        st[nxt].update(b-1, 1)
        A[b-1] = nxt
    else:
        b = int(b)
        c = int(c)
        cnt = 0
        for i in range(26):
            if st[i].query(b-1, c) >= 1:
                cnt += 1
        print(cnt)