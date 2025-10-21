import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
M = [[0 for i in range (0, 21)] for j in range (0, 21)]
F = [0 for i in range (0, 21)]
for i in range (0, n):
    x = int(a[i])
    for j in range (0, 21):
        if j != x:
            M[j][x] = M[j][x] + F[j]
    F[x] = F[x] + 1
ans = 0
for i in range (0, 21):
    for j in range (0, i):
        ans = ans + min(M[i][j], M[j][i])
print(ans)