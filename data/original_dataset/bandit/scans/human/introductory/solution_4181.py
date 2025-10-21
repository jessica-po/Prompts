# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 11:20:10 2020

@author: liang
"""

N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

ans = 0
for i in range(N):
    ans += min(B[i], A[i]+A[i+1])
    if B[i] > A[i]:
        A[i+1] -= B[i] - A[i]
    if A[i+1] < 0:
        A[i+1] = 0
print(ans)