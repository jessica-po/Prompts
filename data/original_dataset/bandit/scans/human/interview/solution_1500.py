n, k = list(map(int, input().split()))
x = list(map(int, input().split()))

ro = list(x[i] - x[i - 1] for i in range(1, n))

if max(x[i] - x[i - 1] for i in range(1, n)) > k:
    print(-1)

else:
    ans = 1
    r = 0

    for el in ro:
        r += el

        if r > k:
            ans += 1
            r = el

    print(ans)