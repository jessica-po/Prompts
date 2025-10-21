def main():
    input()
    l = list(map(int, input().split()))
    n = max(l)
    aa = [0] * (n + 1)
    for x in l:
        aa[x] += 1
    f, x = [0] * n, 0
    for a in reversed(aa):
        x += a
        f.append(x)
    f.reverse()
    res = []
    for i, a in enumerate(aa):
        if a:
            tot, a = 0, f[i]
            for j in range(i, n + 1, i):
                b = f[j + i]
                tot += (a - b) * j
                a = b
            res.append(tot)
    print(max(res))


def __starting_point():
    main()

__starting_point()