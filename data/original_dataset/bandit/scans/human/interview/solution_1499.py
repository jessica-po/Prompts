#!/usr/bin/env python3

OUT = (1, 0, 2, 3)

try:
    while True:
        n, m = map(int, input().split())
        bus = [[None] * 4 for i in range(n)]
        cur = 1
        for row in range(n << 1):
            if row >= n:
                i = row - n
                k = b = 1
            else:
                i = row
                k = 3
                b = 0
            for j in range(2):
                if cur <= m:
                    bus[i][k * j + b] = cur
                    cur += 1
        for i in range(n):
            for j in range(4):
                if bus[i][OUT[j]] is not None:
                    print(bus[i][OUT[j]], end=' ')
        print()

except EOFError:
    pass