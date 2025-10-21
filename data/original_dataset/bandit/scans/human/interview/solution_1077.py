#!/usr/bin/env python3

from collections import Counter

n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

tgt = n // m
b = Counter(a)
rd = sum(b[x] for x in b if x > m)
r = 0

for i in range(1, m+1):
  while rd and b[i] < tgt:
    for j in range(n):
      if a[j] > m:
        b[a[j]] -= 1
        b[i] += 1
        a[j] = i
        rd -= 1
        r += 1
        break
  while b[i] < tgt:
    for j in range(n):
      if b[a[j]] > tgt:
        b[a[j]] -= 1
        b[i] += 1
        a[j] = i
        r += 1
        break

print(tgt, r)
print(" ".join(str(x) for x in a))