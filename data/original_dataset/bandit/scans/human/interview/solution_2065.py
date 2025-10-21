n, m = map(int, input().split())
adj = [[] for _ in range(n)]
cp = [-1] * n

for i in range(m):
    p, c = map(int, input().split())
    adj[p - 1].append(c - 1)
    cp[c - 1] = p - 1

pres = [i - 1 for i in map(int, input().split())]

level = [0] * n
from collections import deque
def bfs(v):
    q = deque([v])
    while q:
        v = q.pop()
        if cp[v] >= 0:
            level[v] = level[cp[v]] + 1
        for nv in adj[v]:
            q.append(nv)

for i in range(n):
    if cp[i] == -1:
        bfs(i)

for i in range(n):
    if level[i] > 0:
        par = cp[i]
        if pres[i] != pres[par] and level[pres[i]] <= level[par]:
            print(-1)
            return

pres = list(set(pres))
pres = sorted(pres, key = lambda i : level[i], reverse = True)

print(len(pres))
pres = [i + 1 for i in pres]
print("\n".join(map(str, pres)))