f = lambda: map(int, input().split())
g = lambda: (a.i, b.i) if a.i < b.i else (b.i, a.i)

class T:
    def __init__(t, i):
        t.i = i
        t.s = t.v = t.u = 0
        t.p = []

n, m = f()
t = [T(i) for i in range(n + 1)]
d, l = [], []
for k in range(m):
    i, j, q = f()
    a, b = t[i], t[j]
    a.p.append(b)
    b.p.append(a)
    if q: d += [g()]
d = set(d)
x, y = [], []
a = t[1]
a.u = 1
while a.i < n:
    for b in a.p:
        v = a.v + (g() in d)
        if not b.u or b.u > a.u and v > b.v: b.v, b.s = v, a.i
        if not b.u:
            b.u = a.u + 1
            y.append(b.i)
    if not x:
        x, y = y, x
        x.reverse()
    a = t[x.pop()]
while a.i > 1:
    b = t[a.s]
    a.p.remove(b)
    b.p.remove(a)
    if g() in d: d.remove(g())
    else: l += [(a.i, b.i)]
    a = b
print(len(l) + len(d))
for a, b in l: print(a, b, 1)
for a, b in d: print(a, b, 0)