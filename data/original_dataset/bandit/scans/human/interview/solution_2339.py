import sys
input = sys.stdin.readline

from math import gcd

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    g = max(l)
    out = []
    while l:
        nex = max((gcd(g,l[i]), i) for i in range(len(l)))
        out.append(l.pop(nex[1]))
        g = nex[0]
    print(' '.join(map(str,out)))