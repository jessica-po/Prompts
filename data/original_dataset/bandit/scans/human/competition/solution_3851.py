ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
from math import gcd

n, k = mi()
a, b = mi()
s = n * k

mn, mx = 10 ** 15, -1

def solve(start):
    nonlocal mn, mx
    for i in range(n):
        bef = k * i - b
        l = (bef - start) % s
        turns = s // gcd(s, l)
        mn = min(mn, turns)
        mx = max(mx, turns)
        aft = k * i + b
        l = (aft - start) % s
        turns = s // gcd(s, l)
        mn = min(mn, turns)
        mx = max(mx, turns)

solve(a)
solve(s - a)
print(mn, mx)