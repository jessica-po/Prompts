#!/usr/bin/env python3

from fractions import Fraction

def __starting_point():
    p, q = list(map(int, input().split()))
    n = int(input())
    l = list(map(int, input().split()))

    f = Fraction(l[-1], 1)

    for x in l[-2::-1]:
        f = 1 / f
        f += x

    print(["NO", "YES"][f == Fraction(p, q)])



__starting_point()