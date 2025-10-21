import sys

def solve():
    n = int(sys.stdin.readline())
    a = [0] + [int(i) for i in sys.stdin.readline().split()]

    dp = [[0]*(n + 1) for i in range(n + 1)]
    ans = 0

    maxnum = [0] * (10**5 + 2)
    maxmod = [0] * 7

    for y in range(n + 1):
        maxmod = [0] * 7

        for ai in a:
            maxnum[ai] = 0

        for i in range(y):
            maxmod[a[i] % 7] = max(maxmod[a[i] % 7], dp[i][y])
            maxnum[a[i]] = max(maxnum[a[i]], dp[i][y])

        for x in range(y + 1, n + 1):
            dp[x][y] = max(maxmod[a[x] % 7], maxnum[a[x] + 1], maxnum[a[x] - 1], dp[0][y]) + 1
            dp[y][x] = dp[x][y]
            maxmod[a[x] % 7] = max(maxmod[a[x] % 7], dp[x][y])
            maxnum[a[x]] = max(maxnum[a[x]], dp[x][y])
            ans = max(ans, dp[x][y])

    print(ans)

def __starting_point():
    solve()
__starting_point()