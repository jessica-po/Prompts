a = list(map(int, input().split()))
m = max(a)

ans = 0
for i in range(3):
    if a[i] < m - 1:
        ans += (m - 1) - a[i]
        a[i] = m - 1

print(ans)