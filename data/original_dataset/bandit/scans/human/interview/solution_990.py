from collections import defaultdict


def dfs(s, t):
    visited = 0
    q = [(s, 0)]
    while q:
        v, used = q.pop()
        if v == t:
            return used
        visited |= used
        for lb, u in graph[v]:
            if lb & visited:
                continue
            q.append((u, used | lb))


n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    lb = 1 << i
    graph[a].append((lb, b))
    graph[b].append((lb, a))

conditions = []
m = int(input())
for i in range(m):
    u, v = list(map(int, input().split()))
    conditions.append(dfs(u, v))

link_conditions = [int(''.join(b), 2) for b in zip(*list(map(('{:0' + str(n - 1) + 'b}').format, conditions)))]

dp = defaultdict(int)
dp[0] = 1
for lc in link_conditions:
    for fulfilled, pattern in list(dp.items()):
        dp[fulfilled | lc] += pattern
print((dp[(1 << m) - 1]))