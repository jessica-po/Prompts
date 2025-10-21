def main():
    n, k = tuple(map(int, input().split()))

    a = [set(range(n)) for _ in range(n)]

    for i in range(k):
        p = set()
        for j in map(int, input().split()):
            a[j-1] -= p
            p.add(j-1)

    sa = sorted(list(range(n)), key=lambda i: len(a[i]))
    maxx = [0] * n
    res = 0
    
    for i in sa:
        m = 1 + maxx[max(a[i], key=lambda e: maxx[e])] if a[i] else 0
        maxx[i] = m
        res = max(res, m)

    print(res)


def __starting_point():
    main()


__starting_point()