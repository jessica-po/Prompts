#!/usr/bin/env python3

from collections import Counter

try:
    while True:
        n = int(input())
        s = input()
        if n > 26:
            print(-1)
        else:
            c = Counter(s)
            print(sum(c.values()) - len(c))

except EOFError:
    pass