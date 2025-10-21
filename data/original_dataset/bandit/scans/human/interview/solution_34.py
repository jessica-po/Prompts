n, a, b = map(int, input().split())
ans = 0
for i in range(1, n):
    ans = max(ans, min(a // i, b // (n - i)))
print(ans)