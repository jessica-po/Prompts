#!usr/bin/env python3
import sys
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
mod = 1000000007

def solve():
    def add(i,x):
        while i < len(bit):
            bit[i] += x
            i += i&-i
    def sum(i):
        res = 0
        while i > 0:
            res += bit[i]
            i -= i&-i
        return res
    n,m = LI()
    a = LI()
    bit = [0]*(n+m+2)
    MIN = [i+1 for i in range(n)]
    MAX = [i+1 for i in range(n)]
    f = [i+m+1 for i in range(n)]
    for i in range(n):
        add(f[i],1)
    M = m
    for i in range(m):
        ai = a[i]-1
        MIN[ai] = 1
        index = sum(f[ai])
        if MAX[ai] < index:
            MAX[ai] = index
        add(M,1)
        add(f[ai],-1)
        f[ai] = M
        M -= 1
    for i in range(n):
        index = sum(f[i])
        if MAX[i] < index:
            MAX[i] = index
    for i in range(n):
        print(MIN[i],MAX[i])
    return

#Solve
def __starting_point():
    solve()

__starting_point()