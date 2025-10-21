ii = lambda: int(input())
mi = lambda: list(map(int, input().split()))
li = lambda: list(mi())
from bisect import bisect_left as lb, bisect_right as ub

n, k, A, B = mi()
a = li()
a.sort()

def f(l, r):
    cnt = ub(a, r) - lb(a, l)
    if cnt == 0:
        return A
    if l == r:
        return B * cnt
    m = (l + r) >> 1
    return min(B * cnt * (r - l + 1), f(l, m) + f(m + 1, r))

print(f(1, 2 ** n))