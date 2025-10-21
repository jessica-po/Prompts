import itertools
import math

def minusv(L):
    return [-x for x in L]

def adamar(M):
    return [L*2 for L in M] + [L + minusv(L) for L in M]

k = int(input())
a = [[1]]
for i in range(k):
    a = adamar(a)
for L in a:
    print(''.join(['+' if c==1 else '*' for c in L]))