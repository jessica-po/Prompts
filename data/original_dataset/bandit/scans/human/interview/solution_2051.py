from collections import defaultdict

n, m, k = [int(x) for x in input().split()]
c = [0] + [int(x) for x in input().split()]
g = defaultdict(lambda: [])
for i in range(m):
    l, r = [int(x) for x in input().split()]
    g[l].append(r)
    g[r].append(l)
done = [0] * (1 + n)
ans = 0
for i in range(n):
    i += 1
    if done[i]:
        continue
    q = [i]
    p = 0
    mn = set([i])
    mcx = defaultdict(lambda: 0)
    while p != len(q):
        t = q[p]
        p += 1
        if done[t]:
            continue
        done[t] = 1
        mcx[c[t]] += 1
        mn.add(t)
        for ne in g[t]:
            q.append(ne)
    fcol = None
    maxn = -1
    for col, num in list(mcx.items()):
        if num >= maxn:
            maxn = num
            fcol = col
    if fcol:
        for ob in mn:
            if c[ob] != fcol and len(g[ob]) > 0:
                c[ob] = fcol
                ans += 1
print(ans)