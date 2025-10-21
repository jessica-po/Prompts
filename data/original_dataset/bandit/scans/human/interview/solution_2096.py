n = int(input())
a = list(map(int, input().split()))
g = [[] for i in range(100)]
for i in range(2 * n):
    g[a[i]].append(i)
x = [0, 0]
cur = 1
mus = []
ans = [0] * 2 * n
for i in range(10, 100):
    if len(g[i]) == 1:
        ans[g[i][0]] = cur
        x[cur - 1] += 1
        cur = 3 - cur
    if len(g[i]) >= 2:
        ans[g[i][0]] = 1
        ans[g[i][1]] = 2
        x[0] += 1
        x[1] += 1
        for j in range(2, len(g[i])):
            mus.append(g[i][j])
for i in range(len(mus)):
    ans[mus[i]] = 2 - (i % 2)
print(x[0] * x[1])
print(*ans)