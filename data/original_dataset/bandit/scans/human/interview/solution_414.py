import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

class BIT_RSQ():
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+2)

    def add(self, i, v):
        while i <= self.n:
            self.data[i] += v
            i += i & -i

    def sum(self, i):
        ret = 0
        while(i > 0):
            ret += self.data[i]
            i -= i & -i
        return ret

    def query(self, l, r):
        return self.sum(r) - self.sum(l-1)

    def lowerBound(self, w):
        if w <= 0: return 0
        x, k = 0, 2**self.n.bit_length()
        while k:
            if x+k <= self.n and self.data[x+k] < w:
                w -= self.data[x+k]
                x += k
            k >>= 1
        return x + 1

n = int(input())
edges = [0]*(2*n)
c = [0]*(2*n)
BIT = BIT_RSQ(2*n)

uf = [-1]*n
def root(x):
    if uf[x] < 0:
        return x
    uf[x] = root(uf[x])
    return uf[x]
def unite(x,y):
    rx, ry = root(x), root(y)
    if rx == ry:
        return False
    if uf[rx] > uf[ry]:
        rx, ry = ry, rx
    uf[rx] += uf[ry]
    uf[ry] = rx
    return True

for i in range(n):
    a,b = list(map(int, input().split()))
    a,b = a-1,b-1
    c[a] = c[b] = i
    edges[a] = b
    edges[b] = b

for i in reversed(list(range(2*n))):
    j = edges[i]
    if j == i:
        BIT.add(j+1, 1)
    else:
        BIT.add(j+1, -1)
        cnt = BIT.sum(j+1)
        while cnt:
            k = BIT.lowerBound(cnt)
            if not unite(c[j], c[k-1]):
                print("NO")
                return
            cnt -= 1
if sum(i<0 for i in uf) == 1:
    print("YES")
else:
    print("NO")