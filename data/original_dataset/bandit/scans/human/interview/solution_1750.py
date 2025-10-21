import sys
sys.setrecursionlimit(200000)

n = int(input())
arr = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    arr[a - 1].append(b - 1)
    arr[b - 1].append(a - 1)
s = max([len(p) for p in arr]) + 1
print(s)

colored = [0] * n
def dfs(v, c, d):
    colored[v] = p = c
    for u in arr[v]:
        if not colored[u]:
            c = c + 1 if c < s else 1
            if c == d:
                c = c + 1 if c < s else 1
            dfs(u, c, p)
if s > 3:
    dfs(0, 1, 0)
else:
    i = 0
    c = 1
    while len(arr[i]) != 1:
        i += 1
    for j in range(n):
        colored[i] = c
        c = c + 1 if c < s else 1
        if j < n - 1:
            i = arr[i][0] if not colored[arr[i][0]] else arr[i][1]
print(" ".join(map(str, colored)))