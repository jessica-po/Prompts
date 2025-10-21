#!/usr/bin/env python
n = int(input())
a = list(map(int, input().split()))
k = [None, 4, 8, 15, 16, 23, 42]
s = [n, 0, 0, 0, 0, 0, 0]
for ai in a:
    for i in range(6, 0, -1):
        if ai == k[i] and s[i - 1] > 0:
            s[i] += 1; s[i - 1] -= 1
            break
print(n - 6 * s[-1])