import sys
from collections import defaultdict, Counter

P = 10 ** 9 + 7

def factmod(n):
    res = 1
    for i in range(2, n+1):
        res *= i
        res %= P

    return res

def solve():
    n, m = list(map(int, input().split()))
    colour = {i:0 for i in range(1, m+1)}
    colour_map = {}
    for i, line in enumerate(sys.stdin):
        A = [int(x) for x in line.split()]
        count = Counter(A)

        if count[A[0]] == 1:
            count.pop(A[0])
        else:
            count[A[0]] -= 1

        for c in count:
            p = (colour[c], i, count[c])
            if p in colour_map:
                colour[c] = colour_map[p]
            else:
                colour[c] = colour_map[p] = len(colour_map) + 1

    count = Counter(list(colour.values()))

    res = 1
    for c in count:
        res *= factmod(count[c])
        res %= P

    return res

print(solve())