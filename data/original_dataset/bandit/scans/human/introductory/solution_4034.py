from collections import deque
n = int(input())
s = input()
graph = {}
for i in range(n):
    graph[i] = set()
rb = set()
for i in range(n):
    for j in range(i + 1, n):
        if s[i] > s[j]:
            graph[i].add(j)
            graph[j].add(i)
            rb.add((i, j))
            rb.add((j, i))
group = [0] * n
used = [0] * n
for p in range(n):
    if not used[p]:
        used[p] = 1
        q = deque([p])
        group[p] = 0
        while q:
            v = q.popleft()
            for u in graph[v]:
                if not used[u]:
                    used[u] = 1
                    q.append(u)
                    group[u] = 1 - group[v]
g1, g2 = set(), set()
for i in range(n):
    if group[i] == 0:
        g1.add(i)
    else:
        g2.add(i)
for p in g1:
    for p2 in g1:
        if (p, p2) in rb:
            print('NO')
            return
for p in g2:
    for p2 in g2:
        if (p, p2) in rb:
            print('NO')
            return
print('YES')
for i in range(n):
    if i in g1:
        print('0', end='')
    else:
        print('1', end='')