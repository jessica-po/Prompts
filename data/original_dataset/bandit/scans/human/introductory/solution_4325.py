n, x, t = list(map(int, input().split()))

ans = 0

while n > 0:
    ans += t
    n -= x

print(ans)