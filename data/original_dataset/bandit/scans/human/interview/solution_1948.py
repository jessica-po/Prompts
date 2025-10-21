from collections import deque
from sys import stdin

n, x = map(int, stdin.readline().split())
leafs = set(range(n))
graph = [[] for i in range(n)]
count = [False for i in range(n)]
for i in range(n - 1):
    a, b = map(int, stdin.readline().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
    if not count[a - 1]:
        count[a - 1] = True
    else:
        leafs.discard(a - 1)
    if not count[b - 1]:
        count[b - 1] = True
    else:
        leafs.discard(b - 1)
queue = deque()
way_a = [10 ** 6 for i in range(n)]
way_b = [10 ** 6 for i in range(n)]
used = [False for i in range(n)]
queue.append([0, 0])
while queue:
    j = queue.popleft()
    way_a[j[0]] = min(way_a[j[0]], j[1])
    for i in graph[j[0]]:
        if not used[i]:
            used[i] = True
            queue.append([i, j[1] + 1])
queue.append([x - 1, 0])
used = [False for i in range(n)]
while queue:
    j = queue.popleft()
    way_b[j[0]] = min(way_b[j[0]], j[1])
    for i in graph[j[0]]:
        if not used[i]:
            used[i] = True
            queue.append([i, j[1] + 1])
res = way_a[x - 1]
for i in leafs:
    if way_a[i] > way_b[i]:
        res = max(res, way_a[i])
print(res * 2)