import sys
from itertools import *
from math import *
def solve():
    n,m,leftbank,rightbank = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    l = list(map(int, input().split()))
    smallx = leftbank
    leftbest, rightbest, distbest = -100, -100, 100000000
    for i, bcord, length in zip(count(), b, l):
        wanty = bcord * smallx / rightbank
        ll , rr = 0, n - 1
        while ll < rr:
            mm = (ll + rr + 1) // 2
            if a[mm] > wanty: rr = mm - 1
            else: ll = mm
        for pos in range(ll - 1, ll + 2):
            if pos >= 0 and pos < n:
                first = sqrt(smallx * smallx + a[pos] * a[pos])
                second = sqrt((rightbank -leftbank)*(rightbank - leftbank) + (bcord - a[pos])*(bcord - a[pos]))
                totaldist = first + second + length
                if totaldist < distbest:
                    distbest = totaldist
                    leftbest = pos
                    rightbest = i
    print(leftbest + 1, rightbest + 1)


if sys.hexversion == 50594544 : sys.stdin = open("test.txt")
solve()