n0, n1, x, y = list(map(int, input().split()))

def f(m, n, x, y):
    return max(0, n - (m // y - m // (x * y)))

lo = -1
hi = x * y * (n0 + n1)
while lo + 1 < hi:
    mid = lo + (hi - lo) // 2
    if f(mid, n0, x, y) + f(mid, n1, y, x) <= mid - mid // x - mid // y + mid // (x * y):
        hi = mid
    else:
        lo = mid
print(hi)