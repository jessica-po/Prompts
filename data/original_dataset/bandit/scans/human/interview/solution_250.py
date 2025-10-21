import math
from functools import reduce
class SegmentTree():
    def __init__(self, L, function = lambda x,y: x+y):
        self.function = function
        N = self.size = len(L)
        M = 1 << N.bit_length()
        self.margin = 2*M - N
        self.L = [None for i in range(self.margin)] + L
        for i in range(M-1, 0, -1):
            x, y = self.L[i<<1], self.L[i<<1|1]
            self.L[i] = None if x is None or y is None else function(x, y)
    def modify(self, pos, value):
        p = pos + self.margin
        self.L[p] = value 
        while p > 1:
            x, y = self.L[p], self.L[p^1]
            if p&1: x, y = y, x
            self.L[p>>1] = None if x is None or y is None else self.function(x, y)
            p>>=1
    def query(self, left, right):
        l, r = left + self.margin, right + self.margin
        stack = []
        void = True
        while l < r:
            if l&1:
                if void:
                    result = self.L[l]
                    void = False
                else:
                    result = self.function(result, self.L[l])
                l+=1
            if r&1:
                r-=1
                stack.append(self.L[r])
            l>>=1
            r>>=1
        init = stack.pop() if void else result
        return reduce(self.function, reversed(stack), init)

n = int(input())
pies, index, first_equal = [0]*n, [0]*n, [0]*n
for i in range(n):
    r, h = [int(x) for x in input().split()]
    pies[i] = r*r*h
s_pies = list(sorted(enumerate(pies), key = lambda p: p[1]))
for i in range(n): index[s_pies[i][0]] = i
for i in range(1, n):
    first_equal[s_pies[i][0]] = i if s_pies[i][1] != s_pies[i-1][1] else first_equal[s_pies[i-1][0]]
towers = SegmentTree([0]*(n+1), max)
for j, pie in enumerate(pies):
    i, k = index[j], first_equal[j]
    q = towers.query(0, k+1)
    towers.modify(i+1, q + pie)
print(math.pi * towers.query(0, n+1))