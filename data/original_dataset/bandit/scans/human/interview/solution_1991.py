from math import *

def r1(t):
    return t(input())

def r2(t):
    return [t(i) for i in input().split()]

for _ in range(r1(int)):
    n = r1(int)
    a = r2(int)
    g = True
    for i in range(n):
        if a[i] != i + 1:
            g = False
            break
    if g:
        print(0)
        continue

    g = True
    c = 0
    p = False
    for i in range(n):
        if a[i] != i + 1:
            if p == False:
                c += 1
                p = True
        else:
            p = False
    print(min(c, 2))