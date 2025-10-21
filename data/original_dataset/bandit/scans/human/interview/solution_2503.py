#!/usr/bin/env python3
# coding=utf-8

import sys

import numpy as np

n, k = list(map(int, sys.stdin.readline().strip().split(" ")))
xyc = [l.strip().split(" ") for l in sys.stdin.readlines()]
xy = [(int(_x) % (2 * k), int(_y) % (2 * k) if _c == "W" else (int(_y) + k) % (2 * k))
      for (_x, _y, _c) in xyc]

# ans = np.zeros((2 * k, 2 * k), dtype=np.int32)
ans = [[0 for j in range(2 * k + 1)] for i in range(2 * k + 1)]
for _x, _y in xy:
    if (_x - k + 0.5) * (_y - k + 0.5) > 0:
        _x %= k
        _y %= k
        ans[_x][_y] += 2
        ans[_x + k][_y] -= 2
        ans[_x][_y + k] -= 2
        ans[_x + k][_y + k] += 2
        ans[_x + k][0] += 1
        ans[0][_y + k] += 1
        ans[0][0] += 1
        ans[_x][0] -= 1
        ans[0][_y] -= 1
    else:
        _x %= k
        _y %= k
        ans[_x][_y] -= 2
        ans[_x + k][_y] += 2
        ans[_x][_y + k] += 2
        ans[_x + k][_y + k] -= 2
        ans[_x + k][0] -= 1
        ans[0][_y + k] -= 1
        ans[_x][0] += 1
        ans[0][_y] += 1
print((np.asarray(ans).cumsum(axis=1).cumsum(axis=0).max()))