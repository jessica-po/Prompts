MAX = 1_000_005
lp = [0] * MAX
pr = []
pid = {1: 0}
for i in range(2, MAX):
    if not lp[i]:
        lp[i] = i
        pr.append(i)
        pid[i] = len(pr)
    for p in pr:
        if p > lp[i] or i * p >= MAX:
            break
        lp[i * p] = p

n = int(input())
a = list(map(int, input().split()))

g = [[] for _ in range(len(pid))]
ec = 0
for x in a:
    f = []
    while x > 1:
        p, c = lp[x], 0
        while lp[x] == p:
            x //= p
            c ^= 1
        if c:
            f.append(p)
    if not f:
        print(1)
        import sys
        return
    f += [1] * (2 - len(f))
    u, v = pid[f[0]], pid[f[1]]
    g[u].append((v, ec))
    g[v].append((u, ec))
    ec += 1

def bfs(p):
    d = [-1] * len(pid)
    d[p] = 0
    q = [(p, -1)]
    while q:
        q2 = []
        for u, peid in q:
            for v, eid in g[u]:
                if d[v] != -1:
                    if eid != peid:
                        return d[u] + d[v] + 1
                else:
                    d[v] = d[u] + 1
                    q2.append((v, eid))
        q = q2

ans = -1
for i in range(len(pid)):
    if i > 0 and pr[i - 1] ** 2 >= MAX:
        break
    cyc = bfs(i) or ans
    if ans == -1 or cyc < ans:
        ans = cyc
print(ans)