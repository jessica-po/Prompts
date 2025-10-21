def solve():
    N, X, D = list(map(int, input().split()))

    if D == 0:
        if X == 0:
            print((1))
        else:
            print((N+1))
        return

    LRss = {}
    for k in range(N+1):
        m = X*k
        rem = m%D
        minCoef = m//D + k*(k-1)//2
        maxCoef = m//D + k*(2*N-k-1)//2
        if rem not in LRss:
            LRss[rem] = [(minCoef, maxCoef)]
        else:
            LRss[rem].append((minCoef, maxCoef))

    ans = 0
    for rem, LRs in list(LRss.items()):
        LRs.sort()
        LNow, RNow = LRs[0]
        for L, R in LRs[1:]:
            if L <= RNow:
                if R > RNow:
                    RNow = R
            else:
                ans += RNow - LNow + 1
                LNow, RNow = L, R
        ans += RNow - LNow + 1

    print(ans)


solve()