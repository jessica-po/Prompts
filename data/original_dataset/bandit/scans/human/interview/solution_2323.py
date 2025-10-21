import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return tuple(map(int, sys.stdin.readline().split()))
def LLI(): return [tuple(map(int, l.split())) for l in sys.stdin]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

def main():
    n = I()
    a = sorted(LI())
    q = I()
    b = []
    for _ in range(q):
        l,r = LI()
        b.append(r-l+1)
    c = []
    for i in range(n-1):
        c.append(a[i+1]-a[i])
    c.sort()
    c.append(inf)

    d = sorted(b)
    e = {}
    s = 0
    t = n
    ci = 0
    for k in d:
        while c[ci] <= k:
            t -= 1
            s += c[ci]
            ci += 1
        e[k] = s + k * t

    rr = [e[k] for k in b]

    return ' '.join(map(str, rr))

print(main())