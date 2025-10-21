import collections
N, M, K = map(int, input().split())
friend = [[] for i in range(N)]
block = [[] for i in range(N)]
graph = [-1] * N
for i in range(M):
  a, b = map(int, input().split())
  friend[a-1].append(b-1)
  friend[b-1].append(a-1)
  
for i in range(K):
  c, d = map(int, input().split())
  block[c-1].append(d-1)
  block[d-1].append(c-1)
  
#print(friend, block)

used = [True] * N
for i in range(N):
  if used[i]:
    q = [i]
    used[i] = False
    graph[i] = i
    while q:
      now = q.pop()
      for j in friend[now]:
        if used[j]:
          graph[j] = graph[now]
          q.append(j)
          used[j] = False
          
          
#print(graph)          
gg = dict(collections.Counter(graph))  
#print(gg)

for i in range(N):
  nn = graph[i]
  size = gg[nn]
  ans = size - 1
  for j in friend[i]:
    if nn == graph[j]:
      ans -= 1
  for j in block[i]:
    if nn == graph[j]:
      ans -= 1
  print(ans, end = " ")