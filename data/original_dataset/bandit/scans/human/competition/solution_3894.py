def grundy(n, k):
    if k % 2 == 0:
        if n <= 2:
            return n
        else:
            return n % 2 == 0
    else:
        if n <= 4:
            return [0, 1, 0, 1, 2][n]
        elif n % 2 == 1:
            return 0
        else:
            return 2 if grundy(n // 2, k) == 1 else 1


def __starting_point():
    n, k = list(map(int, input().split()))
    xList = list(map(int, input().split()))
    res = 0
    for x in xList:
        res ^= grundy(x, k)
    print("Kevin" if res else "Nicky")


__starting_point()