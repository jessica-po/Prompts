n, up = map(int, input().split())
res = 0
for i in range(n):
    fl, t = map(int, input().split())
    res = max(res, max(t, up - fl) + fl)
print(res)