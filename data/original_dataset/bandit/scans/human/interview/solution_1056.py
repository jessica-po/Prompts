3

import array
from fractions import Fraction
import functools
import itertools
import math
import os
import sys


def main():
    H = [read_ints() for _ in range(10)]
    print(solve(H))


def pos_idx(x, y):
    i = y * 10
    if y % 2 == 0:
        i += x
    else:
        i += 9 - x
    return i


def idx_pos(i):
    y = i // 10
    if y % 2 == 0:
        x = i % 10
    else:
        x = 9 - i % 10
    return x, y


def solve(H):
    dp = [0] * 100
    for i in range(1, 100):
        e = 0
        for d in range(1, 7):
            j = i - d
            if j < 0:
                rem = 7 - d
                e += rem / 6
                e *= 6 / (6 - rem)
                break
            x, y = idx_pos(j)
            if H[y][x] != 0:
                dy = y - H[y][x]
                k = pos_idx(x, dy)
                assert idx_pos(k) == (x, dy)
                e += (min(dp[j], dp[k]) + 1) / 6
            else:
                e += (dp[j] + 1) / 6
        dp[i] = e
    return dp[99]


###############################################################################
# AUXILIARY FUNCTIONS

DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(e) for e in inp().split()]


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def __starting_point():
    main()

__starting_point()