#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict

n = int(input())
A = list(map(int,input().split()))
pattern = set()
for a in A:
    p = []
    while a > 0:
        if a in pattern:
            break
        p.append(a)
        a = a//2
    pattern |= set(p)

def check(v):
    ret = 0
    for a in A:
        count = 0
        while a != 0:
            if v == a or (v % a == 0 and (v//a)&-(v//a) == v//a):
                ret += len(bin(v//a))-3
                break
            if (v%a == 0 and (v//a)&-(v//a) == v//a) and a < v:
                return 1e12
            a = a//2
            ret += 1
        else:
            return 1e12
    return ret

ans = 1e12
for p in pattern:
    ret = check(p)
    ans = ans if ans < ret else ret
print(ans)