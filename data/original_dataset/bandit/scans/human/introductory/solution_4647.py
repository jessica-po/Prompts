n = int(input())
a = list(map(int, input().split()))
g = [list() for _ in range(n)]
for _ in range(n-1):
  u,v = list(map(int, input().split()))
  g[u-1].append(v-1)
  g[v-1].append(u-1)
st = [x*2-1 for x in a] + [0]
p = [-1]*n
q = [0]
while q:
  v = q.pop()
  for x in g[v]:
    if x == p[v]: continue
    p[x] = v
    q.append(x)
      
seen = [0]*n
q = [0]
while q:
  v = q[-1]
  if seen[v]:
    q.pop()
    if st[v] > 0:
      st[p[v]] += st[v]
  else:
    for x in g[v]:
      if x == p[v]: continue
      q.append(x)
    seen[v] = 1

seen = [0]*n
q = [0]
while q:
  v = q.pop()
  for x in g[v]:
    if x == p[v]: continue
    c = st[v]
    if st[x] > 0: c -= st[x]
    if c > 0: st[x] += c
    q.append(x)

print(*st[:n])