import collections as col
import itertools as its
import sys
import operator
from bisect import bisect_left, bisect_right
from copy import copy, deepcopy
from math import factorial as fact


class Solver:
    def __init__(self):
        pass

    def solve(self):
        n, t, k, d = list(map(int, input().split()))
        n = (n + k - 1) // k
        if d < (n-1) * t:
            print('YES')
        else:
            print('NO')


def __starting_point():
    s = Solver()
    s.solve()

__starting_point()