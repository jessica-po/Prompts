import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

class RAQ_RMQ():
    def __init__(self, n, inf=2**31-1):
        self.n0 = 1<<(n-1).bit_length()
        self.INF = inf
        self.data = [0]*(2*self.n0)
        self.lazy = [0]*(2*self.n0)

    def getIndex(self, l, r):
        l += self.n0; r += self.n0
        lm = (l // (l & -l)) >> 1
        rm = (r // (r & -r)) >> 1
        while l < r:
            if r <= rm:
                yield r
            if l <= lm:
                yield l
            l >>= 1; r >>= 1
        while l:
            yield l
            l >>= 1

    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i-1]
            if not v:
                continue
            self.lazy[2*i-1] += v; self.lazy[2*i] += v
            self.data[2*i-1] += v; self.data[2*i] += v
            self.lazy[i-1] = 0

    def update(self, l, r, x):
        *ids, = self.getIndex(l, r)

        l += self.n0; r += self.n0
        while l < r:
            if r & 1:
                r -= 1
                self.lazy[r-1] += x; self.data[r-1] += x
            if l & 1:
                self.lazy[l-1] += x; self.data[l-1] += x
                l += 1
            l >>= 1; r >>= 1
        for i in ids:
            self.data[i-1] = min(self.data[2*i-1], self.data[2*i]) + self.lazy[i-1]

    def query(self, l, r):
        self.propagates(*self.getIndex(l, r))
        l += self.n0; r += self.n0

        s = self.INF
        while l < r:
            if r & 1:
                r -= 1
                s = min(s, self.data[r-1])
            if l & 1:
                s = min(s, self.data[l-1])
                l += 1
            l >>= 1; r >>= 1
        return s

n,m,k = map(int, input().split())
l = [0]*(n+1)
now = k
point = [0]*n
for i in range(n):
    a,b,c = map(int, input().split())
    point[i] = c
    now = now-a
    l[i] = now
    now += b+a
l[n] = now

RMQ = RAQ_RMQ(n+1)
for i in range(n+1):
    RMQ.update(i,i+1,l[i])

portal = list(range(n))
for i in range(m):
    u,v = map(int, input().split())
    u,v = u-1, v-1
    if portal[v]<u:
        portal[v] = u

if RMQ.query(0, n+1) < 0:
    print(-1)
    return

heap = [(-point[i], -portal[i]) for i in range(n)]
from heapq import heapify, heappop
heapify(heap)

ans = 0
while heap:
    p,i = heappop(heap)
    p,i = -p,-i
    if RMQ.query(i+1, n+1)>0:
        ans += p
        RMQ.update(i+1, n+1, -1)

print(ans)