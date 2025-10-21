def main():
    from math import sqrt
    m, n, k = list(map(int, input().split()))
    if n < m:
        n, m = m, n
    lo, hi = 1, k + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        t = mid - 1
        v = min(int(sqrt(t)), m)
        tn, tm = (t - 1) // m, t // n
        vv = [t // i for i in range(tm + 1, v + 1)]
        if t // n * (n + m) + sum(vv) * 2 + max(min((tn - tm), len(vv)) * m, 0) - v * v - sum(
                vv[:max(min(tn - tm, len(vv)), 0)]) < k:
            lo = mid
        else:
            hi = mid
    print(lo)


def __starting_point():
    main()

__starting_point()