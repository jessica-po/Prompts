#!/usr/bin/env python3

try:
    while True:
        n = int(input())
        b = list(map(int, input().split()))
        cur = 0
        result = 0
        for x in b:
            result += abs(cur - x)
            cur = x
        print(result)
except EOFError:
    pass