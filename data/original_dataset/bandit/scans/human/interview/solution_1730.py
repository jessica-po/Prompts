def f():
    n, m, k = map(int, input().split())
    p = [[] for i in range(n + 1)]
    for i in range(m):
        a, b = map(int, input().split())
        p[a].append(b)
        p[b].append(a)
    t, r = [0] * (n + 1), [1]
    x = t[1] = 1
    i = 0 - k
    while True:
        for y in p[x]:
            if t[y] == 2: return r[r.index(y): ]
            if t[y]: continue
            t[y], x = 1, y
            r.append(x)
            i += 1
            if i >= 0: t[r[i]] = 2
            break
t = f()
print(len(t))
print(' '.join(map(str, t)))