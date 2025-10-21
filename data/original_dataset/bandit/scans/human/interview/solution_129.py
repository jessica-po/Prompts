n, m, k, l = map(int, input().split())
cnt = (k + l + m - 1) // m
if cnt * m > n:
    print(-1)
else:
    print(cnt)