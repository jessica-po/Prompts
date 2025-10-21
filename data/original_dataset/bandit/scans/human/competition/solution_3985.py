def g(i):
    u[i] = 0
    for j in p[i]:
        if v[j] < 0 or u[v[j]] and g(v[j]):
            v[j] = i
            return 1
    return 0

f = lambda: map(int, input().split())
n, m = f()
s = k = 0
d = [[]]
for i in f():
    j = 2
    t = []
    while j * j <= i:
        while i % j == 0:
            t.append((j, k))
            k += 1
            i //= j
        j += 1
    if i > 1:
        t.append((i, k))
        k += 1
    d.append(t)
p = [[] for i in range(k)]
for q in range(m):
    a, b = f()
    if b % 2: a, b = b, a
    for x, i in d[a]:
        for y, j in d[b]:
            if x == y: p[i].append(j)
v = [-1] * k
for i in range(k):
    u = [1] * k
    s += g(i)
print(s)