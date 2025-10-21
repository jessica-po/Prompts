n, x = map(int, input().split())
ans = 0
for i in range(n, 0, -1):
    if x % i == 0 and x//i <= n:
        ans += 1
print(ans)