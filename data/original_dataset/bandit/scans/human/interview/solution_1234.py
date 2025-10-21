#! usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
import heapq
import math
import bisect


def main():
    N, M, K = list(map(int, input().split()))
    A = list(map(int, input().split()))

    B = [(A[i], i) for i in range(N)]
    B.sort(reverse=True)

    used = [0] * N
    ans = 0
    for i in range(M*K):
        idx = B[i][1]
        used[idx] = 1
        ans += B[i][0]

    lst = []
    cnt = le = 0
    for i in range(N):
        if used[i]:
            cnt += 1
        if cnt == M:
            lst.append(i+1)
            cnt = 0
            le += 1
            if le == K - 1:
                break

    print(ans)
    print(*lst)


def __starting_point():
    main()

__starting_point()