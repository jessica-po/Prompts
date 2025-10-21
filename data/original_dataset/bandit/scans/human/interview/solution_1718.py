N, K = map(int,input().split())
A = list(map(int,input().split()))

if N == K:
  print(1)
else:
  ans = 1
  N -= K
  while N > 0:
    ans += 1
    N -= (K-1)
  print(ans)