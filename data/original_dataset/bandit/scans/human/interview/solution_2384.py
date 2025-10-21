def main():
    import sys
    import numpy as np
    def input(): return sys.stdin.readline().rstrip()
    n = int(input())
    a = list(map(int, input().split()))
    inf = 1e18
    k = n%2 + 1
    dp = np.full((n+1, k+2), -inf, dtype=int)
    dp[0,0] = 0
    for i in range(n):
        for j in range(k+1):
            dp[i+1, j+1] = max(dp[i+1,j+1],dp[i,j])
            now = dp[i,j]
            if (i+j)%2 == 0: now += a[i]
            dp[i+1,j] = max(dp[i+1,j],now)
    print(dp[n,k])

def __starting_point():
    main()
__starting_point()