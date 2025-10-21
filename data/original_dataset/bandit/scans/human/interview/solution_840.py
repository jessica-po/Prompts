def can_make(a, b, k, n):
    k2 = k
    for t, v in zip(a, b):
        diff = v - t * n
        if diff < 0:
            k2 += diff

    return k2 >= 0

def main():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    lo = 0
    hi = 3 * 10**9
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if can_make(a, b, k, mid):
            lo = mid
        else:
            hi = mid

    print(lo)

main()