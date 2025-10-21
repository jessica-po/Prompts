def dfs(v, x, y, t, l, pr):
    ans[v] = x, y
    nx = [(l, 0), (0, -l), (-l, 0), (0, l)]
    if t == 0: p = 0, 1, 3
    if t == 1: p = 0, 1, 2
    if t == 2: p = 1, 2, 3
    if t == 3: p = 0, 2, 3
    listv = [u for u in g[v] if u != pr]
    g[v] = listv[:]
    for i in range(min(len(p), len(g[v]))):
        dx = nx[p[i]][0]
        dy = nx[p[i]][1]
        newx = x + dx
        newy = y + dy
        u = g[v][i]
        dfs(u, newx, newy, p[i], l // 4, v)

read = lambda: map(int, input().split())
n = int(input())
g = [list() for i in range(n + 1)]
for i in range(n - 1):
    u, v = read()
    g[u].append(v)
    g[v].append(u)
def fail():
    print('NO')
    return
root = 1
for i in range(n + 1):
    if len(g[i]) > 4:
        fail()
    if len(g[i]) > len(g[root]):
        root = i
ans = [0] * (n + 1)
ans[root] = (0, 0)
inf = 10 ** 18
l = inf // 4
nx = [(l, 0), (0, -l), (-l, 0), (0, l)]
for i in range(len(g[root])):
    dx = nx[i][0]
    dy = nx[i][1]
    newx = 0 + dx
    newy = 0 + dy    
    dfs(g[root][i], newx, newy, i, l // 4, root)
print('YES')
[print(*i) for i in ans[1:]]