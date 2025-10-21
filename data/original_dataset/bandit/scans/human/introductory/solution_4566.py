n,m = map(int, input().split())
c = [0 for _ in range(n)]
for i in range(m):
  a,b = map(int, input().split())
  c[a-1] += 1
  c[b-1] += 1
for j in range(n):
  print(c[j])