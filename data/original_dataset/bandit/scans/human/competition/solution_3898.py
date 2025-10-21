#!/usr/bin/env python3
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if n <= 3:
    print('YES')
else:
    a.remove(0)
    b.remove(0)
    i = a.index(1)
    a = a[i:] + a[:i]
    i = b.index(1)
    b = b[i:] + b[:i]
    print(['NO','YES'][a == b])