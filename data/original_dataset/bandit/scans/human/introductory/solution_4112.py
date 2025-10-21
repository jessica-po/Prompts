n, k, x = list(map(int, input().split()))
a = [None] + list(map(int, input().split()))

lo, hi = 0, 10 ** 9 * 5000
q = [None] * (n + 1)

def get(mid):
    f, r = 0, 0
    q[0] = 0, 0, 0
    for i in range(1, n + 1):
        if q[r][2] == i - k - 1: r += 1
        cur = q[r][0] + a[i] - mid, q[r][1] + 1, i
        while r <= f and q[f] <= cur: f -= 1
        f += 1
        q[f] = cur
    if q[r][2] == n - k: r += 1
    return q[r]

while lo < hi:
    mid = (lo + hi + 1) >> 1
    _, cnt, _ = get(mid)
    if cnt >= x:
        lo = mid
    else:
        hi = mid - 1

sm, _, _ = get(lo)
ans = max(-1, sm + x * lo)
print(ans)