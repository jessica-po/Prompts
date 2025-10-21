from collections import defaultdict, deque

class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [0 for i in range(n)]

    def find_parent(self, v):
        if self.parents[v] == v:
            return v
        self.parents[v] = self.find_parent(self.parents[v])
        return self.parents[v]

    def join_sets(self, u, v):
        u = self.find_parent(u)
        v = self.find_parent(v)
        if u != v:
            if self.ranks[u] < self.ranks[v]:
                u, v = v, u
            self.parents[v] = u
            if self.ranks[v] == self.ranks[u]:
                self.ranks[u] += 1

n = int(input())
dsu = DSU(n)
colors = list(map(int, input().split(' ')))
vertices = []
for i in range(n-1):
    u, v = [int(x)-1 for x in input().split(' ')]
    if colors[u] == colors[v]:
        dsu.join_sets(u, v)
    vertices.append((u,v))
graph = defaultdict(list)
for u, v in vertices:
    if colors[u] != colors[v]:
        u = dsu.find_parent(u)
        v = dsu.find_parent(v)
        graph[u].append(v)
        graph[v].append(u)


def bfs(u):
    d = dict()
    d[u] = 0
    q = deque()
    q.append(u)
    while q:
        u = q.pop()
        for v in graph[u]:
            if v not in d:
                d[v] = d[u] + 1
                q.append(v)
    return d
if graph:
    v = list(graph.keys())[0]
    d = bfs(v)
    u = v
    for i in d:
        if d[i] > d[u]:
            u = i
    d = bfs(u)
    w = u
    for i in d:
        if d[i] > d[w]:
            w = i
    print((d[w]+1)//2)
else:
    print(0)