n, t = list(map(int,input().split()))
g = [[0.0] * i for i in range(1,n+1)]


for _ in range(t):
    g[0][0] += 1.0
    for i in range(n):
        for j in range(i+1):
            spill = max(0, g[i][j] - 1.0)
            g[i][j] -= spill
            if i < n - 1:
                g[i + 1][j] += spill / 2
                g[i + 1][j + 1] += spill / 2
    if g[n-1][0] == 1.0:
        break

cnt = 0
for i in range(n):
    for j in range(i + 1):
        if g[i][j] == 1.0:
            cnt += 1
print(cnt)