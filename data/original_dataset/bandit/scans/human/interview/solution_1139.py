from sys import stdin, stdout


def __starting_point():

    def omkar_and_last_floor(a, n, m):

        dp = [[0 for c in range(m)] for r in range(m)]

        #print(dp)
        for r in range(m):
            for l in range(r,-1,-1):
                for k in range(l, r+1):
                    cnt = 0
                    for i in range(n):
                        if l <= a[i][k][0] and a[i][k][1] <= r:
                            cnt += 1
                    lr = cnt*cnt
                    if k-1 >= l:
                        lr += dp[l][k-1]
                    if k+1 <= r:
                        lr += dp[k + 1][r]

                    dp[l][r] = max(dp[l][r], lr)
        #print(dp)
        return dp[0][m-1]


    n, m = list(map(int, stdin.readline().split()))
    a = [[[0,0] for c in range(m)] for r in range(n)]
    for i in range(n):
        k = int(stdin.readline())
        for j in range(k):
            l, r = list(map(int, stdin.readline().split()))
            for x in range(l, r+1):
                a[i][x-1][0] = l-1
                a[i][x-1][1] = r-1

    print(omkar_and_last_floor(a, n, m))


__starting_point()