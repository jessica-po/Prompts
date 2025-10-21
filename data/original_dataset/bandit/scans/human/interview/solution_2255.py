from heapq import *
n, m = map(int, input().split())
g = {}
for _ in range(m):
    u, v = map(int, input().split())
    g.setdefault(u, set()).add(v)
    g.setdefault(v, set()).add(u)

d = []
V = set()
h = [1]
while h:
    v = heappop(h)
    if v in V:
        continue
    V.add(v)
    d.append(v)
    for u in g[v]:
        heappush(h, u)
print(*d)