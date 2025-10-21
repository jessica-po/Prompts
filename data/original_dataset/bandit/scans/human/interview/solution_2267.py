#!/usr/bin/env python3

from functools import cmp_to_key
def cmpEqLen(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

def compare(a, b):
    alen = len(a)
    blen = len(b)
    if alen == blen:
        return cmpEqLen(a, b)
    l = min(alen, blen)
    c = cmpEqLen(a[:l], b[:l])
    if c != 0:
        return c

    if alen > blen:
        return -compare(a[:l], a[l:])
    else:
        return compare(b[:l], b[l:])

N = int(input())
arr = [input() for _ in range(N)]
arr.sort(key=cmp_to_key(compare))
print(''.join(arr))