n, m, k = input().split(' ')
n = int(n)
m = int(m)
k = int(k)
ind = []
pre = []

for _ in range(n):
    s = input()
    ind.append([])
    for i, c in enumerate(s):
        if c == '1':
            ind[-1].append(i)

for i in range(n):
    pre.append([])
    for j in range(k + 1):
        pre[i].append([])
        if len(ind[i]) > j:
            pre[i][j] = ind[i][-1] - ind[i][0] + 1
        else:
            pre[i][j] = 0
            continue
        for x in range(j + 1):
            y = len(ind[i]) - 1 - j + x

            if y >= x and ind[i][y] - ind[i][x] + 1 < pre[i][j]:
                pre[i][j] = ind[i][y] - ind[i][x] + 1
dp = [[]]

for i in range(k + 1):
    dp[0].append(pre[0][i])


for i in range(1, n):
    dp.append([])
    for j in range(0, k + 1):
        dp[i].append(pre[i][j] + dp[i - 1][0])
        for z in range(j + 1):
            dp[i][j] = min(dp[i][j], dp[i - 1][z] + pre[i][j - z])

print(dp[n - 1][k])