#!/bin/python

n, k = list(map(int, input().split()))
p = list(map(int, input().split()))

a, b = 0, 0
for i in range(n):
    a += p[i]
    x = min(8, a)
    b += x
    a -= x
    if b >= k:
        print(i+1)
        break
else:
    print(-1)