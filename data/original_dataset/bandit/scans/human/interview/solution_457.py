x, n = list(map(int, input().split()))

def primeFactor(N):
    i, n, ret, d, sq = 2, N, {}, 2, 99
    while i <= sq:
        k = 0
        while n % i == 0: n, k, ret[i] = n//i, k+1, k+1
        if k > 0 or i == 97: sq = int(n**(1/2)+0.5)
        if i < 4: i = i * 2 - 1
        else: i, d = i+d, d^6
    if n > 1: ret[n] = 1
    return ret

pf = primeFactor(x)
mod = 10 ** 9 + 7
def calc(p):
    s = 0
    a = n//p
    while a:
        s += a
        a //= p
    return pow(p, s, mod)

ans = 1
for p in pf:
    ans = ans * calc(p) % mod
print(ans)