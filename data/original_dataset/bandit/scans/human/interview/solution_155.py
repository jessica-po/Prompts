n, m, k = map(int, input().split())
ans = 0, 0
if k < n:
    ans = k + 1, 1
else:
    k -= n
    r = n - k // (m - 1)
    if r % 2:
        c = m - k % (m - 1)
    else:
        c = 2 + k % (m - 1)
    ans = r, c
print(*ans)