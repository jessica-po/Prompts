n, m, k = map(int, input().split())
mod = 998244353

def powerDX(n, r, mod):
  if r == 0: return 1
  if r%2 == 0:
    return powerDX(n*n % mod, r//2, mod) % mod
  if r%2 == 1:
    return n * powerDX(n, r-1, mod) % mod

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
 
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]
 
for i in range(2, n + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

ans = 0
for i in range(0, k+1):
  ans += m*cmb(n-1, i, mod)*pow(m-1, n-i-1, mod)
  ans %= mod
print(ans)