import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

import numpy as np
import itertools

P = int(input())
A = [int(x) for x in input().split()]

# k,i -> i^k
power = np.ones((P,P),dtype = np.int64)
for k in range(1,P):
    power[k] = power[k-1] * np.arange(P,dtype=np.int64) % P

f = np.zeros(P,dtype=np.int64)
for i,a in enumerate(A):
    if a == 1:
        f[0] += 1
        f -= power[:,i][::-1]
f %= P

f %= P
print((*f))