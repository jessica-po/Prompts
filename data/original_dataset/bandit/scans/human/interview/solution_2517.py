from itertools import permutations as p

from scipy.sparse.csgraph import floyd_warshall

n, m, r = map(int, input().split())
R = list(map(int, input().split()))
l = [[0]*n for _ in range(n)]
for _ in range(m):
  a, b, c = map(int, input().split())
  a -= 1
  b -= 1
  l[a][b] = c
  l[b][a] = c
F = floyd_warshall(l)

ans = float("inf")
for v in p(R):
  temp = 0
  for i in range(r-1):
    temp += F[v[i]-1][v[i+1]-1]
  ans = min(ans, temp)
  
print(int(ans))