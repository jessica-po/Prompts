3

n, m, k = tuple(map(int, input().split()))
a = reversed(sorted(map(int, input().split())))

ans = 0
for _ in a:
    if m <= k:
        break
    ans += 1
    m -= k - 1
    k = _
print(ans if m <= k else -1)