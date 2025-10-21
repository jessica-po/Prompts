for i in range(int(input())):
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    ans = d
    for day in range(n - d + 1):
        ans = min(ans, len(set(a[day:day + d])))
    print(ans)