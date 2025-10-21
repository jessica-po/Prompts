#!/usr/bin/env python3

from bisect import bisect

try:
    while True:
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort()
        for x in map(int, input().split()):
            print(bisect(a, x), end=' ')
        print()

except EOFError:
    pass