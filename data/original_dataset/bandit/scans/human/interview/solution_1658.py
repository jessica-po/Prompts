# fast io
from sys import stdin
_data = iter(stdin.read().split('\n'))
input = lambda: next(_data)

N = 101
MOD = 1000000007

def mul_vec_mat(v, a):
    c = [0] * N
    for i in range(N):
        c[i] = sum(a[j][i] * v[j] % MOD for j in range(N)) % MOD
    return c

def mul_vec_sparse_mat(v, a):
    c = [0] * N
    for i in range(N):
        c[i] = sum(x * v[j] % MOD for j, x in a[i]) % MOD
    return c

_, x = [int(v) for v in input().split()]
a = [[0] * N for i in range(N)]
a[0][0] = 1
a[N - 1][0] = 1
for i in range(1, N - 1):
    a[i][i + 1] = 1
for d in map(int, input().split()):
    a[N - 1][N - d] += 1
sa = [[] for i in range(N)]
for i in range(N):
    for j in range(N):
        if a[i][j] != 0:
            sa[j].append((i, a[i][j]))
r = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
while x > 0:
    if x & 1:
        r[0] = mul_vec_mat(r[0], a)
        r[1] = mul_vec_mat(r[1], a)
    aa = [[0] * N for i in range(N)]
    aa[0] = mul_vec_mat(a[0], a)
    aa[1] = mul_vec_mat(a[1], a)
    for i in range(2, N):
        aa[i] = mul_vec_sparse_mat(aa[i - 1], sa)
    a = aa
    x >>= 1
for i in range(2, N):
    r[i] = mul_vec_sparse_mat(r[i - 1], sa)
b = [0] * N
b[0] = 1
b[N - 1] = 1
print(sum(r[N - 1][i] * b[i] % MOD for i in range(N)) % MOD)