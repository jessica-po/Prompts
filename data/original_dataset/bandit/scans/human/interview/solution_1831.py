3

__import__("sys").setrecursionlimit(10 ** 6)

def dfs(u, tr, used):
    used[u] = True
    ans = 1
    for v in tr[u]:
        if not used[v]:
            ans += dfs(v, tr, used)
    return ans


n, m = list(map(int, input().split()))
if n != m + 1:
    print("no")
    return

tr = [[] for i in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    tr[a].append(b)
    tr[b].append(a)

used = [False] * n
if dfs(0, tr, used) == n:
    print("yes")
else:
    print("no")