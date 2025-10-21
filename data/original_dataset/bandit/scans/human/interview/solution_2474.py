mod = 10**9 + 7

def power(p, e):
  ret = 1
  while(e):
    if(e & 1):
      ret *= p
      ret %= mod
    p *= p
    e >>= 1
  return ret

N = int(input())
C = list(map(int, input().split()))
C.sort()

f = 0
for i in range(N):
  f += (N - i + 1) * C[i]
  f %= mod

f *= power(2, N - 1)**2 % mod
f %= mod
print(f)