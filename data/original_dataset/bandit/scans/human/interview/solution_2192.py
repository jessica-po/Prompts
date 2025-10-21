n = int(input())
p = [list(map(int, input().split())) for i in range(n)]
t = [[0] * n for i in range(n)]
for i in range(n):
    t[i][i], p[i][i] = p[i][i], 0
    for j in range(i + 1, n):
        t[j][i] = t[i][j] = d = (p[i][j] + p[j][i]) / 2
        p[i][j] -= d
        p[j][i] -= d
for i in t: print(' '.join(map(str, i)))
for i in p: print(' '.join(map(str, i)))