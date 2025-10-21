#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
k = int(input())

ans = 1
for i in range(n):
    if ans*2 <= (ans+k):
        ans *= 2
    else:
        ans += k
    # print(ans)
print(ans)