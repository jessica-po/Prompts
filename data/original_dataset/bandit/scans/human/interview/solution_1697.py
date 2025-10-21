#!/usr/bin/env python

import sys

sys.setrecursionlimit(10000)

n, m = list(map(int, input().split(' ')))

def neighbors(i, j):
    return [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

def valid(i, j):
    nonlocal n, m
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    return True

def dfs(f, i, j):
    color = f[i][j]
    f[i][j] = color.lower()
    c = 0
    for n, m in neighbors(i, j):
        if valid(n, m):
            if f[n][m] == color:
                cycle_found = dfs(f, n, m)
                if cycle_found:
                    return True
            elif f[n][m] == color.lower():
                c += 1
    if c > 1:
        return True

    f[i][j] = None

    return False

f = []
for i in range(n):
    f.append(list(input().strip()))

for i in range(n):
    for j in range(m):
        if f[i][j]:
            cycle_found = dfs(f, i, j)
            if cycle_found:
                print("Yes")
                return

print("No")