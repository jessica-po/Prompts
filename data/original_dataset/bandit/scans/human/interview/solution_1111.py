n, k = list(map(int, input().split()))

MOD = 10**9+7


def fast_modinv(up_to, M):
    ''' Fast modular inverses of 1..up_to   modulo M. '''
    modinv = [-1 for _ in range(up_to + 1)]
    modinv[1] = 1
    for x in range(2, up_to + 1):
        modinv[x] = (-(M//x) * modinv[M%x])%M
    return modinv

maxn = 2*10**5 + 10
modinv = fast_modinv(maxn, MOD)
fact, factinv = [1], [1]
for i in range(1, maxn):
    fact.append(fact[-1]*i % MOD)
    factinv.append(factinv[-1]*modinv[i] % MOD)


def Stirling(n, k):
    '''The Stirling number of second kind (number of nonempty partitions). '''
    if k > n:
        return 0
    result = 0
    for j in range(k+1):
        result += (-1 if (k-j)&1 else 1) * fact[k] * factinv[j] * factinv[k - j] * pow(j, n, MOD) % MOD
        result %= MOD
    result *= factinv[k]
    return result % MOD

W = sum(map(int, input().split())) % MOD
print((Stirling(n, k) + (n - 1) * Stirling(n - 1, k))* W % MOD)