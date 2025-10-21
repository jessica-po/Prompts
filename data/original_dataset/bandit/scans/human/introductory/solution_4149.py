#!/usr/bin/env python
from collections import Counter
from math import sqrt
m = 2750131 + 100

f = list(range(m))

for d in range(2, int(sqrt(m)) + 10):
    if f[d] == d:
        i, k = 2, d << 1
        while k < m:
            if f[k] == k:
                f[k] = i
            k += d
            i += 1

np = list(range(m))
c = 1
for i in range(2, m):
    if f[i] == i:
        np[i] = c
        c += 1

n = int(input())
b = sorted(list(map(int, input().split())), reverse=True)
d = Counter(b)
a = []
i, la = 0, 0
while la < n:
    if d[b[i]] > 0:
        la += 1
        if f[b[i]] == b[i]:
            a.append(np[b[i]])
            d[b[i]] -= 1
            d[np[b[i]]] -= 1
        else:
            a.append(b[i])
            d[b[i]] -= 1
            d[f[b[i]]] -= 1
    i += 1
print(*a)