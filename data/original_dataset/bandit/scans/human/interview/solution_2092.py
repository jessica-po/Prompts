from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

M,N,K,T = inpl()
AA = inpl()

DD_di = []
LR = []
for i in range(K):
    L,R,D = inpl()
    LR.append((L,R))
    DD_di.append((D,i))

DD_di.sort()
DD_d = [D for D,i in DD_di]

def solve(x):
    idx = bisect.bisect_right(DD_d, x)
    path = [0]*(N+2)
    for D,i in DD_di[idx:]:
        L,R = LR[i]
        path[L] += 1
        path[R+1] -= 1

    t = N+1
    bp = path[0]
    for i in range(1,N+2):
        p = bp + path[i]
        if p > 0:
            t += 2
        bp = p

    return t <= T


OK = (10**5) * 2 + 10
NG = -1

while OK-NG > 1:
    mid = (OK+NG)//2
    if solve(mid):
        OK = mid
    else:
        NG = mid

ans = 0
for A in AA:
    if A >= OK:
        ans += 1

print(ans)