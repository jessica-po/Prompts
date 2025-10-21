N,M,K = map(int,input().split())

INF = 10**6+1
from collections import defaultdict

incoming = defaultdict(list)
outgoing = defaultdict(list)

for _ in range(M):
  d,f,t,c = map(int,input().split())
  if t == 0:
    incoming[d].append((c,f-1))
  if f == 0:
    outgoing[d].append((c,t-1))

incoming_dates = sorted(incoming.keys())
outgoing_dates = sorted(outgoing.keys(),reverse=True)



Li = []
mark = [False]*N
cnt = 0
costs = [0]*N
total_cost = 0

for d in incoming_dates:
  for c,x in incoming[d]:
    if mark[x]:
      if costs[x] > c:
        total_cost += c-costs[x]
        costs[x] = c
    else:
      mark[x] = True
      cnt += 1
      costs[x] = c
      total_cost += c

  if cnt == N:
    Li.append((d,total_cost))


Lo = []
mark = [False]*N
cnt = 0
costs = [0]*N
total_cost = 0

for d in outgoing_dates:
  for c,x in outgoing[d]:
    if mark[x]:
      if costs[x] > c:
        total_cost += c-costs[x]
        costs[x] = c
    else:
      mark[x] = True
      cnt += 1
      costs[x] = c
      total_cost += c

  if cnt == N:
    Lo.append((d,total_cost))

Lo.reverse()


if not Li or not Lo:
  print(-1)
  return


# print(Li,Lo)

from bisect import bisect

best = float('inf')

for d,c in Li:
  i = bisect(Lo,(d+K+1,0))
  if i >= len(Lo):
    break
  else:
    best = min(best,c+Lo[i][1])

if best == float('inf'):
  print(-1)
else:
  print(best)