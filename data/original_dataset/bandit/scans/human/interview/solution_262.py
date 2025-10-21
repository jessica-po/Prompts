#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func():
    N = int(input())
    cells = [0] * N

    if N == 1:
        return 1

    mx = 0
    for n in range(N):
        cells[n] = list(map(int,input().split()))
        mx = max(mx, sum(cells[n]))

    ans = None
    for j in range(N):
        for i in range(N):
            if cells[j][i] == 0:
                ans = mx - sum(cells[j])
                cells[j][i] = ans
                if ans <= 0:
                    return -1

    # validation
    for j in range(N):
        if sum(cells[j]) != mx:
            return -1
    for i in range(N):
        if mx != sum([cells[j][i] for j in range(N)]):
            return -1
    if mx != sum([cells[j][j] for j in range(N)]):
        return -1
    if mx != sum([cells[j][N-1-j] for j in range(N)]):
        return -1
    
    return ans

print(func())