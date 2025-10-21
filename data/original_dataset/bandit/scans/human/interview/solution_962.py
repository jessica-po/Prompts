from collections import deque

class Graph(): #directed
    def __init__(self, n, edge, indexed=1):
        self.n = n
        self.graph = [[] for _ in range(n)]
        for e in edge:
            self.graph[e[0] - indexed].append(e[1] - indexed)

INF = 10**18

N, M = map(int, input().split())
edge = [tuple(map(int, input().split())) for _ in range(M)]

g = Graph(N, edge)

loopsize = INF

for i in range(N):
    root = i
    queue = deque([root])
    dist = [INF for _ in range(N)]
    dist[root] = 0
    prev = [None for _ in range(N)]
    while queue:
        node = queue.popleft()
        for adj in g.graph[node]:
            if adj == root: #閉路を検出する
                dist[root] = dist[node] + 1
                prev[root] = node
                break
            if dist[adj] != INF:
                continue
            dist[adj] = dist[node] + 1
            prev[adj] = node
            queue.append(adj)
        else:
            continue
        break
    else:
        continue
    #最小の閉路なら条件を満たす
    if loopsize > dist[root]:
        loopsize = dist[root]
        path = [root]
        node = root
        while prev[node] != root:
            node = prev[node]
            path.append(node)

if loopsize != INF:
    print(loopsize)
    for node in path:
        print(node + 1)
else:
    print(-1)