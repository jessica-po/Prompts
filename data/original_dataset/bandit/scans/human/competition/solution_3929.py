mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N, K = list(map(int, input().split()))

    if K == 1:
        if N == 1:
            print((1))
        else:
            print((pow(2, N - 2, mod)))
        return

    dp = [[0] * (N+1) for _ in range(K-1)]
    for j in range(2, N+1):
        dp[0][j] = 1
    for i in range(1, K-1):
        cs = [0] * (N+1)
        for j in range(1, N+1):
            cs[j] = (cs[j-1] + dp[i-1][j])%mod
        for j in range(2, N+1):
            if j != N - i + 1:
                dp[i][j] = (dp[i][j] + dp[i-1][j])%mod
            dp[i][j] = (dp[i][j] + cs[-1] - cs[j])%mod
    ans = 0
    for j in range(2, N+1):
        ans = (ans + dp[-1][j])%mod
    if K != N:
        ans = (ans * pow(2, N - K - 1, mod))%mod
    print(ans)


def __starting_point():
    main()

__starting_point()