def main():
    n, m = map(int, input().split())
    res, delta = 0, 1
    while n < m:
        res += 1
        n *= 2
        delta *= 2
    while n > m:
        while n - delta >= m:
            res += 1
            n -= delta
        delta //= 2
    print(res)


def __starting_point():
    main()
__starting_point()