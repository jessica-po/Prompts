from fractions import Fraction
import bisect
import os
from collections import Counter
import bisect
from collections import defaultdict
import math
import random
import heapq as hq
from math import sqrt
import sys
from functools import reduce, cmp_to_key
from collections import deque
import threading
from itertools import combinations
from io import BytesIO, IOBase
from itertools import accumulate


# sys.setrecursionlimit(200000)
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def input():
    return sys.stdin.readline().strip()


def iinput():
    return int(input())


def tinput():
    return input().split()


def rinput():
    return list(map(int, tinput()))


def rlinput():
    return list(rinput())


# mod = int(1e9)+7


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


# ----------------------------------------------------
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
for _ in range(iinput()):
    n = iinput()
    a = rlinput()
    moves = 0
    i = 0
    j = n-1
    prev = 0
    ans1 = 0
    ans2 = 0
    while i <= j:
        temp = 0
        f = False
        while i<=j and i < n and temp <= prev:
            temp += a[i]
            f = True
            i += 1
        ans1 += temp
        if f:
            moves += 1
        prev = temp
        temp = 0
        f = False
        while j >= i and j > 0 and temp <= prev:
            temp += a[j]
            f = True
            j -= 1
        ans2 += temp
        if f:
            moves += 1
        prev = temp
    print(moves,ans1,ans2)