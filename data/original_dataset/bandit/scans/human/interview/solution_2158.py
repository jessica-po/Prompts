import sys

sys.setrecursionlimit(10**6)

ans = 0

def solve():
    n = int(input())
    Adj = [[] for i in range(n)]

    for i in range(n - 1):
        ai, bi, ci = map(int, sys.stdin.readline().split())
        Adj[ai].append((bi, ci))
        Adj[bi].append((ai, ci))

    dfs(n, Adj, -1, 0, 0)

    print(ans)

def dfs(n, Adj, p, u, cost):
    if u != 0 and len(Adj[u]) == 1:
        nonlocal ans
        ans = max(ans, cost)
        return

    for (v, c) in Adj[u]:
        if p == v:
            continue
        dfs(n, Adj, u, v, cost + c)

def __starting_point():
    solve()
__starting_point()