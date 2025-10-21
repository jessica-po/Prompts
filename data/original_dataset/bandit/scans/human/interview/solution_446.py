from collections import Counter, defaultdict
import itertools
import sys

def main():
    n = int(input())
    ans = 1
    for k in range(1, 10):
        v = ((1 << k) - 1) * (1 << (k - 1))
        if n % v == 0:
            ans = v

    print(ans)

main()