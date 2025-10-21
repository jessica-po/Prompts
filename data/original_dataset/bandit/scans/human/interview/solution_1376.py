n = int(input())
a = list(map(int, input().split()))
s = d = 0
m = {i: [] for i in range(1, n + 1)}
for i in range(n):
    m[a[i]] += [i]
for i in range(n, 2 * n):
    m[a[i]] += [i]
res = 0
for i in sorted(m):
    if s > d:
        s, d = d, s
    a, b = m[i]
    if a > b:
        a, b = b, a
    res += abs(s - a) + abs(b - d)
    s, d = a, b
print(res)