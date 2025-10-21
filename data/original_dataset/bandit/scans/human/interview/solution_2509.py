N, K = map(int, input().split())
ans = 0

if K == 0:
  print(N**2)
  return

for r in range(K, N):
  for q in range((N-r)//(r+1) + 1):
    if q == 0:
      ans += N - r
    else:
      ans += max(0, (N-r)//q - r)

print(ans)