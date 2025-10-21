def main():
    n, a, z = int(input()), 0, 10 ** 10
    b, *cc = list(map(int, input().split()))
    dp = [(0, z, z), (z, 0, z), *[(z, z, z)] * ((n - 1) // 2)]
    for i, c in enumerate(cc, 1):
        u, v, w = dp[i // 2 + 1]
        dz = max(0, c - b + 1)
        du = max(0, b - c + 1)
        dw = max(0, min(a - 1, b) - c + 1)
        for j in range(i // 2, -1, -1):
            x, y, z = u, v, w
            u, v, w = dp[j]
            dp[j + 1] = (x if x < z else z, min(u + du, w + dw), y + dz)
        a, b = b, c
    print(' '.join(map(str, list(map(min, dp[1:])))))


def __starting_point():
    main()

__starting_point()