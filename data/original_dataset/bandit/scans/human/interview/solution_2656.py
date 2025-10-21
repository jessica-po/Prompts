from functools import reduce
def comb(n, max_k, mod):
    """
    (n,k) := n個からk個選ぶ組み合わせ
    k = 0~max_Kまでを計算して返す
    """
    res = [1]*(max_k+1)
    t = 1
    for i in range(max_k+1):
        res[i] *= t
        t *= n-i
        t %= mod

    n = reduce(lambda x,y: (x*y)%mod, range(1,max_k+1), 1)
    n = pow(n,-1, mod)

    for i in reversed(range(max_k+1)):
        res[i] *= n
        res[i] %= mod
        n *= i
        n %= mod
    return res

MOD = 10**9+7

K = int(input())
N = len(input())

res = 0
x = 1

com = comb(N+K, K, MOD)

for c in com:
    res += x*c
    res %= MOD
    x *= 25
    x %= MOD

print(res)