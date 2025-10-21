# = map(int, input().split())
n, m = list(map(int, input().split()))
ans = 10 ** 100
for i in range(n):
    p, q = list(map(int, input().split()))
    ans = min(ans, p / q * m)
print(ans)