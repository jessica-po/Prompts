mod = int(1e9) + 7 # <-- input modulo
maxf = 500000           # <-- input factional limitation

def make_fact(n, k):
    tmp = n
    perm = [i for i in range(k)]
    L = [0 for _ in range(k)]
    for i in range(k):
        L[i] = tmp % (i + 1)
        tmp //= i + 1
    LL = [0 for _ in range(k)]
    for i in range(k):
        LL[i] = perm[L[-i-1]]
        for j in range(L[-i-1]+1, k):
            perm[j-1] = perm[j]
    return LL

def doubling(n, m, modulo=mod):
    y = 1
    base = n
    tmp = m
    while tmp != 0:
        if tmp % 2 == 1:
            y *= base
            if modulo > 0:
                y %= modulo
        base *= base
        if modulo > 0:
            base %= modulo
        tmp //= 2
    return y

def inved(a, modulo=mod):
    x, y, u, v, k, l = 1, 0, 0, 1, a, modulo
    while l != 0:
        x, y, u, v = u, v, x - u * (k // l), y - v * (k // l)
        k, l = l, k % l
    return x % modulo

fact = [1 for _ in range(maxf+1)]
invf = [1 for _ in range(maxf+1)]

for i in range(maxf):
    fact[i+1] = (fact[i] * (i+1)) % mod
invf[-1] = inved(fact[-1])
for i in range(maxf, 0, -1):
    invf[i-1] = (invf[i] * i) % mod
n, k = map(int, input().split())
S = 0
if n <= k + 1:
    print(fact[2*n-1]*invf[n]*invf[n-1]%mod)
else:
    S = 0
    for i in range(min(n, k+1)):
        S += invf[i]*invf[i]*invf[n-i-1]*invf[n-i]%mod
        S %= mod
    print(S*fact[n-1]*fact[n]%mod)