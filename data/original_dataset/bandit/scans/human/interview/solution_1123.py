import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
mod2 = 998244353
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)



class Prime():
    def __init__(self, n):
        self.M = m = int(math.sqrt(n)) + 10
        self.A = a = [True] * m
        a[0] = a[1] = False
        self.T = t = [2]
        for j in range(4, m, 2):
            a[j] = False
        for i in range(3, m, 2):
            if not a[i]:
                continue
            t.append(i)
            for j in range(i*i,m,i):
                a[j] = False
        self.ds_memo = {}
        self.ds_memo[1] = set([1])

    def is_prime(self, n):
        return self.A[n]

    def division(self, n):
        d = collections.defaultdict(int)
        for c in self.T:
            while n % c == 0:
                d[c] += 1
                n //= c
            if n < 2:
                break
        if n > 1:
            d[n] += 1
        return d.items()

    # memo
    def divisions(self, n):
        if n in self.ds_memo:
            return self.ds_memo[n]

        for c in self.T:
            if n % c == 0:
                rs = set([c])
                for cc in self.divisions(n // c):
                    rs.add(cc)
                    rs.add(cc * c)
                self.ds_memo[n] = rs
                return rs

        rs = set([1, n])
        self.ds_memo[n] = rs
        return rs

def main():
    n,k = LI()
    pr = Prime(10**5)
    c = collections.defaultdict(int)
    for i in range(k, 0, -1):
        t = k // i
        p = (pow(t, n, mod) + c[i]) % mod
        ds = pr.divisions(i)
        for kk in ds:
            if kk == i:
                continue
            c[kk] -= p
        c[i] = p

    r = sum(k*v%mod for k,v in c.items()) % mod

    return r

print(main())