import sys
input = sys.stdin.readline
from itertools import permutations, accumulate
import heapq
import bisect
from operator import itemgetter

def dijkstra(start, edge):
    n = len(edge)
    dist = [0]*n
    que = [(0, start)]
    while que:
        d, v = heapq.heappop(que)
        if dist[v] < d:
            continue
        for nv, nd in edge[v]:
            if dist[nv] > d + nd:
                dist[nv] = d + nd
                heapq.heappush(que, (dist[nv], nv))
    return dist

n, m = map(int, input().split())
W = tuple(map(int, input().split()))
LV = sorted((tuple(map(int, input().split())) for _ in range(m)), key=itemgetter(1))
L, V = zip(*LV)
P = [0]
w_max = max(W)
for l, v in LV:
  if w_max > v:
    print(-1)
    return
  if P[-1] > l:
    P.append(P[-1])
  else:
    P.append(l)
def f(K):
  S = list(accumulate((W[k] for k in K)))
  edge = [[] for _ in range(n)]
  for i in range(n-1):
    edge[i+1].append((i, 0))
  for i in range(n-1):
    for j in range(i+1, n):
      if i == 0:
        t = S[j]
      else:
        t = S[j] - S[i-1]
      p = P[bisect.bisect_left(V, t)]
      edge[j].append((i, -p))
  return -dijkstra(n-1, edge)[0]

ans = float("inf")
for K in permutations(range(n)):
  ans = min(ans, f(K))
print(ans)