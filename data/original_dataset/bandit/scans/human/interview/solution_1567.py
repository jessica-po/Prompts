def modfac(n, MOD):
 
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
    return factorials, invs


def modnCr(n,r,mod,fac,inv):
    return fac[n] * inv[n-r] * inv[r] % mod


n,k = map(int,input().split())
mod = 998244353
fac,inv = modfac(n+10,mod)
ans = 0

for i in range(1,n+1):

    rem = n // i - 1
    if rem >= k-1:
        ans += modnCr(rem,k-1,mod,fac,inv)
        ans %= mod

print (ans)