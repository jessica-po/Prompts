3

MOD = 998244353

def solve(N, A):
    dp = [[0] * N for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            c = dp[i][j]

            dp[i + 1][j] += c
            dp[i + 1][j] %= MOD

            if j == 0:
                if A[i] > 0 and A[i] < N:
                    dp[i + 1][A[i]] += c
                    dp[i + 1][A[i]] %= MOD
            else:
                dp[i + 1][j - 1] += c
                dp[i + 1][j - 1] %= MOD

    return (dp[N][0] + MOD - 1) % MOD


def main():
    N = int(input())
    A = [int(e) for e in input().split(' ')]
    assert len(A) == N
    print(solve(N, A))


def __starting_point():
    main()

__starting_point()