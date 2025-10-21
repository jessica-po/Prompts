def comb_mod(n,r):
    mod = 10**9+7
    ans = 1
    for i in range(r):
        ans *= n-i
        ans %= mod
    for i in range(1,r+1):
        ans *= pow(i,mod-2,mod)
        ans %= mod
    return ans

def solve():
    n, a, b = list(map(int, input().split()))
    mod = 10**9+7
    ans = pow(2,n,mod)-comb_mod(n,a)-comb_mod(n,b)-1
    ans %= mod
    return ans
print((solve()))