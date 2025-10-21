from math import factorial
cat = [1, 1]
p = 10**9 + 7
n = int(input())
ans = 0
fac = [1]
mat = [[0 for i in range(n + 1)] for j in range(n + 1)]


mat[0][0] = 1
for i in range(1, n + 1):
    mat[i][0] = mat[i - 1][i - 1]
    for j in range(i):
        mat[i][j + 1] = (mat[i][j] + mat[i - 1][j]) % p

print(mat[n][n - 1] % p)