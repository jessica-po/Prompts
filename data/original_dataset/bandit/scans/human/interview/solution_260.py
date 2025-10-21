def nck(n, k, cache = {}):
    if k > n or k < 0: return 0
    if k == 0 or k == n: return 1
    if k*2 > n: k = n-k
    if (n, k) in cache: return cache[(n, k)]

    z = cache[(n, k)] = nck(n-1, k-1) + nck(n-1, k)
    return z

def bits(n):
    b = 0
    while n:
        if n&1: b += 1
        n >>= 1
    return b

def count(n, k):
    z, b, c = 0, 63, 0
    for b in reversed(range(64)):
        if (n>>b)&1:
            z += nck(b, k-c)
            c += 1
        if not k: break
    return z + (bits(n) == k)

def solve(m, k):
    lo, hi = 1, 10**18
    while lo < hi:
        mi = (lo+hi)//2
        if count(2*mi, k) - count(mi, k) < m:
            lo = mi+1
        else:
            hi = mi
    return hi

m, k = [int(x) for x in input().split()]
print(solve(m, k))