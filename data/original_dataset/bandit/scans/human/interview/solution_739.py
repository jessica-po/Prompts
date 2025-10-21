import copy
import sys

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

L,A,B,mod = na()

low = 1
high = 10


def matpow(M, v, e, mod):
    A = copy.deepcopy(M)
    w = copy.deepcopy(v)
    while e > 0:
        if e&1:
            w = mulv(A, w, mod)
        A = mul(A, A, mod)
        e >>= 1
    return w


def mulv(M, v, mod):
    n = len(M)
    m = len(v)
    ret = [0] * n
    for i in range(n):
        s = 0
        for j in range(m):
            s += M[i][j] * v[j]
        ret[i] = s % mod
    return ret


def mul(A, B, mod):
    n = len(A)
    m = len(B)
    o = len(B[0])
    ret = [[0] * o for _ in range(n)]
    for i in range(n):
        for j in range(o):
            s = 0
            for k in range(m):
                s += A[i][k] * B[k][j]
            ret[i][j] = s % mod
    return ret


# x = x * high + val
# val += B
# (high 1 0)
# (0 1 1)
# (0 0 1)

v = [0, A, B]
ra = A

while low < 1e18:
    mat = [[high%mod, 1, 0], [0, 1, 1], [0, 0, 1]]
    step = max(0, min(L, (high-ra+B-1)//B))
    v = matpow(mat, v, step, mod)
    # print(low, high, step, ra + B*step, v)
    ra = ra + B * step
    L -= step

    low *= 10
    high *= 10

print((v[0]))