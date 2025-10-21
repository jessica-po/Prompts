# -*- coding: utf-8 -*-
import sys
from operator import itemgetter
from fractions import gcd
from math import ceil, floor
from copy import deepcopy
from itertools import accumulate
from collections import Counter
import math
from functools import reduce
from bisect import bisect_right
sys.setrecursionlimit(200000)
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(x): print("debug: ", x, file=sys.stderr)
# template


class BIT:
    def __init__(self, x, d=0):
        if isinstance(x, int):
            self.size = x
            self.tree = [d for _ in range(self.size + 1)]
        elif isinstance(x, list):
            self.size = len(x)
            self.tree = [d for _ in range(self.size + 1)]
            self.build(x)
        else:
            raise TypeError

    def build(self, arr):
        if isinstance(arr, list):
            raise TypeError
        for num, x in enumerate(arr):
            self.add0(num, x)

    def sum(self, i):
        s = self.tree[0]
        while i > 0:
            s += self.tree[i]
            i -= (i & -i)
        return s

    def add(self, i, a):
        if(i == 0):
            return
        while (i <= self.size):
            self.tree[i] += a
            i += (i & -i)

    def bisect_left(self, w):
        if w <= 0:
            return 0
        x = 0
        r = 1
        while (r < self.size):
            r <<= 1
        k = r
        while (k > 0):
            if x + k <= self.size and self.tree[x + k] < w:
                w -= self.tree[x + k]
                x += k
            k >>= 1
        return x + 1

    def query(self, l, r):
        return self.sum(r - 1) - self.sum(l - 1)

    def sum0(self, i):
        return self.sum(i + 1)

    def add0(self, i, a):
        self.add(i + 1, a)

    def query0(self, l, r):
        return self.sum(r) - self.sum(l)

    def __getitem__(self, item):
        _tmp = item.indices(self.size + 1)
        return [self.sum(i) - self.sum(i - 1) for i in range(_tmp[0], _tmp[1], _tmp[2])]

    def __str__(self):
        return str(self[1:self.size + 1])

# END CUT HERE


def main():
    s, b = mi()
    a = lmi()
    d = []
    g = []
    for i in range(b):
        _d, _g = mi()
        d.append(_d)
        g.append(_g)
    tmp = [(d[i], g[i]) for i in range(b)]
    tmp.sort(key=lambda x: x[0])
    d.sort()
    # print(tmp)
    # print(d)
    bit = BIT(b)
    for i in range(b):
        bit.add0(i, tmp[i][1])
    for i in range(s):
        tmp = bisect_right(d, a[i])
        # print(tmp)
        print(bit.sum(tmp), end=" ")
    print()


def __starting_point():
    main()

__starting_point()