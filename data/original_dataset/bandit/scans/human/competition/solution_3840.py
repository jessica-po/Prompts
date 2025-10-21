3

n = int(input())
a = [0] + list(map(int, input().split()))
if len(a) < 3 or n % 2 == 0:
    print(-1)
else:
    ans = 0
    for x in range(n // 2, 0, -1):
        d = max(0, a[2 * x], a[2 * x + 1])
        ans += d
        a[x] -= d
    print(ans + max(0, a[1]))