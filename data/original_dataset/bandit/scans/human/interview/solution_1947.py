# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/11/10 22:33

"""


N, M, L = list(map(int, input().split()))
A = [int(x) for x in input().split()]

ans = 0

i = 0
while i < N:
    j = i
    while j < N and A[j] > L:
        j += 1
    if j > i:
        ans += 1
        i = j + 1
    else:
        i += 1


for mi in range(M):
    line = input()
    if len(line) == 1:
        print(ans)
    else:
        t, p, d = list(map(int, line.split()))
        prev = A[p-1]
        A[p-1] += d
        if prev <= L < A[p-1]:
            if p-2 >= 0 and p < N:
                if A[p-2] > L and A[p] > L:
                    ans -= 1
                elif A[p-2] <= L and A[p] <= L:
                    ans += 1
                else:
                    pass
            elif p-2 >= 0:
                if A[p-2] > L:
                    pass
                else:
                    ans += 1
            elif p < N:
                if A[p] > L:
                    pass
                else:
                    ans += 1
            else:
                ans += 1