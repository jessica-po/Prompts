import numpy as np
def f(b, n):
    s = 0
    while n > 0:
        s += n % b
        n //= b
    return s

INF = 10**15
def solve(n, s):
    if n == s:
        return n+1
    m = int(np.sqrt(n)) + 1
    for b in range(2, m+1):
        if f(b, n) == s:
            return b
    best = INF
    for p in range(1, m+10):
        q = s - p
        b = (n - q) // p
        if (b > p) and (b > q) and (f(b, n) == s):
            best = min(best, b)
    return -1 if (best == INF) else best

n = int(input())
s = int(input())
print(solve(n, s))