def dfs(v, root):
    nonlocal cnt
    if used[v]:
        return
    used[v] = True
    for j in range(len(G[v])):
        to = G[v][j]
        dfs(to, root)
    if v == root:
        cnt += 1

cnt = 0
n, e = map(int, input().split())
G = [[] for i in range(n)]
for i in range(e):
    a, b = map(lambda x:int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)

used = [False for i in range(n)]
for v in range(n):
    dfs(v, v)
print(2 ** (n - cnt))