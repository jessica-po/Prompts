n, m = map(int, input().split())
p, c = list(range(n + 1)), [1] * (n + 1)
v = [0] + list(map(int, input().split()))
s, e = 0, [()] * m
for i in range(m):
    x, y = map(int, input().split())
    e[i] = (x, y, min(v[x], v[y]))
e.sort(key = lambda x: x[2], reverse = True)
q = [[i] for i in range(n + 1)]
for l, r, v in e:
    l, r = p[l], p[r]
    if l == r: continue
    if len(q[l]) > len(q[r]): l, r = r, l
    q[r].extend(q[l])
    for t in q[l]: p[t] = r
    s += c[l] * c[r] * v
    c[r] += c[l]
print(s * 2 / (n * (n - 1)))