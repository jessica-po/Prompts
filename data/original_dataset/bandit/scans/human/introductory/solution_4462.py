#!/usr/bin/env python

n = int(input())
a = list(map(int, input().split()))

n2 = 0 
n4 = 0 
for i in range(n):
    if a[i]%4 == 0:
        n4 += 1
    elif a[i]%2 == 0:
        n2 += 1

ok = True
if n2 == 0:
    if n4 >= n//2:
        ok = True
    else:
        ok = False
else:
    n1 = n-n2-n4
    n1 += 1
    nn = n1+n4
    if n4 >= nn//2:
        ok = True
    else:
        ok = False

if ok: 
    print('Yes')
else:
    print('No')