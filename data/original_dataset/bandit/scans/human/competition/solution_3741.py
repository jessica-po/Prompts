from collections import deque
bits = [0] * 64
n = int(input())
data = list([x for x in map(int, input().split()) if x != 0])
n = len(data)
if n == 0:
    print(-1)
    return
for v in data:
    i = 0
    while v != 0:
        bits[i] += v & 1
        i += 1
        v >>= 1
for i in range(64):
    if bits[i] > 2:
        print(3)
        return
graph = [[] for _ in range(n)]
for u in range(n):
    for v in range(u):
        if (data[u] & data[v]) != 0 and u != v:
            graph[v].append(u)
            graph[u].append(v)


def bfs(start):
    group = [-1] * n
    depth = [0] + [-1] * (n - 1)
    for j in range(len(graph[start])):
        to = graph[start][j]
        group[to] = j
        depth[to] = 1
    bfsQ = deque(graph[start])
    minlen = 999999999
    while len(bfsQ) > 0:
        u = bfsQ[0]
        bfsQ.popleft()
        for v in graph[u]:
            if v == start:
                if depth[u] < 2:
                    continue
                return depth[u] + 1
            if group[v] == -1:
                group[v] = group[u]
                depth[v] = depth[u] + 1
                bfsQ.append(v)
            elif group[v] != group[u]:
                newlen = depth[u] + depth[v] + 1
                if newlen < minlen:
                    minlen = newlen
    return minlen


answer = min(list(map(bfs, list(range(n)))))
print(answer if answer <= n else -1)