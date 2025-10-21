import sys
def solve():
    readline = sys.stdin.readline
    write = sys.stdout.write
    MOD = 998244353

    N = int(readline())
    P = [list(map(int, readline().split())) for i in range(N)]

    P.sort()

    Y = [y for x, y in P]

    def compress(X):
        *XS, = set(X)
        XS.sort()
        return list(map({e: i for i, e in enumerate(XS)}.__getitem__, X))
    Y = compress(Y)

    data = [0]*(N+1)
    def add(k, x):
        while k <= N:
            data[k] += x
            k += k & -k
    def get(k):
        s = 0
        while k:
            s += data[k]
            k -= k & -k
        return s

    pow2 = [1]*(N+1)
    r = 1
    for i in range(1, N+1):
        pow2[i] = r = r * 2 % MOD

    def gen(add, get, pow2):
        for i, y in enumerate(Y):
            v = get(y+1); add(y+1, 1)
            p1 = pow2[v]; p0 = pow2[y - v]
            q1 = pow2[i - v]; q0 = pow2[(N - y - 1) - (i - v)]
            yield (p0 + p1 + q0 + q1 - (p0 + q1) * (p1 + q0)) % MOD
    write("%d\n" % ((sum(gen(add, get, pow2)) + N*pow2[N] - N) % MOD))
solve()