def rec(i):
    nonlocal a
    return i
import sys
from collections import Counter
sys.setrecursionlimit(10**6)
n=int(input())
#n,m=list(map(int,input().split()))
a=[input() for i in range(n)]
b=[]
a0=set()
c0=set()
for i in a:
    c=set()
    for i0 in range(1,10):
        for i1 in range(0,10-i0):
            c.add(i[i1:i1+i0])
    b.append(c)
    c0.update(a0&c)
    a0.update(c)

for i in b:
    c=i-c0
    z='0'*10
    for i0 in c:
        if len(i0)<len(z):
            z=i0
    print(z)