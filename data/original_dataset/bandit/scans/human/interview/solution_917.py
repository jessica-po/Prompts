n, h, m = map(int, input().split())
a = [h] * n
for i in range(m):
    l, r, x = map(int, input().split())
    for i in range(l - 1, r):
        a[i] = min(a[i], x)
s = 0
for i in range(n):
    s += a[i] ** 2
print(s)