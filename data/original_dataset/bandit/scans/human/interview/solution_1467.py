import sys
from math import *
from fractions import gcd
readints=lambda:list(map(int, input().strip('\n').split()))

n=int(input())
arr = list(readints())

pref=0
basis=[]

for v in arr:
    pref = pref^v
    for b in basis:
        v = min(v, v^b)
    if v>0:
        basis.append(v)


if pref==0:
    print(-1)
else:
    print(len(basis))