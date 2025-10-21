n = int(input())
c, d = {}, {}
for x, y in zip(input().split(), input().split()):
    c[x] = c.get(x, 1) + 1
    c[y] = c.get(y, 1) + 1
    if x == y: d[x] = d.get(x, 0) + 2
s, m = 1, int(input())
for k, v in c.items():
    u = d.get(k, 0)
    for i in range(v - u, v, 2): s = s * (i * i + i) // 2 % m
    for i in range(1, v - u): s = s * i % m
print(s)