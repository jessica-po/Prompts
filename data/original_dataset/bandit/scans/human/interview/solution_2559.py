import sys


# inf = open('input.txt', 'r')
# reader = (map(int, line.split()) for line in inf)
reader = (list(map(int, line.split())) for line in sys.stdin)

def minmaxPairs(g, costDict, n):
    G = B = 0
    s = 1
    stack = [s]
    traversal = []
    visited = [False] * (n + 1)
    subtreeSize = [1 for _ in range(n + 1)]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            for to in g[v]:
                if not visited[to]:
                    stack.append(v)
                    stack.append(to)
        else:
            to = traversal[-1]
            if (v, to) in costDict:
                cost = costDict[(v, to)]
            else:
                cost = costDict[(to, v)]
            toSize = subtreeSize[to]
            subtreeSize[v] += toSize
            minComp = min(toSize, n - toSize)
            G += (minComp % 2) * cost
            B += minComp * cost
        traversal.append(v)
    return G, B 

t, = next(reader)
for _ in range(t):
    k, = next(reader)
    n = 2 * k
    g = [[] for i in range(n + 1)]
    costDict = {}
    for i in range(n - 1):
        v, to, cost = next(reader)
        costDict[(v, to)] = cost
        g[v].append(to)
        g[to].append(v)
    G, B = minmaxPairs(g, costDict, n)
    print(G, B)

# inf.close()