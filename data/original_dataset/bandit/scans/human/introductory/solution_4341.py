def connected_components(neighbors):
    seen = set()
    def component(node):
        nodes = set([node])
        while nodes:
            node = nodes.pop()
            seen.add(node)
            nodes |= neighbors[node] - seen
            yield node
    for node in neighbors:
        if node not in seen:
            yield component(node)
from collections import defaultdict
graph = defaultdict(set)
n,m = map(int,input().split())
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].add(v)
    graph[v].add(u)

total = 0
for component in connected_components(graph):
    nodes = list(component)
    size = len(nodes)
    seen = set()
    current = nodes[0]
    while len(seen) < size:
        choice = list(graph[current])
        if len(choice) != 2:break
        seen.add(current)
        possible = [c for c in choice if c not in seen]
        if not possible: break
        current = possible[0]
    if len(seen) == size:
        total+=1
print (total)