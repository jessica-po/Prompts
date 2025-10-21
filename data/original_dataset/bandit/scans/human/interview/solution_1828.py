#!/usr/bin/env python3

try:
    while True:
        n = int(input())
        prev_x, prev_y = list(map(int, input().split()))
        prev_d = 0
        result = 0
        for i in range(n):
            x, y = list(map(int, input().split()))
            if y > prev_y:
                d = 0
            elif x > prev_x:
                d = 1
            elif y < prev_y:
                d = 2
            else:
                d = 3
            if ((d + 1) & 0x3) == prev_d:
                result += 1
            prev_x, prev_y = x, y
            prev_d = d
        print(result)

except EOFError:
    pass