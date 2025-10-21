D, N = list(map(int, input().split()))

ans = 0
if D == 0:
    if N % 100 != 0:
        print(N)
    else:
        print((101))
elif D == 1:
    if N % 100 != 0:
        for i in range(N):
            ans += 100**D
        print(ans)
    else:
        for i in range(N):
            ans += 100**D
        print((ans + 100))
else:
    if N % 100 != 0:
        for i in range(N):
            ans += 100**D
        print(ans)
    else:
        for i in range(N):
            ans += 100**D
        print((ans + 10000))