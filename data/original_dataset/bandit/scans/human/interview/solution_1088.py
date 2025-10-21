import bisect,collections,copy,heapq,itertools,math,numpy as np,string,sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    def size(self, x):
        return -self.parents[self.find(x)]
    def same(self, x, y):
        return self.find(x) == self.find(y)

N,K = LI()
a = np.array([LI() for _ in range(N)])
gyou,retu = [],[]
ans = 1
for i,j in itertools.combinations(list(range(N)),2):
    if (a[i,:]+a[j,:]<=K).all():
        gyou.append((i,j))
uf_gyou = UnionFind(N)
for x,y in gyou:
    uf_gyou.union(x,y)
for x in uf_gyou.parents:
    if x<=-2:
        for i in range(2,abs(x)+1):
            ans *= i
            ans %= 998244353
a = a.T
for i,j in itertools.combinations(list(range(N)),2):
    if (a[i,:]+a[j,:]<=K).all():
        retu.append((i,j))
uf_retu = UnionFind(N)
for x,y in retu:
    uf_retu.union(x,y)
for x in uf_retu.parents:
    if x<=-2:
        for i in range(2,abs(x)+1):
            ans *= i
            ans %= 998244353
print(ans)