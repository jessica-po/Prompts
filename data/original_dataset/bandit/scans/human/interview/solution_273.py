from collections import *
import itertools
import sys

def main():
    a, b = input().split()
    ans = a + b
    n = len(a)
    m = len(b)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c = a[:i] + b[:j]
            # print(c)
            ans = min(ans, c)
    print(ans)

main()