n,m = map(int,input().split())
graph = [[float("inf")]*(n+1) for _ in range(n+1)]
for i in range(m):
  a,b,c = map(int,input().split())
  graph[a][b] = c
  graph[b][a] = c

    

def dijkstra(s,cost):
  d = [float("inf")]*(n+1)
  used = [False]*(n+1)
  d[s] = 0
  
  while True:
    v = -1
    for i in range(1,n+1):
      if (not used[i]) and (v == -1):
        v = i
      elif (not used[i]) and d[i] < d[v]:
        v = i
    if v == -1:
      break
    used[v] = True
               
    for j in range(1,n+1):
      d[j] = min(d[j],d[v]+cost[v][j])
  return d

ans = 0
for i in range(1,n):
  d = dijkstra(i,graph)
  for j in range(i+1,n+1):
    if i == j:
      continue
    if graph[i][j] != float("inf") and graph[i][j] > d[j]:
      ans += 1
print(ans)