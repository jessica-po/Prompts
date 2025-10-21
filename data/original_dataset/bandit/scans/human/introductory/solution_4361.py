n,k = map(int,input().split())
L = sorted(list(int(input()) for _ in range(n)))
m = 10**9

for i in range(n-k+1):
  m = min(m, L[i+k-1]-L[i])

print(m)