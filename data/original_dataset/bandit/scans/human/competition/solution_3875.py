from itertools import permutations
from bisect import bisect_left
inf = 10 ** 18
mod = 10 ** 9 + 7


def nCr(n, r, mod=10**9+7):
    if r < 0 or r > n:
        return 0
    res = 1
    div = 1
    r = min(r, n - r)
    for i in range(r):
        res = res * (n - i) % mod
        div = div * (i + 1) % mod
    return res * pow(div, mod-2, mod) % mod


def calc_lis(A):
    L = [A[0]]
    for a in A[1:]:
        if a > L[-1]:
            L.append(a)
        else:
            L[bisect_left(L, a)] = a
    return len(L)


def enum(N, A):
    diff = [A[0]] + [r - l for l, r in zip(A[:-1], A[1:])]
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            for k in range(i - 1, j + 1):
                dp[i][j] += dp[i - 1][k] * nCr(diff[i - 1], j - k)
                dp[i][j] %= mod
    return dp[N][N]


def main():
    N = int(input())
    A = list(map(int, input().split()))

    pair = [(0,)]
    for _ in range(1, N):
        nxt = []
        for p in pair:
            v = p[-1]
            nxt.append(p + (v,))
            nxt.append(p + (v+1,))
        pair = nxt

    ans = 0
    for p in pair:
        sz = p[-1] + 1
        for order in set(permutations(p)):
            arr = [inf] * sz
            for i, a in zip(order, A):
                arr[i] = min(arr[i], a)
            for i in reversed(range(sz - 1)):
                arr[i] = min(arr[i], arr[i + 1])
            ans += enum(sz, arr) * calc_lis(order)
            ans %= mod
    for a in A:
        ans *= pow(a, mod - 2, mod)
        ans %= mod
    print(ans)


main()