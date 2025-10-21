import sys
from operator import itemgetter
readline = sys.stdin.readline

sys.setrecursionlimit(2*10**6)
class UF():
    def __init__(self, num):
        self.par = [-1]*num
        self.size = [1]*num
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            x = self.par[x]
            return self.find(x)
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.par[rx] < self.par[ry]:
                self.par[ry] = rx
                self.size[rx] += self.size[ry] 
            elif self.par[rx] > self.par[ry]:
                self.par[rx] = ry
                self.size[ry] += self.size[rx]
            else:
                self.par[rx] -= 1
                self.par[ry] = rx
                self.size[rx] += self.size[ry]
        return

def parorder(Edge, p):
    N = len(Edge)
    Cs = [None]*N
    par = [0]*N
    par[p] = -1
    stack = [p]
    order = []
    visited = set([p])
    ast = stack.append
    apo = order.append
    while stack:
        vn = stack.pop()
        apo(vn)
        for vf, cost in Edge[vn]:
            if vf in visited:
                continue
            visited.add(vf)
            par[vf] = vn
            Cs[vf] = cost
            ast(vf)
    return par, order, Cs

def getcld(p):
    res = [[] for _ in range(len(p))]
    for i, v in enumerate(p[1:], 1):
        res[v].append(i)
    return res

MOD = 10**9+7
N, M = list(map(int, readline().split()))
X = int(readline())
Edge = []
for _ in range(M):
    a, b, c = list(map(int, readline().split()))
    a -= 1
    b -= 1
    Edge.append((c, a, b))

Edge.sort(key = itemgetter(0))

T = UF(N)

cnt = 0
idx = 0
tEdge = [[] for _ in range(N)]
oEdge = []
mst = 0
while cnt < N-1:
    while True:
        cost, x, y = Edge[idx]
        rx = T.find(x)
        ry = T.find(y)
        idx += 1
        if rx != ry:
            break
        oEdge.append((cost, x, y))
    cnt += 1
    tEdge[x].append((y, cost))
    tEdge[y].append((x, cost))
    mst += cost
    T.union(x, y)
for i in range(idx, M):
    oEdge.append(Edge[i])
    

root = 0
P, L, Cs = parorder(tEdge, root)
#C = getcld(P)

Leng = [0]*N
for i in L[1:]:
    p = P[i]
    Leng[i] = 1 + Leng[p]

Dl = [list(range(N))] + [[P[i] for i in range(N)]]
depth = N.bit_length()
for _ in range(depth-1):
    res = [-1]*N
    for i in range(N):
        a = Dl[-1][i]
        if a != root and a != -1:
            res[i] = Dl[-1][a]
    Dl.append(res)

data = [[0]*N] + [[0 if i == root else Cs[i] for i in range(N)]]

for j in range(depth-1):
    res = [0]*N
    for i in range(N):
        a = Dl[j+1][i]
        if a != root and a != -1 and data[-1][a]:
            res[i] = max(data[-1][i], data[-1][a])
    data.append(res)

def query(u0, v0):
    u, v = u0, v0
    if Leng[u] > Leng[v]:
        u, v = v, u
    dif = Leng[v] - Leng[u]
    res = 0
    for i in range(dif.bit_length()):
        if (1<<i) & dif:
            res = max(res, data[i+1][v])
            v = Dl[i+1][v]
    ll = Leng[u].bit_length()
    for i in range(ll):
        k = ll-1-i
        if Dl[k+1][v] != Dl[k+1][u]:
            res = max(res, data[k+1][v], data[k+1][u])
            u = Dl[k+1][u]
            v = Dl[k+1][v]

    if u != v:
        res = max(res, Cs[v], Cs[u])
        
    return res

if mst == X:
    ans = (pow(2, N-1, MOD) - 2) * pow(2, M-(N-1), MOD) % MOD
else:
    ans = 0
cue = 0
ran = 0
dec = 0
for c, u, v in oEdge:
    me = query(u, v)
    if mst + c - me < X:
        dec += 1
    elif mst + c - me == X:
        cue += 1
    else:
        ran += 1

ans = (ans + 2*(pow(2, cue)-1)*pow(2, ran, MOD))%MOD

print(ans)