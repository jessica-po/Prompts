# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:04:24 2020

@author: liang
"""

W, H, x, y = map(int, input().split())

ans = [0] * 2

ans[0] = H*W/2
if x == W/2 and y == H/2:
    ans[1] = 1
else:
    ans[1] = 0
print(" ".join(map(str, ans)))