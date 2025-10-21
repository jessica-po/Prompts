import sys
import collections
rlines = sys.stdin.readlines()
lines = (l.strip() for l in rlines)

def eucycle(n,m,adj):
    diredges = []
    us = list(adj.keys())
    for u in us:
        while adj[u]:
            v0 = u
            v1 = adj[v0].pop()
            adj[v1].remove(v0)
            diredges.append((v0,v1))
            while v1 != u:
                v0 = v1
                v1 = adj[v0].pop()
                adj[v1].remove(v0)
                diredges.append((v0,v1))
    return diredges

def solve(n,m,edges):
    adj = collections.defaultdict(set)
    diredges = []
    for u,v in edges:
        adj[u].add(v)
        adj[v].add(u)
    odds = set(u for u in adj if len(adj[u])%2 == 1)
    ans = n - len(odds)
    assert(len(odds)%2 == 0)
    for o in odds:
        adj[n+1].add(o)
        adj[o].add(n+1)
    diredges = eucycle(n+1,m,adj)
    return str(ans) + '\n' + '\n'.join(str(u) + ' ' + str(v) for (u,v) in diredges\
            if u != n+1 and v != n+1)


t = int(next(lines))

for ti in range(t):
    n,m = [int(s) for s in next(lines).split()]
    edges = []
    for ei in range(m):
        u,v = [int(s) for s in next(lines).split()]
        edges.append((u,v))
    #print(edges)
    print(solve(n,m,edges))