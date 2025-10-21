n, k = map(int, input().split())
a = list(sorted(map(int, input().split())))
x = -1
if k == 0:
    x = max(1, a[0] - 1)
else:
    x = a[k - 1]
s = 0
for i in range(n):
    s += (a[i] <= x)
if s == k:
    print(x)
else:
    print(-1)