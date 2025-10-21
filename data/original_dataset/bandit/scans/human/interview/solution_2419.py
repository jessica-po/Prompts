for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    d = abs(a - b)
    ans = 0
    while d > 0 or (-d) % 2 or (-d) // 2 > ans:
        ans += 1
        d = abs(d) - ans
    print(ans)